from const import column_list
from datetime import datetime


def parse_rows_from_html(soup, date):
    rows = []
    tbody = soup.find_all('table', {"class": "print_table"})[0].tbody
    for tr in tbody.find_all('tr'):
        td_list = tr.find_all('td')
        if len(td_list) != 9:
            continue
        row = {}
        for i, td in enumerate(td_list):
            row[column_list[i]] = td.get_text()
        row['date'] = datetime(
            year=date.year,
            month=date.month,
            day=date.day
        )
        rows.append(row)
    return rows


def parse_max_page_from_html(soup):
    pagination = soup.find_all("div", {"class": "paginate"})[0].find_all()
    return len(pagination)
