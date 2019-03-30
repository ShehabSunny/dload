class Source():
    def __init__(self, url:str, *args, **kwargs):
        self.url = url

    def download(self):
        raise NotImplementedError("download function is not implemented")