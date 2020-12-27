# import pandas as pd
from bs4 import BeautifulSoup
import requests
import time

"""
1	SIGUN_NM	시군명
2	SIGUN_CD	시군코드
3	BIZPLC_NM	사업장명
4	TELNO	전화번호
5	REFINE_ZIP_CD	소재지우편번호
6	REFINE_LOTNO_ADDR	소재지지번주소
7	REFINE_ROADNM_ADDR	소재지도로명주소
8	REFINE_WGS84_LAT	WGS84위도
9	REFINE_WGS84_LOGT	WGS84경도
"""
page_index = 1
page_request = 50

url = 'https://openapi.gg.go.kr/FoodbankStu?KEY=a8861b6a851d4dc4b02d4efe1e932772&pIndex{}&pSize={}'.format(page_index, page_request)

res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')
road_adresses = soup.find_all("refine_roadnm_addr")
bizplc_nms = soup.find_all("bizplc_nms") 

for road_adress, bizplc_nm in zip(road_adresses, bizplc_nms):
    print("-" * 50)
    print(bizplc_nm.text)
    print(road_adress.text)
    print("-" * 50)
