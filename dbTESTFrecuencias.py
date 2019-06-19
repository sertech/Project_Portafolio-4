import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base, Association, Bus, Paradas

import random
import string

engine = create_engine('sqlite:///busControlApp.db')
DBSession = sessionmaker(bind=engine)
session = DBSession()

new_hoy = json.loads("""{
    "hoy":[
        {
            "bus_id": 1,
            "parada_id": 1,
            "pase_hora": "05:03:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 1,
            "parada_id": 2,
            "pase_hora": "05:19:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "Adelantado"
        },
        {
            "bus_id": 1,
            "parada_id": 3,
            "pase_hora": "05:39:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "Adelantado"
        },
        {
            "bus_id": 1,
            "parada_id": 4,
            "pase_hora": "06:07:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 1,
            "parada_id": 5,
            "pase_hora": "06:20:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 2,
            "parada_id": 1,
            "pase_hora": "06:20:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 2,
            "parada_id": 2,
            "pase_hora": "06:37:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "Adelantado"
        },
        {
            "bus_id": 2,
            "parada_id": 3,
            "pase_hora": "07:10:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "Atrasado"
        },
        {
            "bus_id": 2,
            "parada_id": 4,
            "pase_hora": "07:24:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 2,
            "parada_id": 5,
            "pase_hora": "07:49:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "Atrasado"
        },
        {
            "bus_id": 3,
            "parada_id": 1,
            "pase_hora": "07:47:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "Atrasado"
        },
        {
            "bus_id": 3,
            "parada_id": 2,
            "pase_hora": "08:11:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "Atrasado"
        },
        {
            "bus_id": 3,
            "parada_id": 3,
            "pase_hora": "08:25:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 3,
            "parada_id": 4,
            "pase_hora": "08:46:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 3,
            "parada_id": 5,
            "pase_hora": "08:56:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 4,
            "parada_id": 1,
            "pase_hora": "09:07:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "Atrasado"
        },
        {
            "bus_id": 4,
            "parada_id": 2,
            "pase_hora": "09:20:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 4,
            "parada_id": 3,
            "pase_hora": "09:47:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "Atrasado"
        },
        {
            "bus_id": 4,
            "parada_id": 4,
            "pase_hora": "10:08:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "Atrasado"
        },
        {
            "bus_id": 4,
            "parada_id": 5,
            "pase_hora": "10:16:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 5,
            "parada_id": 1,
            "pase_hora": "10:11:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "Adelantado"
        },
        {
            "bus_id": 5,
            "parada_id": 2,
            "pase_hora": "10:31:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "Adelantado"
        },
        {
            "bus_id": 5,
            "parada_id": 3,
            "pase_hora": "10:52:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 5,
            "parada_id": 4,
            "pase_hora": "11:23:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "Atrasado"
        },
        {
            "bus_id": 5,
            "parada_id": 5,
            "pase_hora": "11:34:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 6,
            "parada_id": 1,
            "pase_hora": "11:41:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "Atrasado"
        },
        {
            "bus_id": 6,
            "parada_id": 2,
            "pase_hora": "11:49:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "Adelantado"
        },
        {
            "bus_id": 6,
            "parada_id": 3,
            "pase_hora": "12:09:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "Adelantado"
        },
        {
            "bus_id": 6,
            "parada_id": 4,
            "pase_hora": "12:36:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 6,
            "parada_id": 5,
            "pase_hora": "13:00:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 1,
            "parada_id": 1,
            "pase_hora": "12:57:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 1,
            "parada_id": 2,
            "pase_hora": "13:09:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 1,
            "parada_id": 3,
            "pase_hora": "13:29:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 1,
            "parada_id": 4,
            "pase_hora": "13:48:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 1,
            "parada_id": 5,
            "pase_hora": "14:21:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "Atrasado"
        },
        {
            "bus_id": 2,
            "parada_id": 1,
            "pase_hora": "14:18:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "Atrasado"
        },
        {
            "bus_id": 2,
            "parada_id": 2,
            "pase_hora": "14:34:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 2,
            "parada_id": 3,
            "pase_hora": "14:52:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 2,
            "parada_id": 4,
            "pase_hora": "15:13:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 2,
            "parada_id": 5,
            "pase_hora": "15:32:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 3,
            "parada_id": 1,
            "pase_hora": "15:36:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "Atrasado"
        },
        {
            "bus_id": 3,
            "parada_id": 2,
            "pase_hora": "15:43:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "Adelantado"
        },
        {
            "bus_id": 3,
            "parada_id": 3,
            "pase_hora": "16:18:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "Atrasado"
        },
        {
            "bus_id": 3,
            "parada_id": 4,
            "pase_hora": "16:29:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 3,
            "parada_id": 5,
            "pase_hora": "16:44:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 4,
            "parada_id": 1,
            "pase_hora": "16:51:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 4,
            "parada_id": 2,
            "pase_hora": "17:08:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 4,
            "parada_id": 3,
            "pase_hora": "17:29:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 4,
            "parada_id": 4,
            "pase_hora": "17:43:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 4,
            "parada_id": 5,
            "pase_hora": "18:06:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 5,
            "parada_id": 1,
            "pase_hora": "18:14:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "Atrasado"
        },
        {
            "bus_id": 5,
            "parada_id": 2,
            "pase_hora": "18:34:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "Atrasado"
        },
        {
            "bus_id": 5,
            "parada_id": 3,
            "pase_hora": "18:46:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 5,
            "parada_id": 4,
            "pase_hora": "19:07:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 5,
            "parada_id": 5,
            "pase_hora": "19:25:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 6,
            "parada_id": 1,
            "pase_hora": "19:33:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "Atrasado"
        },
        {
            "bus_id": 6,
            "parada_id": 2,
            "pase_hora": "19:42:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 6,
            "parada_id": 3,
            "pase_hora": "19:57:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "Adelantado"
        },
        {
            "bus_id": 6,
            "parada_id": 4,
            "pase_hora": "20:28:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 6,
            "parada_id": 5,
            "pase_hora": "20:40:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 1,
            "parada_id": 1,
            "pase_hora": "20:36:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 1,
            "parada_id": 2,
            "pase_hora": "21:09:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "Atrasado"
        },
        {
            "bus_id": 1,
            "parada_id": 3,
            "pase_hora": "21:23:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 1,
            "parada_id": 4,
            "pase_hora": "21:35:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "Adelantado"
        },
        {
            "bus_id": 1,
            "parada_id": 5,
            "pase_hora": "22:00:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 2,
            "parada_id": 1,
            "pase_hora": "22:08:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "Atrasado"
        },
        {
            "bus_id": 2,
            "parada_id": 2,
            "pase_hora": "22:28:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "Atrasado"
        },
        {
            "bus_id": 2,
            "parada_id": 3,
            "pase_hora": "22:41:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 2,
            "parada_id": 4,
            "pase_hora": "23:00:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 2,
            "parada_id": 5,
            "pase_hora": "23:14:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 3,
            "parada_id": 1,
            "pase_hora": "23:23:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "Atrasado"
        },
        {
            "bus_id": 3,
            "parada_id": 2,
            "pase_hora": "23:36:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 3,
            "parada_id": 3,
            "pase_hora": "00:00:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 3,
            "parada_id": 4,
            "pase_hora": "00:13:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 3,
            "parada_id": 5,
            "pase_hora": "00:46:00",
            "pase_fecha": "2019-06-18", 
            "resultado": "Atrasado"
        }
    ]
}""")

for xdiario in new_hoy['hoy']:
    print(xdiario)
    newDiario = Association(bus_id=str(xdiario['bus_id']), parada_id=str(xdiario['parada_id']), pase_hora=str(xdiario['pase_hora']), pase_fecha=str(xdiario['pase_fecha']), resultado=str(xdiario['resultado']))
    session.add(newDiario)
    session.commit()