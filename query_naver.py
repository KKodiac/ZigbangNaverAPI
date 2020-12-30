import requests
import pprint
import geohash2
from urllib.parse import urljoin
import json
from options import NAVER_URL as nv

class NaverAPI:
    def __init__(self, query: str):
        self.url = urljoin(nv.NAVER_BASE_URL, nv.NAVER_SEARCH_URL.format(query))
        self._json = requests.get(self.url).content.decode('utf-8') # raw-byte 를 utf-8로 디코딩

    def get_json(self):
        # print(self._json)
        _js = json.loads(self._json)
        _json_list = _js['result']['site']['list']
        
        return _json_list

    def save_as_file(self):
        with open('content_json.json','w+') as file:
            file.write(self.get_json())
            file.close()

nv = NaverAPI("노은역gs25")
nv.get_json()