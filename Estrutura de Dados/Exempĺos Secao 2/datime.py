import datetime as datetime

print(dir(datetime))

datetime.date.today()

datetime.date(2020,7,7)

datetime.datetime(2020,7,7,15,57,29, 324234)

data = datetime.date(2020, 7, 10)

print(data)

data.day
data.month
data.year

horario = datetime.datetime(2020, 7, 10, 7, 30, 0)

horario.hour
horario.minute
horario.second