from bs4 import BeautifulSoup as BS
from urllib import request
from datetime import datetime
from datetime import timedelta
import yaml


class Streak:
    def __init__(self):
        self.user_id = None
        self.page = None
        self.last_solved_time = None
        self.standard_time = None
        self.is_solved = None

    def get_id(self):
        with open('./user.yml') as yml:
            config = yaml.load(yml, Loader=yaml.BaseLoader)
            self.user_id = config['user-id']

    def html_parse(self):
        url = f'https://www.acmicpc.net/status?user_id={self.user_id}&result_id=4'
        headers = {'User-Agent': 'Chrome/66.0.3359.181'}
        req = request.Request(url, headers=headers)
        html = request.urlopen(req)
        self.page = BS(html, 'lxml')

    def get_last_solved_time(self):
        elem = self.page.select_one('#status-table > tbody > tr:nth-child(1) > td:last-child > a')
        last_solved_timestamp = elem.attrs['data-timestamp']
        self.last_solved_time = datetime.fromtimestamp(int(last_solved_timestamp))

    def is_solved_today(self):
        now_time = datetime.now() + timedelta(hours=9)
        standard_time_str = str(now_time).split(' ')[0] + ' 06:00:00'
        self.standard_time = datetime.strptime(standard_time_str, "%Y-%m-%d %H:%M:%S")

        if self.standard_time <= self.last_solved_time:
            self.is_solved = True
        else:
            self.is_solved = False
