from .base_provider import BaseProvider, Options


class AnitakuProvider(BaseProvider):
    def __init__(self, options: Options, provider):
        super().__init__(options, provider)

    def search(self):
        print("searching")
