import Search
from Presentation import Pres

present = Pres("sample.pptx", "sample")
present.initialize()
Search.runSearch(present.slides)
present.create_new_presentation()
