# Hint:  use Google to find python function

import datetime
def date_function (start, finish, date_fmt):
    start = datetime.datetime.strptime(start,date_fmt)
    finish = datetime.datetime.strptime(finish,date_fmt)
    return (finish-start).days

date_start = '01-02-2013'
date_stop = '07-28-2015'
print date_function(date_start, date_stop, '%m-%d-%Y')

date_start = '12312013'
date_stop = '05282015'
print date_function(date_start, date_stop, '%m%d%Y')

date_start = '15-Jan-1994'
date_stop = '14-Jul-2015'
print date_function(date_start, date_stop, '%d-%b-%Y') #strftime formatting
