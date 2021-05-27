from datetime import datetime
from dateutil.rrule import rrule, WEEKLY, MO, TH

start_date = datetime(2021, 9, 1)
for date in rrule(WEEKLY, byweekday=TH, count=30, dtstart=start_date):
    print(date)

