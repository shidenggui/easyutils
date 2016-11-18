import datetime
from datetime import timedelta
from functools import lru_cache

import requests

import time


@lru_cache()
def is_holiday(day):
    """
    判断是否节假日, api 来自百度 apistore: http://apistore.baidu.com/apiworks/servicedetail/1116.html
    :param day: 日期， 格式为 '20160404'
    :return: bool
    """
    api = 'http://tool.bitefu.net/jiari/'
    params = {'d': day, 'apiserviceid': 1116}
    rep = requests.get(api, params)
    res = rep.text
    return True if res != "0" else False


def is_holiday_today():
    """
    判断今天是否时节假日
    :return: bool
    """
    today = datetime.date.today().strftime('%Y%m%d')
    return is_holiday(today)


def is_tradetime_now():
    """
    判断目前是不是交易时间, 并没有对节假日做处理
    :return: bool
    """
    now_time = time.localtime()
    now = (now_time.tm_hour, now_time.tm_min, now_time.tm_sec)
    if (9, 15, 0) <= now <= (11, 30, 0) or (13, 0, 0) <= now <= (15, 0, 0):
        return True
    return False


def calc_next_trade_time_delta_seconds():
    now_time = datetime.datetime.now()
    now = (now_time.hour, now_time.minute, now_time.second)
    if now < (9, 15, 0):
        next_trade_start = now_time.replace(hour=9, minute=15, second=0, microsecond=0)
    elif (12, 0, 0) < now < (13, 0, 0):
        next_trade_start = now_time.replace(hour=13, minute=0, second=0, microsecond=0)
    elif now > (15, 0, 0):
        distance_next_work_day = 1
        while True:
            target_day = now_time + timedelta(days=distance_next_work_day)
            if is_holiday(target_day.strftime('%Y%m%d')):
                distance_next_work_day += 1
            else:
                break

        day_delta = timedelta(days=distance_next_work_day)
        next_trade_start = (now_time + day_delta).replace(hour=9, minute=15,
                                                          second=0, microsecond=0)
    else:
        return 0
    time_delta = next_trade_start - now_time
    return time_delta.total_seconds()
