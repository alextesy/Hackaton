import os
from PIL import Image
from google import google
from langdetect import detect
import imgkit
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


def articles(slide):
    query = slide.title
    advancedQuery = query + ' site:reuters.com'
    google_result = google.search(advancedQuery, 1)
    idx = 0
    for res in google_result:
        try:
            idx += 1
            lang = detect(res.description)
            if lang == 'en':
                path_wkhtmltoimage = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltoimage.exe'
                config = imgkit.config(wkhtmltoimage=path_wkhtmltoimage)
                article_path = "Articles/" + query + str(idx) + '.jpg'
                imgkit.from_url(res.google_link, article_path, config=config)
                img = Image.open(article_path)
                imgs2 = img.crop((0, 200, 1000, 1000))
                imgs2.save(query + str(idx) + '.jpg')
        except Exception:
            os.remove(query + str(idx) + '.jpg')
            idx -= 1


def runSearch(slides):
    for s in slides:
        searcher(s)


'''
import os
from PIL import Image
from google import google
from langdetect import detect
import imgkit

query = 'eye egg'
advancedQuery = query + ' site:reuters.com'
google_result = google.search(advancedQuery, 2)
idx = 0
for res in google_result:
    try:
        idx += 1
        lang = detect(res.description)
        if lang == 'en':
            path_wkhtmltoimage = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltoimage.exe'
            config = imgkit.config(wkhtmltoimage=path_wkhtmltoimage)
            imgkit.from_url(res.google_link, query + str(idx) + '.jpg', config=config)
            img = Image.open(query + str(idx) + '.jpg')
            imgs2 = img.crop((0, 200, 1000, 1000))
            imgs2.save(query + str(idx) + '.jpg')
    except Exception:
        os.remove(query + str(idx) + '.jpg')
        idx -= 1

'''
