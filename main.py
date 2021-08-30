import datetime

with open('data.txt', 'r') as f:
    print(f.read())

with open('data.txt', 'a') as f:
    f.write(str(datetime.date.today()) + '\n')
