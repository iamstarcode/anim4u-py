from typing import Dict, Optional, List, Generic, List, TypeVar
from pydantic import BaseModel

T = TypeVar("T")


class Search(BaseModel, Generic[T]):
    currentPage: int
    hasNextPage: bool
    totalPages: int
    totalResults: int
    results: List[T]


class IVideo(BaseModel):
    url: str
    quality: Optional[str]
    isM3U8: Optional[bool]
    isDASH: Optional[bool]
    size: Optional[int]


class Source(BaseModel):
    headers: Optional[Dict[str, str]]
    """ intro: Optional[Intro]
    outro: Optional[Intro]
    subtitles: Optional[List[ISubtitle]] """
    sources: List[IVideo]
    download: Optional[str]
    embedURL: Optional[str]
