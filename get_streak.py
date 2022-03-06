from bs4 import BeautifulSoup as BS
from urllib import request
from datetime import datetime
from datetime import timedelta
import yaml


user_id = ''
page = ''
last_solved_time = datetime.now()
stadard_time = datetime.now()


def get_id():
    global user_id

    with open('./user.yml') as yml:
        config = yaml.load(yml, Loader=yaml.BaseLoader)
        user_id = config['user-id']


def html_parse():
    global page

    url = f'https://www.acmicpc.net/status?user_id={user_id}&result_id=4'
    headers = {'User-Agent': 'Chrome/66.0.3359.181'}
    req = request.Request(url, headers=headers)
    html = request.urlopen(req)
    page = BS(html, 'lxml')


def get_last_solved_time():
    global last_solved_time

    elem = page.select_one('#status-table > tbody > tr:nth-child(1) > td:last-child > a')
    last_solved_timestamp = elem.attrs['data-timestamp']
    last_solved_time = datetime.fromtimestamp(int(last_solved_timestamp))


def is_solved_today():
    global stadard_time

    now_time = datetime.now() + timedelta(hours=9)
    standard_time_str = str(now_time).split(' ')[0] + ' 06:00:00'
    standard_time = datetime.strptime(standard_time_str, "%Y-%m-%d %H:%M:%S")

    if standard_time <= last_solved_time:
        return True
    else:
        return False


def main():
    get_id()
    html_parse()
    get_last_solved_time()
    is_solved = is_solved_today()

    return is_solved, last_solved_time, stadard_time
