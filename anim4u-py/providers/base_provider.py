class BaseProvider:
    def __init__(self, options, query, provider, search_path) -> None:
        self.options = options
        self.query = query
        self.provider = provider
        self.searchPath = search_path
