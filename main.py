from docx import Document  # pip install python-docx 
from datetime import datetime
from dateutil.rrule import rrule, WEEKLY, MO, TH

# С какого по какое число нужны даты
start_date = datetime(2021, 9, 1)
end_date = datetime(2022, 6, 1)

# Известное содержимое ячеек
counter = 1
time = "16.00-16.45 17.00-17.45"
form = "комбинированная"
duration = "2"
theme = ""
location = "МАУ ДО ДДТ г. Можайска; Ул. Мира, д. 6а, каб. 10"
control = "Устный опрос, беседа, практическая проверка"

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
9*8
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


for date in rrule(WEEKLY, byweekday=(MO, TH), dtstart=start_date, until=end_date):
    
    # Получаем кортеж из 9 элементов
    line = (
        counter,
        translation_dict[date.strftime('%b')],
        date.strftime('%d'),
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