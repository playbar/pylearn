# datetime_datetime_strptime.py

# strptime/strftime format codes
# Symbol	Meaning	                        Example
# %a	    Abbreviated weekday name	    'Wed'
# %A	    Full weekday name	            'Wednesday'
# %w	    Weekday number – 0 (Sunday) through 6 (Saturday)	'3'
# %d	    Day of the month (zero padded)	'13'
# %b	    Abbreviated month name	        'Jan'
# %B	    Full month name	                'January'
# %m	    Month of the year	            '01'
# %y	    Year without century	        '16'
# %Y	    Year with century	            '2016'
# %H	    Hour from 24-hour clock	        '17'
# %I	    Hour from 12-hour clock	        '05'
# %p	    AM/PM	                        'PM'
# %M	    Minutes	                        '00'
# %S	    Seconds	                        '00'
# %f	    Microseconds	                '000000'
# %z	    UTC offset for time zone-aware objects	'-0500'
# %Z	    Time Zone name	                'EST'
# %j	    Day of the year	                '013'
# %W	    Week of the year	            '02'
# %c	    Date and time representation for the current locale	'Wed Jan 13 17:00:00 2016'
# %x	    Date representation for the current locale	'01/13/16'
# %X	    Time representation for the current locale	'17:00:00'
# %%	    A literal % character	        '%'


import datetime

format = "%a %b %d %H:%M:%S %Y"

today = datetime.datetime.today()
print('ISO     :', today)

s = today.strftime(format)
print('strftime:', s)

d = datetime.datetime.strptime(s, format)
print('strptime:', d.strftime(format))

today = datetime.datetime.today()
print('ISO     :', today)
print('format(): {:%a %b %d %H:%M:%S %Y}'.format(today))

