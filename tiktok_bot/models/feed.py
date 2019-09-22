from typing import List

from .feed_enums import FeedType, PullType
from .post import Post
from .request import (
    CursorOffsetRequestParams,
    CursorOffsetResponseParams,
    ListRequestParams,
    ListResponseData,
)


class ListFeedRequest(ListRequestParams, CursorOffsetRequestParams):
    # The type of feed to load
    type: FeedType

    # Your device's current volume level on a scale of 0 to 1, e.g. 0.5
    volume: int

    # How the feed was requested
    pull_type: PullType

    # ??? - empty
    req_from: str = None

    # ??? - 0
    is_cold_start: int = None

    # ???
    gaid: str = None

    # A user agent for your device
    ad_user_agent: str = None


class ListFeedResponse(ListResponseData, CursorOffsetResponseParams):
    # A list of posts in the feed
    aweme_list: List[Post]


class ListForYouFeedResponse(ListFeedResponse):
    # ??? - 1
    home_model: int

    # ??? - 1
    refresh_clear: int
