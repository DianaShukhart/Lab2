#!/usr/bin/env python3
# coding=utf-8

import sys

from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


# Основной класс программы
class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('form.ui', self)  # Загрузка формы из файла

        # Задание заголовка окна
        self.setWindowTitle('Создание простейшей визуальной '
                            'программы на Python')

        # Задание иконки окна
        self.setWindowIcon(QtGui.QIcon('logo.png'))

        # Задание картинки с заданием с масштабированием в компоненте
        self.label_img.setPixmap(QPixmap('1.png'))
        self.label_img.setScaledContents(True)

        # Привязываем к кнопкам наши процедуры-обработчики
        self.b_solve.clicked.connect(self.solve)
        self.b_clear.clicked.connect(self.clear)
        self.b_exit.clicked.connect(self.close)

    # Процедура решения примера
    def solve(self):
        try:
            pass
            a = float(self.lineEdit_x.text())
            b = float(self.lineEdit_b.text())
            x = float(self.lineEdit_x.text())
            if x <= 4:
                answer = (a ** 2 / x ** 2) + 6 * x
            else:
                answer = (b ** 2) * ((4 + x) ** 2)
            self.label_answer.setText('Ответ: ' + str(format(answer, '.2f')))
        except:
            self.label_answer.setText('Ошибка!')

    # Процедура очистки данных
    def clear(self):
        self.lineEdit_a.setText('')
        self.lineEdit_b.setText('')
        self.lineEdit_x.setText('')
        self.label_answer.setText('Ответ: ')


# Основная часть программы
app = QApplication(sys.argv)
window = Main()  # базовый класс окна
window.show()  # отобразить окно на экране
sys.exit(app.exec_())  # запуск основного цикла приложения
