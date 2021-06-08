from datetime import datetime
from calendar import monthrange
 
def last_day_of_month(date_value):
    return date_value.replace(day = monthrange(date_value.year, date_value.month)[1])
 
given_date = datetime.today().date()
print("\nGiven date:", given_date, " --> Last day of month:", last_day_of_month(given_date))
 
given_date = datetime(year=2008, month=2, day=1).date()
print("\nGiven date:", given_date, " --> Last day of month:", last_day_of_month(given_date))
 
given_date = datetime(year=2009, month=2, day=15).date()
print("\nGiven date:", given_date, " --> Last day of month:", last_day_of_month(given_date), "\n")