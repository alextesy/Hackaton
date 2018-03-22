from Presentation import Pres
from Slide import Slide

url = ["http://google.com", "http://www.yent.co.il"]
slides = []
for index in range(0,5):
    s = Slide("", "", index)
    s.url = url
    slides.append(s)


present = Pres("PresentationGuide.pptx", "sample")
present.slides = slides
present.create_new_presentation()

print("done")
