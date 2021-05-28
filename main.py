import sys
from PyQt5.QtWidgets import QFileDialog  # pip install pyside2
from PyQt5 import QtTest  # pip install pyside2
from interface import *

from docx import Document  # pip install python-docx 
from datetime import datetime
from dateutil.rrule import rrule, WEEKLY
import holidays_parser

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()


def main():
    # С какого по какое число нужны даты
    start_date = ui.start_date.date().toPyDate()
    end_date = ui.end_date.date().toPyDate()
    start_year = start_date.strftime("%Y")
    end_year = end_date.strftime("%Y")

    # Парсинг сайта с данными праздников
    urls = [
    "http://www.consultant.ru/law/ref/calendar/proizvodstvennye/" + start_year,
    "http://www.consultant.ru/law/ref/calendar/proizvodstvennye/" + end_year
    ]
    # TODO: сообщение в виджет, что сайт вернул 200

    page_content = holidays_parser.get_site_content(urls)
    holidays_list = holidays_parser.make_holidays_list(page_content)
    # TODO: сообщения в видежет, что праздники получены
    
    days = []

    # TODO: списковое включение
    if ui.mon.isChecked():
        days.append(0)
    if ui.tue.isChecked():
        days.append(1)
    if ui.wed.isChecked():
        days.append(2)
    if ui.thu.isChecked():
        days.append(3)
    if ui.fri.isChecked():
        days.append(4)
    if ui.sun.isChecked():
        days.append(5)
    if ui.sat.isChecked():
        days.append(6)

    # Перевод месяцев на русский язык
    translation_dict = {
        "Sep" : "Сентябрь",
        "Oct" : "Октябрь",
        "Nov" : "Ноябрь",
        "Dec" : "Декабрь",
        "Jan" : "Январь",
        "Feb" : "Февраль",
        "Mar" : "Март",
        "Apr" : "Апрель",
        "May" : "Май",
        "Jun" : "Июнь",
        "Jul" : "Июль",
        "Aug" : "Август",
        }

    # Создаем стилизованную таблицу 1 строка, 9 колонок
    document = Document()
    table = document.add_table(1, 9)
    table.style = 'Table Grid'

    # Заполняем заголовки таблицы
    # TODO: Брать загловки из списка
    heading_cells = table.rows[0].cells
    heading_cells[0].text = '№ п/п'
    heading_cells[1].text = 'месяц'
    heading_cells[2].text = 'число'
    heading_cells[3].text = 'время проведения'
    heading_cells[4].text = 'форма занятия'
    heading_cells[5].text = 'кол-во часов'
    heading_cells[6].text = 'тема занятия'
    heading_cells[7].text = 'место проведения'
    heading_cells[8].text = 'форма контроля'

    # byweekday=(0, 3) понедельники и четверги
    counter = 1
    for date in rrule(WEEKLY, byweekday=(days), dtstart=start_date, until=end_date):
        
        # Получаем кортеж из 9 элементов
        month = translation_dict[date.strftime('%b')]
        day = date.strftime('%d')
        month_and_day = month + " " + day

        if month_and_day in holidays_list:
            time = ""
            form = ""
            duration = ""
            theme = "Праздничный день"
            location = ""
            control = ""
        else:
            time = "16.00-16.45 17.00-17.45"
            form = "комбинированная"
            duration = "2"
            theme = ""
            location = "МАУ ДО ДДТ г. Можайска; Ул. Мира, д. 6а, каб. 10"
            control = "Устный опрос, беседа, практическая проверка"

        line = (
            counter,
            month,
            day,
            time,
            form,
            duration,
            theme,
            location,
            control
        )

        # Записываем ячейки в ряд таблицы
        i = 0
        cells = table.add_row().cells
        for item in line:
            cells[i].text = str(line[i])
            i += 1

        counter += 1

    document.save('output.docx')

ui.make_file.clicked.connect(main)

sys.exit(app.exec_())
