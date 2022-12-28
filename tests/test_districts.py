from fastapi.testclient import TestClient


def test_get_districts(client: TestClient):
    response = client.get("/api/districts")

    assert response.status_code == 200
    assert response.json() == [
        {
            "name": "中正區",
            "id": 0,
            "county_id": 0
        },
        {
            "name": "大同區",
            "id": 1,
            "county_id": 0
        },
        {
            "name": "中山區",
            "id": 2,
            "county_id": 0
        },
        {
            "name": "萬華區",
            "id": 3,
            "county_id": 0
        },
        {
            "name": "信義區",
            "id": 4,
            "county_id": 0
        },
        {
            "name": "松山區",
            "id": 5,
            "county_id": 0
        },
        {
            "name": "大安區",
            "id": 6,
            "county_id": 0
        },
        {
            "name": "南港區",
            "id": 7,
            "county_id": 0
        },
        {
            "name": "北投區",
            "id": 8,
            "county_id": 0
        },
        {
            "name": "內湖區",
            "id": 9,
            "county_id": 0
        },
        {
            "name": "士林區",
            "id": 10,
            "county_id": 0
        },
        {
            "name": "文山區",
            "id": 11,
            "county_id": 0
        },
        {
            "name": "板橋區",
            "id": 12,
            "county_id": 1
        },
        {
            "name": "新莊區",
            "id": 13,
            "county_id": 1
        },
        {
            "name": "泰山區",
            "id": 14,
            "county_id": 1
        },
        {
            "name": "林口區",
            "id": 15,
            "county_id": 1
        },
        {
            "name": "淡水區",
            "id": 16,
            "county_id": 1
        },
        {
            "name": "金山區",
            "id": 17,
            "county_id": 1
        },
        {
            "name": "八里區",
            "id": 18,
            "county_id": 1
        },
        {
            "name": "萬里區",
            "id": 19,
            "county_id": 1
        },
        {
            "name": "石門區",
            "id": 20,
            "county_id": 1
        },
        {
            "name": "三芝區",
            "id": 21,
            "county_id": 1
        },
        {
            "name": "瑞芳區",
            "id": 22,
            "county_id": 1
        },
        {
            "name": "汐止區",
            "id": 23,
            "county_id": 1
        },
        {
            "name": "平溪區",
            "id": 24,
            "county_id": 1
        },
        {
            "name": "貢寮區",
            "id": 25,
            "county_id": 1
        },
        {
            "name": "雙溪區",
            "id": 26,
            "county_id": 1
        },
        {
            "name": "深坑區",
            "id": 27,
            "county_id": 1
        },
        {
            "name": "石碇區",
            "id": 28,
            "county_id": 1
        },
        {
            "name": "新店區",
            "id": 29,
            "county_id": 1
        },
        {
            "name": "坪林區",
            "id": 30,
            "county_id": 1
        },
        {
            "name": "烏來區",
            "id": 31,
            "county_id": 1
        },
        {
            "name": "中和區",
            "id": 32,
            "county_id": 1
        },
        {
            "name": "永和區",
            "id": 33,
            "county_id": 1
        },
        {
            "name": "土城區",
            "id": 34,
            "county_id": 1
        },
        {
            "name": "三峽區",
            "id": 35,
            "county_id": 1
        },
        {
            "name": "樹林區",
            "id": 36,
            "county_id": 1
        },
        {
            "name": "鶯歌區",
            "id": 37,
            "county_id": 1
        },
        {
            "name": "三重區",
            "id": 38,
            "county_id": 1
        },
        {
            "name": "蘆洲區",
            "id": 39,
            "county_id": 1
        },
        {
            "name": "五股區",
            "id": 40,
            "county_id": 1
        },
        {
            "name": "仁愛區",
            "id": 41,
            "county_id": 2
        },
        {
            "name": "中正區",
            "id": 42,
            "county_id": 2
        },
        {
            "name": "信義區",
            "id": 43,
            "county_id": 2
        },
        {
            "name": "中山區",
            "id": 44,
            "county_id": 2
        },
        {
            "name": "安樂區",
            "id": 45,
            "county_id": 2
        },
        {
            "name": "暖暖區",
            "id": 46,
            "county_id": 2
        },
        {
            "name": "七堵區",
            "id": 47,
            "county_id": 2
        },
        {
            "name": "桃園區",
            "id": 48,
            "county_id": 3
        },
        {
            "name": "中壢區",
            "id": 49,
            "county_id": 3
        },
        {
            "name": "平鎮區",
            "id": 50,
            "county_id": 3
        },
        {
            "name": "八德區",
            "id": 51,
            "county_id": 3
        },
        {
            "name": "楊梅區",
            "id": 52,
            "county_id": 3
        },
        {
            "name": "蘆竹區",
            "id": 53,
            "county_id": 3
        },
        {
            "name": "龜山區",
            "id": 54,
            "county_id": 3
        },
        {
            "name": "龍潭區",
            "id": 55,
            "county_id": 3
        },
        {
            "name": "大溪區",
            "id": 56,
            "county_id": 3
        },
        {
            "name": "大園區",
            "id": 57,
            "county_id": 3
        },
        {
            "name": "觀音區",
            "id": 58,
            "county_id": 3
        },
        {
            "name": "新屋區",
            "id": 59,
            "county_id": 3
        },
        {
            "name": "復興區",
            "id": 60,
            "county_id": 3
        },
        {
            "name": "竹北市",
            "id": 61,
            "county_id": 4
        },
        {
            "name": "竹東鎮",
            "id": 62,
            "county_id": 4
        },
        {
            "name": "新埔鎮",
            "id": 63,
            "county_id": 4
        },
        {
            "name": "關西鎮",
            "id": 64,
            "county_id": 4
        },
        {
            "name": "峨眉鄉",
            "id": 65,
            "county_id": 4
        },
        {
            "name": "寶山鄉",
            "id": 66,
            "county_id": 4
        },
        {
            "name": "北埔鄉",
            "id": 67,
            "county_id": 4
        },
        {
            "name": "橫山鄉",
            "id": 68,
            "county_id": 4
        },
        {
            "name": "芎林鄉",
            "id": 69,
            "county_id": 4
        },
        {
            "name": "湖口鄉",
            "id": 70,
            "county_id": 4
        },
        {
            "name": "新豐鄉",
            "id": 71,
            "county_id": 4
        },
        {
            "name": "尖石鄉",
            "id": 72,
            "county_id": 4
        },
        {
            "name": "五峰鄉",
            "id": 73,
            "county_id": 4
        },
        {
            "name": "東區",
            "id": 74,
            "county_id": 5
        },
        {
            "name": "北區",
            "id": 75,
            "county_id": 5
        },
        {
            "name": "香山區",
            "id": 76,
            "county_id": 5
        },
        {
            "name": "苗栗市",
            "id": 77,
            "county_id": 6
        },
        {
            "name": "通霄鎮",
            "id": 78,
            "county_id": 6
        },
        {
            "name": "苑裡鎮",
            "id": 79,
            "county_id": 6
        },
        {
            "name": "竹南鎮",
            "id": 80,
            "county_id": 6
        },
        {
            "name": "頭份鎮",
            "id": 81,
            "county_id": 6
        },
        {
            "name": "後龍鎮",
            "id": 82,
            "county_id": 6
        },
        {
            "name": "卓蘭鎮",
            "id": 83,
            "county_id": 6
        },
        {
            "name": "西湖鄉",
            "id": 84,
            "county_id": 6
        },
        {
            "name": "頭屋鄉",
            "id": 85,
            "county_id": 6
        },
        {
            "name": "公館鄉",
            "id": 86,
            "county_id": 6
        },
        {
            "name": "銅鑼鄉",
            "id": 87,
            "county_id": 6
        },
        {
            "name": "三義鄉",
            "id": 88,
            "county_id": 6
        },
        {
            "name": "造橋鄉",
            "id": 89,
            "county_id": 6
        },
        {
            "name": "三灣鄉",
            "id": 90,
            "county_id": 6
        },
        {
            "name": "南庄鄉",
            "id": 91,
            "county_id": 6
        },
        {
            "name": "大湖鄉",
            "id": 92,
            "county_id": 6
        },
        {
            "name": "獅潭鄉",
            "id": 93,
            "county_id": 6
        },
        {
            "name": "泰安鄉",
            "id": 94,
            "county_id": 6
        },
        {
            "name": "中區",
            "id": 95,
            "county_id": 7
        },
        {
            "name": "東區",
            "id": 96,
            "county_id": 7
        },
        {
            "name": "南區",
            "id": 97,
            "county_id": 7
        },
        {
            "name": "西區",
            "id": 98,
            "county_id": 7
        },
        {
            "name": "北區",
            "id": 99,
            "county_id": 7
        },
        {
            "name": "北屯區",
            "id": 100,
            "county_id": 7
        },
        {
            "name": "西屯區",
            "id": 101,
            "county_id": 7
        },
        {
            "name": "南屯區",
            "id": 102,
            "county_id": 7
        },
        {
            "name": "太平區",
            "id": 103,
            "county_id": 7
        },
        {
            "name": "大里區",
            "id": 104,
            "county_id": 7
        },
        {
            "name": "霧峰區",
            "id": 105,
            "county_id": 7
        },
        {
            "name": "烏日區",
            "id": 106,
            "county_id": 7
        },
        {
            "name": "豐原區",
            "id": 107,
            "county_id": 7
        },
        {
            "name": "后里區",
            "id": 108,
            "county_id": 7
        },
        {
            "name": "東勢區",
            "id": 109,
            "county_id": 7
        },
        {
            "name": "石岡區",
            "id": 110,
            "county_id": 7
        },
        {
            "name": "新社區",
            "id": 111,
            "county_id": 7
        },
        {
            "name": "和平區",
            "id": 112,
            "county_id": 7
        },
        {
            "name": "神岡區",
            "id": 113,
            "county_id": 7
        },
        {
            "name": "潭子區",
            "id": 114,
            "county_id": 7
        },
        {
            "name": "大雅區",
            "id": 115,
            "county_id": 7
        },
        {
            "name": "大肚區",
            "id": 116,
            "county_id": 7
        },
        {
            "name": "龍井區",
            "id": 117,
            "county_id": 7
        },
        {
            "name": "沙鹿區",
            "id": 118,
            "county_id": 7
        },
        {
            "name": "梧棲區",
            "id": 119,
            "county_id": 7
        },
        {
            "name": "清水區",
            "id": 120,
            "county_id": 7
        },
        {
            "name": "大甲區",
            "id": 121,
            "county_id": 7
        },
        {
            "name": "外埔區",
            "id": 122,
            "county_id": 7
        },
        {
            "name": "大安區",
            "id": 123,
            "county_id": 7
        },
        {
            "name": "南投市",
            "id": 124,
            "county_id": 8
        },
        {
            "name": "埔里鎮",
            "id": 125,
            "county_id": 8
        },
        {
            "name": "草屯鎮",
            "id": 126,
            "county_id": 8
        },
        {
            "name": "竹山鎮",
            "id": 127,
            "county_id": 8
        },
        {
            "name": "集集鎮",
            "id": 128,
            "county_id": 8
        },
        {
            "name": "名間鄉",
            "id": 129,
            "county_id": 8
        },
        {
            "name": "鹿谷鄉",
            "id": 130,
            "county_id": 8
        },
        {
            "name": "中寮鄉",
            "id": 131,
            "county_id": 8
        },
        {
            "name": "魚池鄉",
            "id": 132,
            "county_id": 8
        },
        {
            "name": "國姓鄉",
            "id": 133,
            "county_id": 8
        },
        {
            "name": "水里鄉",
            "id": 134,
            "county_id": 8
        },
        {
            "name": "信義鄉",
            "id": 135,
            "county_id": 8
        },
        {
            "name": "仁愛鄉",
            "id": 136,
            "county_id": 8
        },
        {
            "name": "彰化市",
            "id": 137,
            "county_id": 9
        },
        {
            "name": "員林鎮",
            "id": 138,
            "county_id": 9
        },
        {
            "name": "和美鎮",
            "id": 139,
            "county_id": 9
        },
        {
            "name": "鹿港鎮",
            "id": 140,
            "county_id": 9
        },
        {
            "name": "溪湖鎮",
            "id": 141,
            "county_id": 9
        },
        {
            "name": "二林鎮",
            "id": 142,
            "county_id": 9
        },
        {
            "name": "田中鎮",
            "id": 143,
            "county_id": 9
        },
        {
            "name": "北斗鎮",
            "id": 144,
            "county_id": 9
        },
        {
            "name": "花壇鄉",
            "id": 145,
            "county_id": 9
        },
        {
            "name": "芬園鄉",
            "id": 146,
            "county_id": 9
        },
        {
            "name": "大村鄉",
            "id": 147,
            "county_id": 9
        },
        {
            "name": "永靖鄉",
            "id": 148,
            "county_id": 9
        },
        {
            "name": "伸港鄉",
            "id": 149,
            "county_id": 9
        },
        {
            "name": "線西鄉",
            "id": 150,
            "county_id": 9
        },
        {
            "name": "福興鄉",
            "id": 151,
            "county_id": 9
        },
        {
            "name": "秀水鄉",
            "id": 152,
            "county_id": 9
        },
        {
            "name": "埔心鄉",
            "id": 153,
            "county_id": 9
        },
        {
            "name": "埔鹽鄉",
            "id": 154,
            "county_id": 9
        },
        {
            "name": "大城鄉",
            "id": 155,
            "county_id": 9
        },
        {
            "name": "芳苑鄉",
            "id": 156,
            "county_id": 9
        },
        {
            "name": "竹塘鄉",
            "id": 157,
            "county_id": 9
        },
        {
            "name": "社頭鄉",
            "id": 158,
            "county_id": 9
        },
        {
            "name": "二水鄉",
            "id": 159,
            "county_id": 9
        },
        {
            "name": "田尾鄉",
            "id": 160,
            "county_id": 9
        },
        {
            "name": "埤頭鄉",
            "id": 161,
            "county_id": 9
        },
        {
            "name": "溪州鄉",
            "id": 162,
            "county_id": 9
        },
        {
            "name": "斗六市",
            "id": 163,
            "county_id": 10
        },
        {
            "name": "斗南鎮",
            "id": 164,
            "county_id": 10
        },
        {
            "name": "虎尾鎮",
            "id": 165,
            "county_id": 10
        },
        {
            "name": "西螺鎮",
            "id": 166,
            "county_id": 10
        },
        {
            "name": "土庫鎮",
            "id": 167,
            "county_id": 10
        },
        {
            "name": "北港鎮",
            "id": 168,
            "county_id": 10
        },
        {
            "name": "莿桐鄉",
            "id": 169,
            "county_id": 10
        },
        {
            "name": "林內鄉",
            "id": 170,
            "county_id": 10
        },
        {
            "name": "古坑鄉",
            "id": 171,
            "county_id": 10
        },
        {
            "name": "大埤鄉",
            "id": 172,
            "county_id": 10
        },
        {
            "name": "崙背鄉",
            "id": 173,
            "county_id": 10
        },
        {
            "name": "二崙鄉",
            "id": 174,
            "county_id": 10
        },
        {
            "name": "麥寮鄉",
            "id": 175,
            "county_id": 10
        },
        {
            "name": "臺西鄉",
            "id": 176,
            "county_id": 10
        },
        {
            "name": "東勢鄉",
            "id": 177,
            "county_id": 10
        },
        {
            "name": "褒忠鄉",
            "id": 178,
            "county_id": 10
        },
        {
            "name": "四湖鄉",
            "id": 179,
            "county_id": 10
        },
        {
            "name": "口湖鄉",
            "id": 180,
            "county_id": 10
        },
        {
            "name": "水林鄉",
            "id": 181,
            "county_id": 10
        },
        {
            "name": "元長鄉",
            "id": 182,
            "county_id": 10
        },
        {
            "name": "太保市",
            "id": 183,
            "county_id": 11
        },
        {
            "name": "朴子市",
            "id": 184,
            "county_id": 11
        },
        {
            "name": "布袋鎮",
            "id": 185,
            "county_id": 11
        },
        {
            "name": "大林鎮",
            "id": 186,
            "county_id": 11
        },
        {
            "name": "民雄鄉",
            "id": 187,
            "county_id": 11
        },
        {
            "name": "溪口鄉",
            "id": 188,
            "county_id": 11
        },
        {
            "name": "新港鄉",
            "id": 189,
            "county_id": 11
        },
        {
            "name": "六腳鄉",
            "id": 190,
            "county_id": 11
        },
        {
            "name": "東石鄉",
            "id": 191,
            "county_id": 11
        },
        {
            "name": "義竹鄉",
            "id": 192,
            "county_id": 11
        },
        {
            "name": "鹿草鄉",
            "id": 193,
            "county_id": 11
        },
        {
            "name": "水上鄉",
            "id": 194,
            "county_id": 11
        },
        {
            "name": "中埔鄉",
            "id": 195,
            "county_id": 11
        },
        {
            "name": "竹崎鄉",
            "id": 196,
            "county_id": 11
        },
        {
            "name": "梅山鄉",
            "id": 197,
            "county_id": 11
        },
        {
            "name": "番路鄉",
            "id": 198,
            "county_id": 11
        },
        {
            "name": "大埔鄉",
            "id": 199,
            "county_id": 11
        },
        {
            "name": "阿里山鄉",
            "id": 200,
            "county_id": 11
        },
        {
            "name": "東區",
            "id": 201,
            "county_id": 12
        },
        {
            "name": "西區",
            "id": 202,
            "county_id": 12
        },
        {
            "name": "中西區",
            "id": 203,
            "county_id": 13
        },
        {
            "name": "東區",
            "id": 204,
            "county_id": 13
        },
        {
            "name": "南區",
            "id": 205,
            "county_id": 13
        },
        {
            "name": "北區",
            "id": 206,
            "county_id": 13
        },
        {
            "name": "安平區",
            "id": 207,
            "county_id": 13
        },
        {
            "name": "安南區",
            "id": 208,
            "county_id": 13
        },
        {
            "name": "永康區",
            "id": 209,
            "county_id": 13
        },
        {
            "name": "歸仁區",
            "id": 210,
            "county_id": 13
        },
        {
            "name": "新化區",
            "id": 211,
            "county_id": 13
        },
        {
            "name": "左鎮區",
            "id": 212,
            "county_id": 13
        },
        {
            "name": "玉井區",
            "id": 213,
            "county_id": 13
        },
        {
            "name": "楠西區",
            "id": 214,
            "county_id": 13
        },
        {
            "name": "南化區",
            "id": 215,
            "county_id": 13
        },
        {
            "name": "仁德區",
            "id": 216,
            "county_id": 13
        },
        {
            "name": "關廟區",
            "id": 217,
            "county_id": 13
        },
        {
            "name": "龍崎區",
            "id": 218,
            "county_id": 13
        },
        {
            "name": "官田區",
            "id": 219,
            "county_id": 13
        },
        {
            "name": "麻豆區",
            "id": 220,
            "county_id": 13
        },
        {
            "name": "佳里區",
            "id": 221,
            "county_id": 13
        },
        {
            "name": "西港區",
            "id": 222,
            "county_id": 13
        },
        {
            "name": "七股區",
            "id": 223,
            "county_id": 13
        },
        {
            "name": "將軍區",
            "id": 224,
            "county_id": 13
        },
        {
            "name": "學甲區",
            "id": 225,
            "county_id": 13
        },
        {
            "name": "北門區",
            "id": 226,
            "county_id": 13
        },
        {
            "name": "新營區",
            "id": 227,
            "county_id": 13
        },
        {
            "name": "後壁區",
            "id": 228,
            "county_id": 13
        },
        {
            "name": "白河區",
            "id": 229,
            "county_id": 13
        },
        {
            "name": "東山區",
            "id": 230,
            "county_id": 13
        },
        {
            "name": "六甲區",
            "id": 231,
            "county_id": 13
        },
        {
            "name": "下營區",
            "id": 232,
            "county_id": 13
        },
        {
            "name": "柳營區",
            "id": 233,
            "county_id": 13
        },
        {
            "name": "鹽水區",
            "id": 234,
            "county_id": 13
        },
        {
            "name": "善化區",
            "id": 235,
            "county_id": 13
        },
        {
            "name": "大內區",
            "id": 236,
            "county_id": 13
        },
        {
            "name": "山上區",
            "id": 237,
            "county_id": 13
        },
        {
            "name": "新市區",
            "id": 238,
            "county_id": 13
        },
        {
            "name": "安定區",
            "id": 239,
            "county_id": 13
        },
        {
            "name": "楠梓區",
            "id": 240,
            "county_id": 14
        },
        {
            "name": "左營區",
            "id": 241,
            "county_id": 14
        },
        {
            "name": "鼓山區",
            "id": 242,
            "county_id": 14
        },
        {
            "name": "三民區",
            "id": 243,
            "county_id": 14
        },
        {
            "name": "鹽埕區",
            "id": 244,
            "county_id": 14
        },
        {
            "name": "前金區",
            "id": 245,
            "county_id": 14
        },
        {
            "name": "新興區",
            "id": 246,
            "county_id": 14
        },
        {
            "name": "苓雅區",
            "id": 247,
            "county_id": 14
        },
        {
            "name": "前鎮區",
            "id": 248,
            "county_id": 14
        },
        {
            "name": "小港區",
            "id": 249,
            "county_id": 14
        },
        {
            "name": "旗津區",
            "id": 250,
            "county_id": 14
        },
        {
            "name": "鳳山區",
            "id": 251,
            "county_id": 14
        },
        {
            "name": "大寮區",
            "id": 252,
            "county_id": 14
        },
        {
            "name": "鳥松區",
            "id": 253,
            "county_id": 14
        },
        {
            "name": "林園區",
            "id": 254,
            "county_id": 14
        },
        {
            "name": "仁武區",
            "id": 255,
            "county_id": 14
        },
        {
            "name": "大樹區",
            "id": 256,
            "county_id": 14
        },
        {
            "name": "大社區",
            "id": 257,
            "county_id": 14
        },
        {
            "name": "岡山區",
            "id": 258,
            "county_id": 14
        },
        {
            "name": "路竹區",
            "id": 259,
            "county_id": 14
        },
        {
            "name": "橋頭區",
            "id": 260,
            "county_id": 14
        },
        {
            "name": "梓官區",
            "id": 261,
            "county_id": 14
        },
        {
            "name": "彌陀區",
            "id": 262,
            "county_id": 14
        },
        {
            "name": "永安區",
            "id": 263,
            "county_id": 14
        },
        {
            "name": "燕巢區",
            "id": 264,
            "county_id": 14
        },
        {
            "name": "田寮區",
            "id": 265,
            "county_id": 14
        },
        {
            "name": "阿蓮區",
            "id": 266,
            "county_id": 14
        },
        {
            "name": "茄萣區",
            "id": 267,
            "county_id": 14
        },
        {
            "name": "湖內區",
            "id": 268,
            "county_id": 14
        },
        {
            "name": "旗山區",
            "id": 269,
            "county_id": 14
        },
        {
            "name": "美濃區",
            "id": 270,
            "county_id": 14
        },
        {
            "name": "內門區",
            "id": 271,
            "county_id": 14
        },
        {
            "name": "杉林區",
            "id": 272,
            "county_id": 14
        },
        {
            "name": "甲仙區",
            "id": 273,
            "county_id": 14
        },
        {
            "name": "六龜區",
            "id": 274,
            "county_id": 14
        },
        {
            "name": "茂林區",
            "id": 275,
            "county_id": 14
        },
        {
            "name": "桃源區",
            "id": 276,
            "county_id": 14
        },
        {
            "name": "那瑪夏區",
            "id": 277,
            "county_id": 14
        },
        {
            "name": "屏東市",
            "id": 278,
            "county_id": 15
        },
        {
            "name": "潮州鎮",
            "id": 279,
            "county_id": 15
        },
        {
            "name": "東港鎮",
            "id": 280,
            "county_id": 15
        },
        {
            "name": "恆春鎮",
            "id": 281,
            "county_id": 15
        },
        {
            "name": "萬丹鄉",
            "id": 282,
            "county_id": 15
        },
        {
            "name": "長治鄉",
            "id": 283,
            "county_id": 15
        },
        {
            "name": "麟洛鄉",
            "id": 284,
            "county_id": 15
        },
        {
            "name": "九如鄉",
            "id": 285,
            "county_id": 15
        },
        {
            "name": "里港鄉",
            "id": 286,
            "county_id": 15
        },
        {
            "name": "鹽埔鄉",
            "id": 287,
            "county_id": 15
        },
        {
            "name": "高樹鄉",
            "id": 288,
            "county_id": 15
        },
        {
            "name": "萬巒鄉",
            "id": 289,
            "county_id": 15
        },
        {
            "name": "內埔鄉",
            "id": 290,
            "county_id": 15
        },
        {
            "name": "竹田鄉",
            "id": 291,
            "county_id": 15
        },
        {
            "name": "新埤鄉",
            "id": 292,
            "county_id": 15
        },
        {
            "name": "枋寮鄉",
            "id": 293,
            "county_id": 15
        },
        {
            "name": "新園鄉",
            "id": 294,
            "county_id": 15
        },
        {
            "name": "崁頂鄉",
            "id": 295,
            "county_id": 15
        },
        {
            "name": "林邊鄉",
            "id": 296,
            "county_id": 15
        },
        {
            "name": "南州鄉",
            "id": 297,
            "county_id": 15
        },
        {
            "name": "佳冬鄉",
            "id": 298,
            "county_id": 15
        },
        {
            "name": "琉球鄉",
            "id": 299,
            "county_id": 15
        },
        {
            "name": "車城鄉",
            "id": 300,
            "county_id": 15
        },
        {
            "name": "滿州鄉",
            "id": 301,
            "county_id": 15
        },
        {
            "name": "枋山鄉",
            "id": 302,
            "county_id": 15
        },
        {
            "name": "霧台鄉",
            "id": 303,
            "county_id": 15
        },
        {
            "name": "瑪家鄉",
            "id": 304,
            "county_id": 15
        },
        {
            "name": "泰武鄉",
            "id": 305,
            "county_id": 15
        },
        {
            "name": "來義鄉",
            "id": 306,
            "county_id": 15
        },
        {
            "name": "春日鄉",
            "id": 307,
            "county_id": 15
        },
        {
            "name": "獅子鄉",
            "id": 308,
            "county_id": 15
        },
        {
            "name": "牡丹鄉",
            "id": 309,
            "county_id": 15
        },
        {
            "name": "三地門鄉",
            "id": 310,
            "county_id": 15
        },
        {
            "name": "宜蘭市",
            "id": 311,
            "county_id": 16
        },
        {
            "name": "羅東鎮",
            "id": 312,
            "county_id": 16
        },
        {
            "name": "蘇澳鎮",
            "id": 313,
            "county_id": 16
        },
        {
            "name": "頭城鎮",
            "id": 314,
            "county_id": 16
        },
        {
            "name": "礁溪鄉",
            "id": 315,
            "county_id": 16
        },
        {
            "name": "壯圍鄉",
            "id": 316,
            "county_id": 16
        },
        {
            "name": "員山鄉",
            "id": 317,
            "county_id": 16
        },
        {
            "name": "冬山鄉",
            "id": 318,
            "county_id": 16
        },
        {
            "name": "五結鄉",
            "id": 319,
            "county_id": 16
        },
        {
            "name": "三星鄉",
            "id": 320,
            "county_id": 16
        },
        {
            "name": "大同鄉",
            "id": 321,
            "county_id": 16
        },
        {
            "name": "南澳鄉",
            "id": 322,
            "county_id": 16
        },
        {
            "name": "花蓮市",
            "id": 323,
            "county_id": 17
        },
        {
            "name": "鳳林鎮",
            "id": 324,
            "county_id": 17
        },
        {
            "name": "玉里鎮",
            "id": 325,
            "county_id": 17
        },
        {
            "name": "新城鄉",
            "id": 326,
            "county_id": 17
        },
        {
            "name": "吉安鄉",
            "id": 327,
            "county_id": 17
        },
        {
            "name": "壽豐鄉",
            "id": 328,
            "county_id": 17
        },
        {
            "name": "秀林鄉",
            "id": 329,
            "county_id": 17
        },
        {
            "name": "光復鄉",
            "id": 330,
            "county_id": 17
        },
        {
            "name": "豐濱鄉",
            "id": 331,
            "county_id": 17
        },
        {
            "name": "瑞穗鄉",
            "id": 332,
            "county_id": 17
        },
        {
            "name": "萬榮鄉",
            "id": 333,
            "county_id": 17
        },
        {
            "name": "富里鄉",
            "id": 334,
            "county_id": 17
        },
        {
            "name": "卓溪鄉",
            "id": 335,
            "county_id": 17
        },
        {
            "name": "臺東市",
            "id": 336,
            "county_id": 18
        },
        {
            "name": "成功鎮",
            "id": 337,
            "county_id": 18
        },
        {
            "name": "關山鎮",
            "id": 338,
            "county_id": 18
        },
        {
            "name": "長濱鄉",
            "id": 339,
            "county_id": 18
        },
        {
            "name": "海端鄉",
            "id": 340,
            "county_id": 18
        },
        {
            "name": "池上鄉",
            "id": 341,
            "county_id": 18
        },
        {
            "name": "東河鄉",
            "id": 342,
            "county_id": 18
        },
        {
            "name": "鹿野鄉",
            "id": 343,
            "county_id": 18
        },
        {
            "name": "延平鄉",
            "id": 344,
            "county_id": 18
        },
        {
            "name": "卑南鄉",
            "id": 345,
            "county_id": 18
        },
        {
            "name": "金峰鄉",
            "id": 346,
            "county_id": 18
        },
        {
            "name": "大武鄉",
            "id": 347,
            "county_id": 18
        },
        {
            "name": "達仁鄉",
            "id": 348,
            "county_id": 18
        },
        {
            "name": "綠島鄉",
            "id": 349,
            "county_id": 18
        },
        {
            "name": "蘭嶼鄉",
            "id": 350,
            "county_id": 18
        },
        {
            "name": "太麻里鄉",
            "id": 351,
            "county_id": 18
        },
        {
            "name": "馬公市",
            "id": 352,
            "county_id": 19
        },
        {
            "name": "湖西鄉",
            "id": 353,
            "county_id": 19
        },
        {
            "name": "白沙鄉",
            "id": 354,
            "county_id": 19
        },
        {
            "name": "西嶼鄉",
            "id": 355,
            "county_id": 19
        },
        {
            "name": "望安鄉",
            "id": 356,
            "county_id": 19
        },
        {
            "name": "七美鄉",
            "id": 357,
            "county_id": 19
        },
        {
            "name": "金城鎮",
            "id": 358,
            "county_id": 20
        },
        {
            "name": "金湖鎮",
            "id": 359,
            "county_id": 20
        },
        {
            "name": "金沙鎮",
            "id": 360,
            "county_id": 20
        },
        {
            "name": "金寧鄉",
            "id": 361,
            "county_id": 20
        },
        {
            "name": "烈嶼鄉",
            "id": 362,
            "county_id": 20
        },
        {
            "name": "烏坵鄉",
            "id": 363,
            "county_id": 20
        },
        {
            "name": "南竿鄉",
            "id": 364,
            "county_id": 21
        },
        {
            "name": "北竿鄉",
            "id": 365,
            "county_id": 21
        },
        {
            "name": "莒光鄉",
            "id": 366,
            "county_id": 21
        },
        {
            "name": "東引鄉",
            "id": 367,
            "county_id": 21
        }
    ]
