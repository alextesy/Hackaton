from pptx import Presentation
from pathlib import Path


class Pres(object):

    def __init__(self, path):
        my_file = Path(path)
        if my_file.is_file() and (path.endswith('.pptx')):
            self.prs = Presentation(path)
        else:
            raise Exception("No Presentation is found")
