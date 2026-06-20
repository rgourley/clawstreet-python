#!/usr/bin/env bash
# Regenerate the typed layer from the production OpenAPI spec.
#
# Output lives at src/clawstreet/_typed/. The hand-written ergonomic Bot
# in src/clawstreet/__init__.py imports from it.
#
# This script:
#   1. Generates into a temp dir using `package_name_override:
#      _clawstreet_typed_raw` (a flat top-level name).
#   2. Moves the inner package into src/clawstreet/_typed/.
#   3. Rewrites internal imports from `_clawstreet_typed_raw.X` to
#      `clawstreet._typed.X` so the package works under the nested
#      namespace.
#
# Run: bash scripts/regen.sh
# CI version is in .github/workflows/regen.yml.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TMP_DIR="$(mktemp -d)"
SPEC_URL="${SPEC_URL:-https://api.clawstreet.io/openapi.json}"
TYPED_DIR="${REPO_ROOT}/src/clawstreet/_typed"

trap 'rm -rf "$TMP_DIR"' EXIT

echo "Generating typed client from ${SPEC_URL}..."
uvx openapi-python-client generate \
  --url "${SPEC_URL}" \
  --config "${REPO_ROOT}/openapi-python-client-config.yaml" \
  --output-path "${TMP_DIR}" \
  --overwrite \
  --meta none

# With --meta none, the generator writes package contents directly to
# --output-path (no wrapper directory). Sanity-check for the expected files.
if [ ! -f "${TMP_DIR}/client.py" ] || [ ! -d "${TMP_DIR}/api" ]; then
  echo "ERROR: expected client.py and api/ in ${TMP_DIR}, not found."
  ls -la "${TMP_DIR}"
  exit 1
fi

echo "Installing into ${TYPED_DIR}..."
rm -rf "${TYPED_DIR}"
mkdir -p "${TYPED_DIR}"
cp -r "${TMP_DIR}/." "${TYPED_DIR}/"
# Drop the ruff cache that openapi-python-client leaves behind.
rm -rf "${TYPED_DIR}/.ruff_cache"

echo "Rewriting internal imports..."
# Rewrite `_clawstreet_typed_raw.X` to `clawstreet._typed.X` everywhere.
# Use python for safe in-place replace (cross-platform vs sed -i).
python3 - <<'PY'
import pathlib
import re

root = pathlib.Path("src/clawstreet/_typed")
pat = re.compile(r'\b_clawstreet_typed_raw\b')
for p in root.rglob("*.py"):
    s = p.read_text()
    new = pat.sub("clawstreet._typed", s)
    if new != s:
        p.write_text(new)
PY

echo "Done. Generated typed layer at src/clawstreet/_typed/."
echo "Next: review diff, run smoke tests, bump pyproject version if shipping."
