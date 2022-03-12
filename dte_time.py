import datetime

#just comment
#added second line 

tday = datetime.date.today()
d1 = datetime.date(2001, 11, 16)

# print(d1-d)
td = datetime.date.today()
# print(td)
# print(td.year)

tdelta = datetime.timedelta(days=7)

# print(td + tdelta)

bday = datetime.date(2001,11,18)
till_bday = tday - bday
# print(till_bday)


# t = datetime.time(9,30,45,100000)
# print(t.hour)

t = datetime.datetime(2021,3,12,3,23,45,100000)
print(t.date())
print(t.time())

