# -----------------------------------------------------------
# geekbrains parser
# (C) 2021 Vasin Vsevolod, Novokuznetsk, Russia
# email vsevolod.vasin.gm@gmail.com
# -----------------------------------------------------------


import urllib3
from bs4 import BeautifulSoup
from sqlighter import SQLighter


class parser1:
    def __init__(self):

        db = SQLighter('db.db')
        http = urllib3.PoolManager()
        page = 'https://gb.ru/courses.html'
        response = http.request('GET', page)

        soup = BeautifulSoup(response.data, 'html.parser')

        x = soup.body.find('div', attrs={'class' : 'gu-profession-cards-grid__content'}).text

        proffesionslinks  = []

        for a in soup.find_all('a', href=True):
            print ("Found the URL:", a['href'])
            if ('geek_university' in a['href']):
                proffesionslinks.append(a['href'])


        print(proffesionslinks)




        for a in proffesionslinks:
            http = urllib3.PoolManager()
            page = 'https://gb.ru' + a
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
                description = soup.body.find('p').text
                
            except Exception:
                try:
                    description = soup.body.find('div', attrs={'class': 'par-20 top'}).text
                except Exception:
                    description = '?'


          
            try:
                price = soup.body.find('span', attrs={'gb-dates': 'price'}).text
            except Exception:
                price = 'Цена не указана'



            if('оплатите' in description):
                try:
                    description = soup.body.find('p', attrs={'class': 'small-p hero-p'}).text
                except Exception:
                    description = "?"



            if('Начало занятий' in description):
                description = soup.body.find('div', attrs={'class': 'par-20 top'}).text

            time = 'Длительность не указана'
            try:
                time  = soup.body.find('div', attrs={'class': 'par-20 white'}).text
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
                courseid = db.lastcourseid()
                compid = db.lastcompetenceid()
                courseid = courseid[0]
                compid = compid[0]
                courseid = courseid[0]
                compid = compid[0]
                print(type(courseid))
                print(compid)
                db.add_competensebycourse(compid,courseid)

            except Exception:
                competense = 'Компетенции не указаны'

            compdescription = ''



            print(price)
            print(type(price))
            
            db.add_course(name,description, url, time, price, place)
            
