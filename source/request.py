from bs4 import BeautifulSoup
import requests
from const import target_url


def get_soup_from_page(page, fish_name, date_string):
    r = requests.post(target_url, data={
        'pageIndex': page,
        'pageUnit': 10,
        'pageSize': 10,
        'kdfshNm': fish_name,
        'kdfshCode': fish_name,
        'searchStartDe': date_string,
        'searchEndDe': date_string
    })
    return BeautifulSoup(r.text, 'html.parser')
