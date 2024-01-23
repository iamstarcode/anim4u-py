from abc import ABC, abstractmethod


class BaseProvider(ABC):
    name: str
    baseURL: str
