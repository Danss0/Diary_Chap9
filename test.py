# Name
# first_name = 'Mochamad Rizky'
# last_name = 'Septian R'
# full_name = f'{first_name} {last_name}'
# print(full_name)

from datetime import datetime

today = datetime.now()
date_time = today.strftime('%Y-%m-%d %H:%M:%S')

print(date_time)