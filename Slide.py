from pptx import Presentation


class Slide:
    def __init__(self,title,content,slideNum,picture,text,meme,video):
        self.title = title
        self.content=content
        self.slideNum = slideNum
        self.picture =picture
        self.text=text
        self.meme=meme
        self.video=video
    def find_links(self):
        return findLinks(self)

