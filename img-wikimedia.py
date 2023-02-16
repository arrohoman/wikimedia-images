import requests
from requests import get
from pprint import pprint
import http
# from pyWikiCommons import pyWikiCommons
#
# # pyWikiCommons.get_commons_url("File:Flag_of_Germany.svg")
# pyWikiCommons.download_commons_image("File:Flag_of_Germany.jpg")
# pyWikiCommons.get_commons_url("File:Flag_of_Germany.jpg")

# url = 'https://commons.wikimedia.org/w/api.php?action=query&generator=images&prop=imageinfo&gimlimit=500&redirects=1&titles=Cat&iiprop=timestamp|user|userid|comment|canonicaltitle|url|size|dimensions|sha1|mime|thumbmime|mediatype|bitdepth'
url = 'https://commons.wikimedia.org/w/api.php?format=json&action=query&generator=images&prop=imageinfo&gimlimit=50&redirects=1&titles=crow&iiprop=timestamp|user|userid|comment|canonicaltitle|url|size|dimensions|sha1|mime|thumbmime|mediatype|bitdepth'
s = requests.get(url).json()


images = s.get('query').get('pages')
# print(images)
for img_num, img_detail in images.items():
    id = img_detail
    ind_img_title = id.get('imageinfo')[0].get('canonicaltitle')
    ind_img_url = id.get('imageinfo')[0].get('url')
    ind_img_srt_url = id.get('imageinfo')[0].get('descriptionshorturl')
    ind_img_desc_url = id.get('imageinfo')[0].get('descriptionshorturl')
    ind_img_download_url = get(ind_img_url)
    # print(ind_img_url)
    with open('images/'+ind_img_title, 'wb') as file:
        file.write(ind_img_download_url.content)