# -----------------------------------------------------------
# scheduled parser
# (C) 2021 Vasin Vsevolod, Novokuznetsk, Russia
# email vsevolod.vasin.gm@gmail.com
# -----------------------------------------------------------



from sqlighter import SQLighter
from parser1 import parser1 as gb
from parser2 import parser2 as sb
from parser3 import parser3 as yand
import configparser
import datetime
import schedule
import json

with open('settings.json') as settings:
    config = json.load(settings)
sites = {'GeekBrains': gb, 'SkillBox': sb, 'YandexPracticum': yand}

def job():
    db = SQLighter('db.db')
    db.clearcomp()
    db.clearcours()
    with open('log.ini', 'a', encoding='utf-8') as log:
        print(f"Парсинг сайтов начался - {datetime.datetime.now()}", file=log)
        for site in sites:
            if config[site]['parsing']:
                try:
                    sites[site]()
                    print(f"Парсинг сайта {site} прошёл успешно - {datetime.datetime.now()}", file=log)
                except:
                    print(f"Ошибка! - {datetime.datetime.now()}")
        print(f"Парсинг сайтов прошёл успешно - {datetime.datetime.now()}", file=log)

parsing_period = int(config["Time"]["parsing_period"])
parsing_time = config["Time"]["parsing_time"]

print(parsing_time)
schedule.every(parsing_period).days.at(str(parsing_time)).do(job)

while True:
    schedule.run_pending()
