# 직방 / 네이버 맵 API 

WEB inspector 로 알아본 직방과 네이버 맵 API 호출 내용입니다.

## API 정리
### 직방
직방 API 는 따로 documentation 이 없습니다.. ㅠㅠㅠ 일단 web inspector 로 알아본 사항만 나열 해 볼게요.
1. 기본 API URL
    - [기본URL](https://apis.zigbang.com/)
    > 클릭하면 아마 json 오류 떠 있을 거 같긴 합니다..
2. V1
    - /items/{room_id}/read
        - 해당 매물의 id 의 *상세 설명* 을 문자열로 보여줍니다.
3. V2
    - items
        - 해당 geohash 내에 있는 items 의 *위치정보, item id* 를 보여줍니다.
        - 웹에서는 맵에서 보여지는 해당 geohash 내의 값들이 브라우저로 로딩되면서 cache가 쌓여 오랬동안 해당 작업을 웹으로 할 경우 브라우저가 헤비해 질 수도 있을 거 같습니다.
    ```
    {
    "clusters": [],
    "items": [
        {
            "lat": 36.38675586127603,
            "lng": 127.34890423511645,
            "item_id": 25083999
        },
        {
            "lat": 36.38675247781794,
            "lng": 127.3484234690869,
            "item_id": 25144856
        }, ...
    ]
    }
    ```
    - search
        - 쿼리를 넣을 때 ajax로 불러지는 해당 api call 에 대한 json 값으로 보여집니다.
        > https://apis.zigbang.com/v2/search?q=신촌역&serviceType=원룸 이런 느낌으로
    ```
    {
    {
    "success": true,
    "code": "200",
    "items": [
        {
            "id": 49,
            "type": "subway",
            "name": "신촌역",
            "hint": "2호선",
            "description": "서울특별시 서대문구 창천동",
            "lat": 37.5551399,
            "lng": 126.9369074,
            "zoom": 3,
            "polygon": [
                [
                    474.75,
                    611
                ], ...
            ],
            "_score": null,
            "_source": {
                "name_length": 3,
                "local1": "서울특별시",
                "local2": "서대문구",
                "local3": "창천동",
                "suggestions": [],
                "suggestions_insensitive": [],
                "distance": 1000
            },
            "zoom_level": {
                "google": 14,
                "daum": 4
            },
            "zoom_level_v2": {
                "app": 6,
                "web": 4
            }
        },
        {
            "id": 153,
            "type": "subway",
            "name": "신촌역",
            "hint": "경의선",
            "description": "서울특별시 서대문구 신촌동",
            "lat": 37.5598030090332,
            "lng": 126.941917419434,
            "zoom": 3,
            "polygon": [],
            "_score": null,
            "_source": {
                "name_length": 3,
                "local1": "서울특별시",
                "local2": "서대문구",
                "local3": "신촌동",
                "suggestions": [],
                "suggestions_insensitive": [],
                "distance": 1000
            },
            "zoom_level": {
                "google": 14,
                "daum": 4
            },
            "zoom_level_v2": {
                "app": 6,
                "web": 4
            }
        }
    ],
    "next": null,
    "limit": 0
    }
    ```
    - /subways
        - /{지하철 id}
            - 직방 API 중 전국 지하철에 대한 id 값을 가져와 이름으로 하여 보여줍니다
            - *지하철 id, 해당 역 이름* 을 보여줍니다.
            ```
            {
                "subway_id": 586,
                "name": "유성온천(충남대·목원대)역"
            }   
            ```
    - /items
            - 전반적인 방의 정보를 포함하고 있습니다. 
            - 대표적으로는 *방id, 이미지, 월세/전세, 보증금, 월세* 등 입니다. 
    ```
    {
            "section_type": null,
            "item_id": 25187082,
            "images_thumbnail": "https://ic.zigbang.com/ic/items/25187082/1.jpg",
            "sales_type": "월세",
            "sales_title": "월세",
            "deposit": 200,
            "rent": 32,
            "size_m2": 26.44,
            "공급면적": {
                "m2": 26.44,
                "p": "8"
            },
            "전용면적": {
                "m2": 26.44,
                "p": "8"
            },
            "계약면적": null,
            "room_type_title": null,
            "floor": "2",
            "floor_string": "2",
            "building_floor": "4",
            "title": "💚💚💚초대형붙박이장^^리모델링원룸💚침대입고💚",
            "is_first_movein": null,
            "room_type": "02",
            "address": "유성구 장대동",
            "random_location": {
                "lat": 36.35824046006694,
                "lng": 127.33838425263652
            },
            "is_zzim": false,
            "status": true,
            "service_type": "원룸",
            "tags": [
                "추천"
            ],
            "address1": "대전시 유성구 장대동",
            "address2": null,
            "address3": null,
            "manage_cost": "1.3",
            "reg_date": "2020-12-15T11:47:54+09:00",
            "is_new": false
        },...
    ```
    - /{room_id}
        - 매물 id 에 해당하는 정보를 보여줍니다. 
    ```
                {
        "item": {
            "item_id": 25322645,
            "user_no": 9407854,
            "sales_type": "월세",
            "sales_title": "월세",
            "service_type": "원룸",
            "images": [
                "https://ic.zigbang.com/ic/items/25322645/1.jpg",
                "https://ic.zigbang.com/ic/items/25322645/2.jpg",
                "https://ic.zigbang.com/ic/items/25322645/3.jpg",
                "https://ic.zigbang.com/ic/items/25322645/4.jpg",
                "https://ic.zigbang.com/ic/items/25322645/5.jpg",
                "https://ic.zigbang.com/ic/items/25322645/6.jpg",
                "https://ic.zigbang.com/ic/items/25322645/7.jpg",
                "https://ic.zigbang.com/ic/items/25322645/8.jpg",
                "https://ic.zigbang.com/ic/items/25322645/9.jpg",
                "https://ic.zigbang.com/ic/items/25322645/10.jpg"
            ],
            "image_thumbnail": "https://ic.zigbang.com/ic/items/25322645/1.jpg",
            "매매금액": null,
            "보증금액": 1000,
            "월세금액": 51,
            "전용면적_m2": 29.75,
            "공급면적_m2": 29.75,
            "대지권면적_m2": null,
            "address": "서대문구 연희동",
            "jibunAddress": null,
            "local1": "서울시",
            "local2": "서대문구",
            "local3": "연희동",
            "local4": null,
            "room_type_code": "02",
            "room_type": "02",
            "title": "⚽연희동 연대인근 1.5룸 분리형 고양이가능⚽",
            "status": "open",
            "description": "연희동 연희교차로 인근에 있는 원룸입니다\r\n\r\n대로변에 가까워서 안전하구요\r\n\r\n연대 서문 3분이면 갑니다\r\n\r\n주방및거실 따로 분리되어 있고 방따로 베란다 따로 있습니다\r\n\r\n주차 가능하며 애완동물은 짖지 않는 동물만 가능합니다(고양이 가능)",
            "secret_memo": null,
            "is_zzim": null,
            "random_location": "37.5666794731908,126.93185871066368",
            "parking": "1대 가능",
            "elevator": false,
            "room_direction": "E",
            "movein_date": "즉시 입주",
            "agent_comment": "English ok\r\nkakaotalk  id :  jitaeboa1201",
            "pnu": "1141011700101870005",
            "floor": "2",
            "floor_string": "2",
            "floor_all": "3층",
            "pets": null,
            "loan": null,
            "building_id": null,
            "options": "01;02;03;04;07;10;11;12;",
            "manage_cost": 3,
            "manage_cost_inc": "03;",
            "is_realestate": true,
            "is_room": false,
            "is_owner": null,
            "is_premium": true,
            "is_homepage": true,
            "user_has_penalty": false,
            "building_type": null,
            "room_gubun_code": "01",
            "view_count": 0,
            "updated_at": "2020-12-24 15:48:44",
            "is_first_movein": null,
            "vr_key": null,
            "vr_type_name": null,
            "approve_date": "1995.06.09",
            "bathroom_count": 1,
            "residence_type": "단독주택",
            "manage_cost_not_inc": "01;02;04;05;",
            "popular": {
                "title": "인기 있는 집입니다.",
                "description": "지난 24시간 동안 주변에서 이 집에 관심을 보인\n사용자가 급격하게 증가했습니다.",
                "image_url": "https://ic.zigbang.net/vp/upload/popular/pop_img_1.png"
            }
        },
        "agent": {
            "agent_title": "더연희힐공인중개사사무소",
            "agent_address": "서울특별시 서대문구 연희로5길 16-13, 7층 701호(연희동, 더연희힐)",
            "agent_phone": "010-5503-1821",
            "agent_intro": "English ok\r\nkakaotalk  id :  jitaeboa1201",
            "owner": {
                "agent_title": "더연희힐공인중개사사무소",
                "agent_user_type": "대표공인중개사",
                "owner_user_no": 9407854,
                "owner_name": "하준",
                "owner_phone": "0507-1280-9187",
                "profile_url": "https://ic.zigbang.com/vp/profile/9407854/bfe914680fe0ccf2333423a67d0c6cd6aeb21e6e.jpg"
            }
        },
        "register": {
            "agent_user_type": "대표공인중개사",
            "register_user_no": 9407854,
            "register_name": "하준",
            "register_phone": "0507-1280-9187"
        },
        "subways": [
            {
                "id": 153,
                "name": "신촌역",
                "description": "경의선"
            },
            {
                "id": 48,
                "name": "홍대입구역",
                "description": "2호선,경의선,공항철도"
            },
            {
                "id": 49,
                "name": "신촌역",
                "description": "2호선"
            }
        ],
        "danji": null,
        "is_zzim": null
    }
    ```
    - /agents/{agent_id}
        - 해당 공인 중개사의 정보를 보여줍니다. 
        ```
            {
            "user_name": "김치억",
            "user_no": 442782,
            "address": "서울특별시 서대문구 연세로7길 48 1층(창천동, 코쿤하임)",
            "agent_name": "코쿤공인중개사사무소",
            "agent_phone": "02-365-9100",
            "agent_regid": "11410-2015-00016",
            "mobile_phone": "0504-3129-6737",
            "intro": "신촌 중개 전문 코쿤 부동산입니다.\r\n서대문구, 마포구 등 원하시는 조건에 맞는 물건을 찾아 드리겠습니다.\r\n \r\n상담도 가능하니 부담 갖지 마시고\r\n전화, 문자, 카톡, 메일 등 코쿤 부동산으로 연락 주세요\r\n \r\n정직, 정확, 성실한 중개로 쉽고 편안하게 찾으실 수 있도록 도와 드립니다!",
            "lat": 37.5580635,
            "lng": 126.93427999999999,
            "items": [
                {
                    "id": 25336373
                }
            ],
            "profile_url": "https://ic.zigbang.com/vp/profile/442782.jpg",
            "중개전문분야": "빌라 / 원룸",
            "local1": "서울시",
            "local2": "서대문구",
            "local3": "신촌동",
            "한국감정원": false,
            "한국부동산원": false
           }
        ```

4. V3
    - /items/ad/{장소id}
        - 해당되는 장소에 대한 (광고)주님들의 목록을 표시합니다. 
    ```
    {
    "list_items": [
        {
            "simple_item": {
                "item_id": 25338352
            },
            "section_title": "이 지역 <b>추천 방</b>",
            "section_type": "premium_recommand",
            "position": 0
        },
        {
            "simple_item": {
                "item_id": 25294273
            },
            "section_title": "이 지역 <b>추천 방</b>",
            "section_type": "premium_recommand",
            "position": 1
        },
        {
            "simple_item": {
                "item_id": 25225793
            },
            "section_title": "이 지역 <b>추천 방</b>",
            "section_type": "premium_recommand",
            "position": 2
        }, ...
    ]
    }
    ```
