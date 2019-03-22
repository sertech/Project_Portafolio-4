from datetime import datetime, date, timedelta

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base, Association, Bus, Paradas

import random
import string
import time
import os

from colorama import *
init()


engine = create_engine('sqlite:///busControlApp.db?check_same_thread=False')
DBSession = sessionmaker(bind=engine)
session = DBSession()


todayDate = date.today() # class datetime.date 2018-12-05
todayTime = datetime.now().time() # class datetime.time 

dbTime = datetime.now().time().strftime("%H:%M:%S") # class str

anyRecord = session.query(Paradas).filter_by(id=1).first() # class str

print("todayDate(date.today()) = %s \ntype = %s\n" % (todayDate, type(todayDate)))

print("todayTime(datetime.now().time()) = %s\ntype = %s\n" % (todayTime, type(todayTime)))

print("dbTime(datetime.now().time().strftime(H:M:S)) = %s \n type = %s\n" % (dbTime, type(dbTime)))

print("from DB anyRecord.parada_Time = %s \ntype = %s \n" % (anyRecord.parada_Time, type(anyRecord.parada_Time)))

# sample 1
date_time_str = '2018-06-29 08:15:27.243860'  
date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')

print('Date:', date_time_obj.date())
print('Time:', date_time_obj.time())
print('Date-time:', date_time_obj)
print('\n')

# conversion 
# test 1

print('db time conversion to type time\n')
fbDateTime = datetime.strptime(anyRecord.parada_Time, '%H:%M:%S')
print('fbDateTime: %s type: %s' % (fbDateTime, type(fbDateTime)))
bfplus30 = fbDateTime - timedelta(minutes=20)
print('fbDateTime - 20 minutes: %s type: %s' % (bfplus30, type(bfplus30)))
print('fbDateTime just the time for DB: %s' % bfplus30.time())

print('\n')
print('part 2 fors and ifs \n')
# test 2 time comparisons with DB

print('the year does not matter but is has to be there for calculations')
print('fixed time in DB: %s \n' % fbDateTime)

print('-------------------LOGIC TEST------------------------\n')
print('Rules:\n')
print('FIXED TIME: 19:00:00 \n DELAY: 19:10:00 +10[m]\n AHEAD: 18:50:00 -10[m]\n')
for i in range(50):
    rTime=bfplus30+timedelta(minutes=random.randint(1, 60))
    # print('rTime: %s type: %s' % (rTime.time(), type(rTime.time())))
    if rTime > fbDateTime + timedelta(minutes=10):
        #os.system("color 04")
        print(Fore.RED + "Time: %s Result: %s" % (rTime.time(), "ATRASO"))
    elif rTime < fbDateTime - timedelta(minutes=10):
        #os.system("color 0E")
        print(Fore.YELLOW + 'time: %s Result: %s' % (rTime.time(), "ADELANTADO"))
    elif rTime >= fbDateTime - timedelta(minutes=10) and rTime <= fbDateTime + timedelta(minutes=10):
        #os.system("color 0A")
        print(Fore.GREEN + 'time: %s Result: %s' % (rTime.time(), "A TIEMPO"))
    time.sleep(0.5)

