class NAVER_URL:
    NAVER_BASE_URL = "https://m.map.naver.com"
    NAVER_SEARCH_URL = "/search2/searchMore.nhn?query={}&page=1&displayCount=75&type=SITE_1"


class ZIGBANG_URL:
    ZIGBANG_BASE_URL = "https://apis.zigbang.com"
    ZIGBANG_subway_all = "/property/biglab/subway/all?"
    v1_url = "/v1/items/{}/read"                   # {room_id}
    v2_url = {
        "items": "/v2/items?geohash={}",
        "search_servicetype": "/v2/search?q={}&serviceType={}",# {query_item} , {room_type} 
        "search" : "/v2/search?q={}",
        "subways": "/v2/subways/{}",               # {subway_id}
        "items_info": "/v2/items/{}",              # {room_id}
        "agents": "/v2/agents/{}",                 # {agent_id}
    }
    v3_url = {
        "ads": "/v3/items/ad/{}",                  # {subway_id}
    }
