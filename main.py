from datetime import datetime
from dateutil.rrule import rrule, WEEKLY, MO, TH

start_date = datetime(2021, 9, 1)
end_date = datetime(2022, 6, 1)

translation_dict = {
    "Sep" : "Сентябрь",
    "Oct" : "Октябрь",
    "Nov" : "Ноябрь",
    "Dec" : "Декабрь",
    "Jan" : "Январь",
    "Feb" : "Февраль",
    "Mar" : "Март",
    "Oct" : "Апрель",
    "Oct" : "Май",
    "Jun" : "Июнь",
    "Jul" : "Июль",
    "Aug" : "Август",
    }

counter = 1
for date in rrule(WEEKLY, byweekday=(MO, TH), dtstart=start_date, until=end_date):
    tup = (counter, translation_dict[date.strftime('%b')], date.strftime('%d'))
    counter += 1
    print(tup)

"""
на выходе таблица 9 колонок
№ п/п, месяц, число, время проведения, форма занятия, кол-во часов, тема занятия, место проведения, форма контроля
"""