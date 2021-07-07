# -----------------------------------------------------------
# main parser file
# (C) 2021 Vasin Vsevolod, Novokuznetsk, Russia
# email vsevolod.vasin.gm@gmail.com
# -----------------------------------------------------------


import sys
from design import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from parser1 import parser1 as gb
from parser2 import parser2 as sb
from parser3 import parser3 as yand
import sys
import datetime
import json
import subprocess

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.Do_parse.clicked.connect(self.parsething)
        self.save.clicked.connect(self.save_config)
        self.Start_parse.clicked.connect(self.start_parse)
        self.Exit.clicked.connect(self.exit_program)

    def exit_program(self):
        self.close()

    def parsething(self):

        with open('log.ini', 'a', encoding='utf-8') as log:
            print(f"Парсинг сайтов начался - {datetime.datetime.now()}", file=log)
            print(f"Парсинг сайтов начался - {datetime.datetime.now()}")
            print(f"Парсинг сайта GeekBrains прошёл успешно - {datetime.datetime.now()}")
            if self.GeekBrain.isChecked():
                try:
                    gb()
                    print(f"Парсинг сайта GeekBrains прошёл успешно - {datetime.datetime.now()}", file=log)
                    print(f"Парсинг сайта GeekBrains прошёл успешно - {datetime.datetime.now()}")
                except:
                    print(f"Во время парсинга сайта GeekBrains произошла ошибка - {datetime.datetime.now()}", file=log)
                    print(f"Во время парсинга сайта GeekBrains произошла ошибка - {datetime.datetime.now()}")
            if self.SkillBox.isChecked():
                try:
                    sb()
                    print(f"Парсинг сайта SkillBox прошёл успешно - {datetime.datetime.now()}", file=log)
                except:
                    print(f"Во время парсинга сайта SkillBox произошла ошибка - {datetime.datetime.now()}", file=log)
                    print(f"Во время парсинга сайта SkillBox произошла ошибка - {datetime.datetime.now()}")
            if self.Yandex.isChecked():
                try:
                    yand()
                    print(f"Парсинг сайта YandexPracticum прошёл успешно - {datetime.datetime.now()}", file=log)
                    print(f"Парсинг сайта YandexPracticum прошёл успешно - {datetime.datetime.now()}")
                except:
                    print(f"Во время парсинга сайта YandexPracticum произошла ошибка - {datetime.datetime.now()}", file=log)
                    print(f"Во время парсинга сайта YandexPracticum произошла ошибка - {datetime.datetime.now()}")
            self.statusbar.showMessage("Парсинг завершился")
            print(f"Парсинг сайтов прошёл успешно - {datetime.datetime.now()}", file=log)
            print(f"Парсинг сайтов прошёл успешно - {datetime.datetime.now()}")

    def save_config(self):
        config = {
          "Time": {"parsing_period": self.Perdioct.value(), "parsing_time":  str(self.timeEdit.time().toPyTime())},
          "GeekBrains": {"parsing": self.GeekBrain.isChecked()},
          "SkillBox": {"parsing": self.SkillBox.isChecked()},
          "YandexPracticum": {"parsing": self.Yandex.isChecked()}
        }
        with open('settings.json', "w") as settings:
            json.dump(config, settings)
            self.statusbar.showMessage("Конфигурация сохранена")

    def start_parse(self):
        self.save_config()
        subprocess.Popen(["python", "schedule_parsing.py"])
        self.Start_parse.setEnabled(False)
        self.save.setEnabled(False)
        self.statusbar.showMessage("Парсер запущен")



def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
