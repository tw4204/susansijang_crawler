from bs4 import BeautifulSoup
import requests
from url import susansijang_url 
from parser import (
    parse_rows_from_html,
    parse_max_page_from_html
)
import time


r = requests.post(susansijang_url, data={
    'pageIndex': 2,
    'pageUnit': 10,
    'pageSize': 20,
    'kdfshNm': '가자미',
    'kdfshCode': '가자미',
    'searchStartDe': '2021.07.12',
    'searchEndDe': '2021.07.19'
})

soup = BeautifulSoup(r.text, 'html.parser')
print(parse_rows_from_html(soup))
