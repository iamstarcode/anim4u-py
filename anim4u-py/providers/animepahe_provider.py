from .base_provider import BaseProvider, Options


class AnimepaheProvider(BaseProvider):
    def __init__(self, options: Options, provider):
        super().__init__(options, provider)

    """ def __init__(self, *args, **kwargs) -> None:
        super.__init__(options, query, provider, search_path)
        self.options = options
        self.query = query
        self.provider = provider
        self.searchPath = search_path  """

    def search():
        print("searching")
