#!/usr/bin/env python
# coding=utf-8

import socket
import sys
from _thread import *
import time
from datetime import datetime, date, timedelta

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base, Association, Bus, Paradas

import os
from colorama import *
init()

engine = create_engine('sqlite:///busControlApp.db?check_same_thread=False')
DBSession = sessionmaker(bind=engine)
session = DBSession()

'''
userX = User(t_name="Test user", t_email="project3User@testmail.com", t_picture="dededed")
session.add(userX)
session.commit()
'''


HOST = '192.168.1.28'  # host pc ip
PORT = 9999        # Port to listen on (non-privileged ports are > 1023)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((HOST, PORT))
except socket.error as e:
    print(str(e))

s.listen()

todayDate = date.today()
todayTime = datetime.now().time()
print('current date: %s' % todayDate)
print('current time: %s' % todayTime)
print('waiting for a connection........\n')


def threaded_client(conn, addr):
    conn.send(str.encode('welcome irfd sensor\n'))
    while True:
        data = conn.recv(1024)
        reply = 'server output: ' + data.decode('utf-8')
        dTime = datetime.now().time().strftime("%H:%M:%S")
        todaydb = datetime.today()
        nowp = addr[0]

        print('------------------------RDFI detectado------------------------')
        if not data:
            break
        # print('RFID complete message: ', repr(data))
        # print('string manipulation test \n')
        rfidmessage = str(data)
        #print('rfidmessage: %s' % rfidmessage[2:12])
        #print('rdfimessss type: %s' % type(rfidmessage))
        print('Parada >>> %s' % addr[0])
        print("Bus nombre >>> %s" % rfidmessage[2:12])
        print('Fecha y Hora >>> %s' % todaydb.strftime("%Y-%m-%d %H:%M:%S"))
        print('Hora para DB %s type(dTime): %s' % (dTime, type(dTime)))
        print('\n')

        # DB findings
        
        # DB info on paradas
        dbParada = session.query(Paradas).filter_by(parada_Ip=nowp).first()
        print('paradaDB parada_id: %s \nparadaDB parada_Ip: %s \nparadaDB parada_Time: %s \nparadaDB parada_nombre: %s \nparadaDB parada_desc: %s' % (dbParada.id, dbParada.parada_Ip, dbParada.parada_Time, dbParada.parada_nombre, dbParada.parada_desc))

        #Db info on buses
        if session.query(Bus).filter_by(bus_Hex=rfidmessage[2:12]).first():
            dbbus = session.query(Bus).filter_by(bus_Hex=rfidmessage[2:12]).first()
            print('busdb id: %s\nbusdb bus_Hex: %s \nbusdb bus_placa: %s \nbusdb bus_chofer: %s' % (dbbus.id, dbbus.bus_Hex, dbbus.bus_Placa, dbbus.bus_chofer))
        else:
            print("nothing but why? \n rfidmessage = %s " % rfidmessage)

        # early arrival and delay logic before de DB entry
        # print("dbParada.parada_Time + 300: %s " % dbParada.parada_Time+300) error

        dbTime = datetime.strptime(dbParada.parada_Time, "%H:%M:%S")
        print('this is dbTime: %s type: %s' % (dbTime, type(dbTime)))

        dTime = datetime.strptime(dTime, "%H:%M:%S")
        print('this is dTime: %s type: %s' % (dTime, type(dTime)))

        if dTime > dbTime + timedelta(minutes=10):
            print(Fore.RED + "Hora Marcada: %s Resultado: %s" % (dTime.time(), "ATRASO"))
            print(Style.RESET_ALL)
            new_diario = Association(bus_id=dbbus.id, parada_id=dbParada.id, pase_hora=str(dTime.time()), pase_fecha=todaydb.strftime("%Y-%m-%d"), resultado='ATRASO')
            session.add(new_diario)
            session.commit()
        elif dTime < dbTime - timedelta(minutes=10):
            print(Fore.YELLOW + "hora marcada: %s Resultado: %s" %(dTime.time(), "ADELANTADO"))
            print(Style.RESET_ALL)
            new_diario = Association(bus_id=dbbus.id, parada_id=dbParada.id, pase_hora=str(dTime.time()), pase_fecha=todaydb.strftime("%Y-%m-%d"), resultado='ADELANTADO')
            session.add(new_diario)
            session.commit()
        elif dTime >= dbTime - timedelta(minutes=10) and dTime <= dbTime + timedelta(minutes=10):
            print(Fore.GREEN + "hora marcada: %s resultado: %s" % (dTime.time(), "A TIEMPO"))
            print(Style.RESET_ALL)
            new_diario = Association(bus_id=dbbus.id, parada_id=dbParada.id, pase_hora=str(dTime.time()), pase_fecha=todaydb.strftime("%Y-%m-%d"), resultado='A TIEMPO')
            session.add(new_diario)
            session.commit()


        conn.sendall(str.encode(reply))
    conn.close()

while True:
    conn, addr = s.accept()
    print('Conectado a la Parada: ' + addr[0] + ':' + str(addr[1]))
    start_new_thread(threaded_client, (conn, addr))