
# -----------------------------------------------------------
# sqlite connection and functions
# (C) 2021 Vasin Vsevolod, Novokuznetsk, Russia
# email vsevolod.vasin.gm@gmail.com
# -----------------------------------------------------------


import sqlite3

class SQLighter:

    def __init__(self, database):
        """Подключаемся к БД и сохраняем курсор соединения"""
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()
        self.connection.execute("PRAGMA busy_timeout = 30000")


    def add_course(self, name, description, url,time, cost, place):
        """Добавляем новый курс"""
        with self.connection:
            return self.cursor.execute("INSERT INTO `Courses` (`Course_name`, `Course_description`, `Course_URL`, "
                                       "`Course_education_time`,`Course_cost` , `Course_place`) VALUES(?,?,?,?,?,?)",
                                       (name,description, url, time, cost, place))

    def add_competense(self, name, description):
        """Добавляем новую компетенцию"""
        with self.connection:
            return self.cursor.execute("INSERT INTO `Competencies` (`Competence_name`, `Competence_description`) "
                                       "VALUES(?,?)",
                                       (name,description))


    # Доделать

    def add_competensebycourse(self, idcomp, idcourse):
        """Добавляем новую компетенцию"""
        with self.connection:
            print("INSERT INTO `Competences_by_courses` (`Competence_id`, `Course_id`) "
                                       "VALUES(?,?)",
                                       (idcomp, idcourse))
            return self.cursor.execute("INSERT INTO `Competences_by_courses` (`Competence_id`, `Course_id`) "
                                       "VALUES(?,?)",
                                       (idcomp, idcourse))



    def clearcours(self):
        """Очистка БД"""
        with self.connection:
            return self.cursor.execute("DELETE FROM `Courses`")

    def clearcomp(self):
        """Очистка БД"""
        with self.connection:
            return self.cursor.execute("DELETE FROM `Competencies`")



    def lastcourseid(self):
        """Последний добавленный курс"""
        with self.connection:
            self.cursor.execute("SELECT `Course_id` FROM `Courses` ORDER BY `Course_id` DESC LIMIT 1")
            return self.cursor.fetchall()
            
            
    def lastcompetenceid(self):
        """Последняя компетенция"""
        with self.connection:
            self.cursor.execute("SELECT `Competence_id` FROM `Competencies` ORDER BY `Competence_id` DESC LIMIT 1")
            return self.cursor.fetchall()


    def close(self):
        """Закрываем соединение с БД"""
        self.connection.close()
