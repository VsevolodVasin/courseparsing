import urllib3
from bs4 import BeautifulSoup
from sqlighter import SQLighter
class parser2:
    def __init__(self):
        db = SQLighter('db.db')
        http = urllib3.PoolManager()
        page = 'https://skillbox.ru/courses'
        response = http.request('GET', page)

        soup = BeautifulSoup(response.data, 'html.parser')

        x = soup.body.find('div', attrs={'class' : 'card-list courses-block__list card-list--catalog'}).text
        x = x[1]
        proffesionslinks  = []

        for a in soup.find_all('a', href=True):
            print ("Found the URL:", a['href'])
            if ('course/' in a['href']):
                proffesionslinks.append(a['href'])


        print(proffesionslinks)

        for a in proffesionslinks:
            http = urllib3.PoolManager()
            page = a
            print(page)
            response = http.request('GET', page)

            soup = BeautifulSoup(response.data, 'html.parser')
            url = page
            # Переменные под запись
            try:
                name = soup.body.find('h1').text
            except Exception:
                continue

            try:
                description = soup.body.find('p', attrs={'class': 'start-screen__desc'}).text

            except Exception:
                 description = '?'



            try:
                price = soup.body.find('span', attrs={'class': 'h h--3'}).text
            except Exception:
                price = 'Цена не указана'

            try:
                time = soup.body.find('span', attrs={'class': 'start-screen__feature-text'}).text
            except Exception:
                time = 'Длительность не указана'







            place = 'Дистанционно'



            price = price.replace(" ", "")


            try:
                price = int(price)
            except:
                price = price

            try:
                competense = soup.body.find('div', attrs={'class': 'tech-list'}).text
                competense = competense.strip()

                db.add_competense(competense, compdescription)
                print(db.add_competensebycourse(competense))

            except Exception:
                competense = 'Компетенции не указаны'

            compdescription = ''



            print(price)
            print(type(price))

            db.add_course(name,description, url, time, price, place)
