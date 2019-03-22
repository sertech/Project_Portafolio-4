import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base, Association, Bus, Paradas

import random
import string

engine = create_engine('sqlite:///busControlApp.db')
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Add dummy buses to the DB
new_bus = json.loads("""{
    "newBus": [
        {
            "bus_Hex":"76b7c43237",
            "bus_Placa":"1324TYF",
            "bus_chofer":"Milton Capuma Condori"
        },
        {
            "bus_Hex":"262eeb48ab",
            "bus_Placa":"6516RDD",
            "bus_chofer":"Peter Kantuta Kasa"
        },
        {
            "bus_Hex":"90cfe3873b",
            "bus_Placa":"8461SDF",
            "bus_chofer":"Markos Castro TunTun"
        },
        {
            "bus_Hex":"k1tn8as3dt",
            "bus_Placa":"3245DFG",
            "bus_chofer":"Mauricio Loza Cruz"
        },
        {
            "bus_Hex":"9bbgtm8q4k",
            "bus_Placa":"1592OHS",
            "bus_chofer":"Rocket Vampichoco"
        }
    ]
}""")

for xbus in new_bus['newBus']:
    print(xbus)
    new_bus = Bus(bus_Hex=str(xbus['bus_Hex']), bus_Placa=str(xbus['bus_Placa']), bus_chofer=str(xbus['bus_chofer']))
    session.add(new_bus)
    session.commit()

# Add dummy paradas to the DB
new_paradas = json.loads("""{
    "newParadas": [
        {
            "parada_Ip": "192.168.1.200",
            "parada_Time": "19:00:00",
            "parada_nombre":"German Bush",
            "parada_desc":"Ut consequat ad aute ullamco anim ad velit esse nostrud duis proident non. Cillum cillum nostrud officia culpa nulla nostrud officia quis ipsum Lorem esse excepteur. Ullamco anim irure et irure enim ea esse."
        },
        {
            "parada_Ip": "192.168.1.210",
            "parada_Time": "20:00:00",
            "parada_nombre":"Cancha Quarto Centenario",
            "parada_desc":"Mollit esse officia deserunt laborum reprehenderit nostrud. Exercitation non proident elit velit. Do ex cillum nisi ipsum cillum.."
        },
        {
            "parada_Ip": "192.168.1.220",
            "parada_Time": "21:00:00",
            "parada_nombre":"Cancha Maracana",
            "parada_desc":"Proident duis nostrud sit eiusmod aliqua ipsum. Occaecat incididunt aute do mollit ullamco laborum. Velit laborum velit proident eiusmod irure aute ea sint fugiat est aliquip enim. Consectetur ut in reprehenderit aute qui excepteur laborum deserunt non sint enim enim sint aliqua. Duis officia est duis quis sunt laborum commodo nisi occaecat reprehenderit veniam enim est. Aliqua laboris elit mollit ipsum aliquip. Ea ipsum eiusmod consequat nisi labore elit non irure dolor eu consectetur anim ad."
        },
        {
            "parada_Ip": "192.168.1.230",
            "parada_Time": "22:00:00",
            "parada_nombre":"Calvario",
            "parada_desc":"Est enim magna dolor ea ullamco nulla eiusmod irure enim amet elit quis. Pariatur duis eu cupidatat voluptate minim minim. Ut voluptate eu cupidatat culpa consequat dolore id dolor ipsum reprehenderit excepteur ullamco eu eiusmod. Amet velit fugiat sit aliqua velit aute eiusmod excepteur eu qui nostrud."
        },
        {
            "parada_Ip": "192.168.1.240",
            "parada_Time": "23:00:00",
            "parada_nombre":"La llamita",
            "parada_desc":"Dolore est sit adipisicing nostrud aliquip veniam tempor duis consequat exercitation. Minim magna ex deserunt cupidatat qui consectetur incididunt. Consectetur sint commodo occaecat sit minim laborum sunt dolor dolore. Nostrud est Lorem cupidatat sunt amet nulla."
        }
    ]
}""")

for xParada in new_paradas['newParadas']:
    print(xParada)
    newParada = Paradas(parada_Ip=str(xParada['parada_Ip']), parada_Time=str(xParada['parada_Time']), parada_nombre=str(xParada['parada_nombre']), parada_desc=str(xParada['parada_desc']))
    session.add(newParada)
    session.commit()


# Add dummy Hoy
# parada 1 a tiempo: 19:00:00 adelantado:18:30:00 restrasado:19:30:00

# parada 2 a tiempo: 20:00:00 adelantado:19:30:00 restrasado:20:30:00

# parada 3 a tiempo: 21:00:00 adelantado:20:30:00 restrasado:21:30:00

# parada 4 a tiempo: 22:00:00 adelantado:21:30:00 restrasado:22:30:00

# parada 5 a tiempo: 23:00:00 adelantado:22:30:00 restrasado:23:30:00

new_hoy = json.loads("""{
    "hoy":[
        {
            "bus_id": 1,
            "parada_id": 1,
            "pase_hora": "19:15:00",
            "pase_fecha": "2018-11-27", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 2,
            "parada_id": 1,
            "pase_hora": "19:10:00",
            "pase_fecha": "2018-11-27",
            "resultado": "A tiempo"
        },
        {
            "bus_id": 3,
            "parada_id": 1,
            "pase_hora": "19:00:00",
            "pase_fecha": "2018-11-27", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 4,
            "parada_id": 1,
            "pase_hora": "19:20:00",
            "pase_fecha": "2018-11-27", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 5,
            "parada_id": 1,
            "pase_hora": "19:15:00",
            "pase_fecha": "2018-11-27", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 1,
            "parada_id": 2,
            "pase_hora": "20:11:00",
            "pase_fecha": "2018-11-27", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 2,
            "parada_id": 2,
            "pase_hora": "20:28:00",
            "pase_fecha": "2018-11-27", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 3,
            "parada_id": 2,
            "pase_hora": "20:12:00",
            "pase_fecha": "2018-11-27", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 4,
            "parada_id": 2,
            "pase_hora": "20:14:00",
            "pase_fecha": "2018-11-27", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 5,
            "parada_id": 2,
            "pase_hora": "20:18:00",
            "pase_fecha": "2018-11-27", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 1,
            "parada_id": 3,
            "pase_hora": "21:11:00",
            "pase_fecha": "2018-11-27",
            "resultado": "A tiempo"
        },
        {
            "bus_id": 2,
            "parada_id": 3,
            "pase_hora": "21:16:00",
            "pase_fecha": "2018-11-27", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 3,
            "parada_id": 3,
            "pase_hora": "21:17:00",
            "pase_fecha": "2018-11-27", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 4,
            "parada_id": 3,
            "pase_hora": "21:19:00",
            "pase_fecha": "2018-11-27", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 5,
            "parada_id": 3,
            "pase_hora": "21:13:00",
            "pase_fecha": "2018-11-27",
            "resultado": "A tiempo"
        },
        {
            "bus_id": 1,
            "parada_id": 4,
            "pase_hora": "22:16:00",
            "pase_fecha": "2018-11-27", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 2,
            "parada_id": 4,
            "pase_hora": "22:14:12",
            "pase_fecha": "2018-11-27", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 3,
            "parada_id": 4,
            "pase_hora": "22:12:30",
            "pase_fecha": "2018-11-27", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 4,
            "parada_id": 4,
            "pase_hora": "22:16:00",
            "pase_fecha": "2018-11-27", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 5,
            "parada_id": 4,
            "pase_hora": "22:19:19",
            "pase_fecha": "2018-11-27", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 1,
            "parada_id": 5,
            "pase_hora": "23:18:00",
            "pase_fecha": "2018-11-27", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 2,
            "parada_id": 5,
            "pase_hora": "23:11:00",
            "pase_fecha": "2018-11-27", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 3,
            "parada_id": 5,
            "pase_hora": "23:17:00",
            "pase_fecha": "2018-11-27", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 4,
            "parada_id": 5,
            "pase_hora": "23:00:00",
            "pase_fecha": "2018-11-27", 
            "resultado": "A tiempo"
        },
        {
            "bus_id": 5,
            "parada_id": 5,
            "pase_hora": "23:12:00",
            "pase_fecha": "2018-11-27", 
            "resultado": "A tiempo"
        }

    ]
}""")

for xdiario in new_hoy['hoy']:
    print(xdiario)
    newDiario = Association(bus_id=str(xdiario['bus_id']), parada_id=str(xdiario['parada_id']), pase_hora=str(xdiario['pase_hora']), pase_fecha=str(xdiario['pase_fecha']), resultado=str(xdiario['resultado']))
    session.add(newDiario)
    session.commit()