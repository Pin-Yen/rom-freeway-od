import requests
import os

# date, in YYYYMMDD format
DATE = '20190415'
print(DATE)

# Make data directory if not exists
if not os.path.exists('data'):
    os.makedirs('data')
if not os.path.exists('data/' + DATE):
    os.makedirs('data/' + DATE)

url_template = (
    'http://tisvcloud.freeway.gov.tw/history/TDCS/M08A/{date}/{hour:02}'
     + '/TDCS_M08A_{date}_{hour:02}{min:02}00.csv')

filename_template = 'data/{date}/{hour:02}/TDCS_M08A_{date}_{hour:02}{min:02}00.csv'

for hour in range(6, 24):
    for minute in range(0, 60, 5):
        r = requests.get(url_template.format(date=DATE, hour=hour, min=minute))

        if not os.path.exists('data/{date}/{hour:02}'.format(date=DATE, hour=hour)):
            os.makedirs('data/{date}/{hour:02}'.format(date=DATE, hour=hour))

        filename = filename_template.format(date=DATE, hour=hour, min=minute)
        with open(filename, 'w+') as file:
            file.write(r.text)
        print('Download', filename, 'complete.')
