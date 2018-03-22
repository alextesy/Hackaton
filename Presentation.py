from __future__ import print_function

import os

from pathlib import Path
from pptx import Presentation
from pptx.enum.shapes import PP_PLACEHOLDER_TYPE
from pptx.util import Pt
from pptx.util import Cm

from Parser import Parser
from Slide import Slide


def smaller_text(slide):
    for shape in slide.shapes:
        if not shape.has_text_frame:
            continue

        if shape.is_placeholder:
            if shape.placeholder_format.type is PP_PLACEHOLDER_TYPE.TITLE or \
                    shape.placeholder_format.type is PP_PLACEHOLDER_TYPE.CENTER_TITLE:
                continue
        for paragraph in shape.text_frame.paragraphs:
            for run in paragraph.runs:
                run.font.size = Pt(16)


class Pres(object):

    def __init__(self, path, course):
        my_file = Path(path)
        if my_file.is_file() and (path.endswith('.pptx')):
            self.prs = Presentation(path)
            self.path = path
            self.course = course
            self.slides = []
            self.parser = Parser()

        else:
            raise Exception("No Presentation is found")

    def initialize(self):
        for slide in self.prs.slides:
            if slide.shapes.title is None or (not slide.shapes.title.has_text_frame):
                continue
            title = self.parser.parse_title(slide.shapes.title.text)
            s = Slide(title, "", self.prs.slides.index(slide), False, False, False, False)
            self.slides.append(s)

    def create_url_file(self):
        dir, file = os.path.split(self.path)
        url_file_name = os.path.join(dir, "url_links.txt")
        url_file = open(url_file_name, "w")
        for slide in self.slides:
            print(slide.url.path, file=url_file)

    def create_new_presentation(self):
        for slide in self.prs.slides:
            smaller_text(slide)
            img_path = "./downloads/'eagle'"
            left = top = Cm(20)
            height = Cm(40)
            slide.shapes.add_picture(img_path, left, top, height=height)

        self.prs.save("result.pptx")
