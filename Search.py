import os
from Slide import Slide
from google import google



def searcher(slide):
    query=slide.title
    query=query[0:-1]
    mypath = 's'+ str(slide.slideNum)
    mypath=mypath[1:5]
    if not os.path.isdir(mypath):
        os.makedirs(mypath)
    s1 = "googleimagesdownload --keywords \""+query+"\" --limit 1 -o "+mypath
    s2="googleimagesdownload --keywords \""+query+" meme\" --limit 1 -o "+mypath
    os.system(s1)  #save pic
    os.system(s2)
    advancedQuery = query + ' site:reuters.com'
    google_result = google.search(advancedQuery, 2)
    for res in google_result:
        i=0
        if i>10:
            continue
        slide.url.append(res.link)



def runSearch(slides):
    for s in slides:
        searcher(s)





