from typing import List, Union
from pydantic import BaseModel


class FuzzyDate(BaseModel):
    year: int
    month: int
    day: int


class Trailer(BaseModel):
    url: str
    embed: bool


class IAnimeResult(BaseModel):
    # Define fields from IAnimeResult if available
    # ...
    pass


class SubOrSub(BaseModel):
    # Define SubOrSub if needed
    # ...
    pass


class IAnimeEpisode(BaseModel):
    # Define IAnimeEpisode if needed
    # ...
    pass


class IAnimeInfo(BaseModel):
    malId: Union[int, str]
    genres: List[str]
    description: str
    status: str  # Assuming MediaStatus is a string type
    totalEpisodes: int
    subOrDub: SubOrSub  # Assuming SubOrSub is a defined model
    hasSub: bool
    hasDub: bool
    synonyms: List[str]
    countryOfOrigin: str
    isAdult: bool
    isLicensed: bool
    season: str
    studios: List[str]
    color: str
    cover: str
    trailer: Trailer
    episodes: List[IAnimeEpisode]
    startDate: FuzzyDate
    endDate: FuzzyDate
    recommendations: List[IAnimeResult]
    relations: List[IAnimeResult]
