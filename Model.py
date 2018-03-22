from Presentation import Pres
from Slide import Slide
import Search

present = Pres("PresentationGuide.pptx", "sample")
present.initialize()
Search.runSearch(present.slides)
#present.create_new_presentation()