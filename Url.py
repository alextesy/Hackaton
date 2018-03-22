import urllib


class Url:
    def __init__(self, path, flag):
        self.path = path
        self.flag = flag

    def get_content(self, slide_number):
        if self.flag == "img":
            urllib.urlretrieve(self.path, "/" + slide_number + "/" + self.path.rsplit('/', 1)[-1])
        if self.flag == "article":
            pass
