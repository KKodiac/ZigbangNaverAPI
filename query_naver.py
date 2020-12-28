import requests
import pprint
import geohash2
from urllib.parse import urljoin
import json
from options import naver_url as nv

class NaverAPI:
    def __init__(self, query: str):
        self.url = urljoin(nv.NAVER_BASE_URL, nv.NAVER_SEARCH_URL.format(query))
        self._json = requests.get(url).content.decode('utf-8') # raw-byte 를 utf-8로 디코딩

    def show_json(self):
        print(self._json)
        return self._json

    def save_as_file(self):
        with open('content_json.json','w+') as file:
            file.write(_json)
            file.close()

# print(parsed)
