from const import fish_list
from parser import (
    parse_rows_from_html,
    parse_max_page_from_html
)
from request import get_soup_from_page
from database import db
from config import (
    start_date,
    end_date
)
import datetime
from logger import get_logger
import os

base_path = os.path.dirname(os.path.abspath(__file__))
log_path = os.path.join(base_path, 'logs/crawler_log.txt')
LOG = get_logger(__name__, log_path)


def crawl():
    for fish_name in fish_list:
        date = start_date
        while date <= end_date:
            date_string = date.strftime('%Y.%m.%d')
            page = 1
            soup = get_soup_from_page(page, fish_name, date_string)
            max_page = parse_max_page_from_html(soup)
            while True:
                rows = parse_rows_from_html(soup, date)
                if len(rows) > 0:
                    db[fish_name].insert_many(rows)
                LOG.info(
                    f'name: {fish_name},'
                    f'date: {date_string},'
                    f'page: {page} / {max_page},'
                    f'#rows: {len(rows)}'
                )
                if page >= max_page:
                    break
                soup = get_soup_from_page(page + 1, fish_name, date_string)
                page += 1
            date += datetime.timedelta(days=1)


if __name__ == '__main__':
    crawl()
