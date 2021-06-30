
import urllib3
from bs4 import BeautifulSoup
from sqlighter import SQLighter
import unicodedata
class parser3:
    def __init__(self):
        db = SQLighter('db.db')
        http = urllib3.PoolManager()
        page = 'https://practicum.yandex.ru/'
        response = http.request('GET', page)

        soup = BeautifulSoup(response.data, 'html.parser')


        descriptions = [a.get_text() for a in soup.body.find_all('div', attrs={'class' : 'skills-section__card-description'})]
        timeandcount = [a.get_text() for a in soup.body.find_all('span', attrs={'class' : 'skills-section__card-additional-info'})]
        names = [a.get_text() for a in soup.body.find_all('u')]




        print(descriptions)
        print(timeandcount)
        print(names)


        db.clearcomp()
        db.clearcours()

        number = 1
        while (number < len(names)):




            decoded_correct = timeandcount[number].encode().decode('utf-8', 'replace')
            print(decoded_correct)
            splitedtimeandcount = decoded_correct.split('—')
            try:
                time = splitedtimeandcount[0]
                price = splitedtimeandcount[1]
            except Exception:
                time = splitedtimeandcount[0]
                price = ''
            db.add_course(names[number], descriptions[number], 'https://practicum.yandex.ru/', time, price, 'Дистанционно')
            

            number+=1



