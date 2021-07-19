def parse_rows_from_html(soup):
    rows = []
    tbody = soup.find_all('table', {"class": "print_table"})[0].tbody
    for tr in tbody.find_all('tr'):
        td_list = tr.find_all('td')
        if len(td_list) != 9:
            continue
        row = []
        for td in td_list:
            row.append(td.get_text())
        rows.append(row)
    return rows

def parse_max_page_from_html(soup):
    pagination = soup.find_all("div", {"class": "paginate"})[0].find_all()
    return len(pagination)
