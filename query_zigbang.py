import requests 
from bs4 import BeautifulSoup as bs4
import geohash2
from urllib.parse import urljoin
import json
from options import ZIGBANG_URL as zg
# geohash_url = "v2/items?deposit_gteq=0&domain=zigbang&geohash={}&rent_gteq=0&sales_type_in=전세%7C월세&service_type_eq=원룸".format(geohash)

class ZigbangAPI:
    def __init__(self):
        pass

    def _get_geohash(self, lat: float, lng: float, prec=5):
        _geohash = geohash2.encode(lat, lng, precision=prec)
        return _geohash
    
    def _get_json(self, url: str):
        _json = requests.get(url).content.decode('utf-8')
        
        return _json

    def get_room_info_all(self, query, roomtype):
        # test value
        _json = self.get_query_result(query, roomtype)
        
        lat = _json["items"][0]["lat"]
        lng = _json["items"][0]["lng"]
        geohash = self._get_geohash(lat,lng)
        url = urljoin(zg.ZIGBANG_BASE_URL, zg.v2_url["items"].format(geohash))
        _json = self._get_json(url)

        return json.loads(_json)

    def get_room_info_detail(self, room_id: str):
        url = urljoin(zg.ZIGBANG_BASE_URL, zg.v2_url['search'].format(room_id))
        _json = self._get_json(url)
        
        return json.loads(_json)

    def get_query_result(self, query: str, roomtype=None):
        if(roomtype is None):
            url = urljoin(zg.ZIGBANG_BASE_URL, zg.v2_url['search'].format(query))
        else:
            url = urljoin(zg.ZIGBANG_BASE_URL, zg.v2_url['search'].format(query, roomtype))
        _json = self._get_json(url)
        
        return json.loads(_json) 

    def get_subway_result(self, subway_id: int):
        url = urljoin(zg.ZIGBANG_BASE_URL, zg.v2_url['subways'].format(subway_id))
        _json = self._get_json(url)

        return json.loads(_json)

    def get_subway_result_all(self):
        url = urljoin(zg.ZIGBANG_BASE_URL, zg.ZIGBANG_subway_all)
        _json = self._get_json(url)
        
        return json.loads(_json)

    def save_json_to_file(self, filename: str, content_json):
        with open(f'{filename}.json', 'w+') as f:
            f.write(content_json)
            f.close()

if __name__=='__main__':
    z_api = ZigbangAPI()
    query = "노은역"
    roomtype = "원룸"
    data = z_api.get_room_info_all(query, roomtype)
    print(data['items'])
    print(data[''])