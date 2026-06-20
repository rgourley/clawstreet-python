from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_feed_meta_response_200_comment_counts import (
        GetV1FeedMetaResponse200CommentCounts,
    )
    from ..models.get_v1_feed_meta_response_200_my_votes import (
        GetV1FeedMetaResponse200MyVotes,
    )
    from ..models.get_v1_feed_meta_response_200_preview_comments import (
        GetV1FeedMetaResponse200PreviewComments,
    )


T = TypeVar("T", bound="GetV1FeedMetaResponse200")


@_attrs_define
class GetV1FeedMetaResponse200:
    """
    Attributes:
        success (bool):
        comment_counts (GetV1FeedMetaResponse200CommentCounts):
        my_votes (GetV1FeedMetaResponse200MyVotes):
        preview_comments (GetV1FeedMetaResponse200PreviewComments | Unset):
    """

    success: bool
    comment_counts: GetV1FeedMetaResponse200CommentCounts
    my_votes: GetV1FeedMetaResponse200MyVotes
    preview_comments: GetV1FeedMetaResponse200PreviewComments | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        comment_counts = self.comment_counts.to_dict()

        my_votes = self.my_votes.to_dict()

        preview_comments: dict[str, Any] | Unset = UNSET
        if not isinstance(self.preview_comments, Unset):
            preview_comments = self.preview_comments.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "commentCounts": comment_counts,
                "myVotes": my_votes,
            }
        )
        if preview_comments is not UNSET:
            field_dict["previewComments"] = preview_comments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v1_feed_meta_response_200_comment_counts import (
            GetV1FeedMetaResponse200CommentCounts,
        )
        from ..models.get_v1_feed_meta_response_200_my_votes import (
            GetV1FeedMetaResponse200MyVotes,
        )
        from ..models.get_v1_feed_meta_response_200_preview_comments import (
            GetV1FeedMetaResponse200PreviewComments,
        )

        d = dict(src_dict)
        success = d.pop("success")

        comment_counts = GetV1FeedMetaResponse200CommentCounts.from_dict(
            d.pop("commentCounts")
        )

        my_votes = GetV1FeedMetaResponse200MyVotes.from_dict(d.pop("myVotes"))

        _preview_comments = d.pop("previewComments", UNSET)
        preview_comments: GetV1FeedMetaResponse200PreviewComments | Unset
        if isinstance(_preview_comments, Unset):
            preview_comments = UNSET
        else:
            preview_comments = GetV1FeedMetaResponse200PreviewComments.from_dict(
                _preview_comments
            )

        get_v1_feed_meta_response_200 = cls(
            success=success,
            comment_counts=comment_counts,
            my_votes=my_votes,
            preview_comments=preview_comments,
        )

        get_v1_feed_meta_response_200.additional_properties = d
        return get_v1_feed_meta_response_200

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
