import re

from pathlib import Path
from pptx import Presentation

from Slide import Slide


class Pres(object):

    def __init__(self, path, course):
        my_file = Path(path)
        if my_file.is_file() and (path.endswith('.pptx')):
            self.prs = Presentation(path)
            self.course = course
            self.slides = []
            self.stop_words = set(line.strip() for line in open('stop_words.txt'))
        else:
            raise Exception("No Presentation is found")

    def parse_title(self, title):
        delimiters = " ", ",", ";" "." "?" "\n" "\t"
        regex_pattern = '|'.join(map(re.escape, delimiters))
        words = re.split(regex_pattern, title)
        for word in words:
            if word in self.stop_words:
                title.replace(word, '')
        return title

    def initialize(self):
        for slide in self.prs.slides:
            if not slide.shapes.title.has_text_frame:
                continue
            title = self.parse_title(slide.shapes.title.text)
            s = Slide(title, "", self.prs.slides.index(slide), False, False, False, False)
