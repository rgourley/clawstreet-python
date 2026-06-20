"""
Smoke tests against the live API. Hits only public endpoints.
"""

from typing import Any

from clawstreet import Bot, AuthenticatedClient, Client, __version__
from clawstreet._typed.api.system import get_v1_health, get_v1


def test_version_is_set() -> None:
    assert __version__ == "0.2.0"


def test_bot_constructor_validates(monkeypatch: Any) -> None:
    import pytest

    monkeypatch.delenv("CLAWSTREET_AGENT_ID", raising=False)
    monkeypatch.delenv("CLAWSTREET_API_KEY", raising=False)
    monkeypatch.delenv("CLAWSTREET_BOT_ID", raising=False)

    with pytest.raises(ValueError, match="agent_id"):
        Bot()
    with pytest.raises(ValueError, match="api_key"):
        Bot(agent_id="x")
    with pytest.raises(ValueError, match="agent_id"):
        Bot(api_key="x")


def test_bot_reads_env(monkeypatch: Any) -> None:
    monkeypatch.setenv("CLAWSTREET_AGENT_ID", "00000000-0000-0000-0000-000000000001")
    monkeypatch.setenv("CLAWSTREET_API_KEY", "tb_live_test")
    bot = Bot()
    assert bot.agent_id == "00000000-0000-0000-0000-000000000001"
    assert bot.api_key == "tb_live_test"


def test_bot_context_manager() -> None:
    with Bot(agent_id="x", api_key="tb_live_test") as bot:
        assert bot.agent_id == "x"


def test_v1_root_metadata() -> None:
    """Public — anyone can hit /v1 to discover the API."""
    client = Client(base_url="https://api.clawstreet.io")
    resp = get_v1.sync(client=client)
    assert resp is not None


def test_v1_health() -> None:
    """Public — health check endpoint."""
    client = Client(base_url="https://api.clawstreet.io")
    resp = get_v1_health.sync(client=client)
    assert resp is not None


