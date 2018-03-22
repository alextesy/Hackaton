import os
from types import NoneType

from google import google


def searcher(slide):
    query = slide.title
    query = query[0:-1]
    my_path = 's' + str(slide.slideNum)
    if query.endswith(" "):
        query = my_path[:-1]
    if not os.path.isdir(my_path):
        os.makedirs(my_path)
    s1 = "googleimagesdownload --keywords \"" + query + "\" --limit 1 -o " + my_path
    s2 = "googleimagesdownload --keywords \"" + query + " meme\" --limit 1 -o " + my_path
    os.system(s1)  # save pic
    os.system(s2)
    advancedQuery = query
    google_result = google.search(advancedQuery, 2)
    i = 0
    for res in google_result:
        if i == 10:
            break
        slide.url.append(res.link)
        i += 1


def runSearch(slides):
    for s in slides:
        searcher(s)
