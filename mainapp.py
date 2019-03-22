# -------- python functinality imports--------------------------

from flask import Flask, render_template, request, redirect, jsonify, \
    url_for, flash, g, abort
from flask import session as login_session
import random
import string
import httplib2
import json
from flask import make_response
import requests
import re
import bleach
from functools import wraps

# ------------------------- DB imports---------------------

from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker
from db_setup import Base, Bus, Association, Paradas

# connect to the data base and create a session-----------
engine = create_engine('sqlite:///busControlApp.db?check_same_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()
# ---------------------------------------------------------

app = Flask(__name__)

@app.route('/')
@app.route('/busrecord')
def mainPage():
    hoy = session.query(Association).order_by(desc(Association.id)).limit(10)
    tpardas = session.query(Paradas).all()
    tbuses = session.query(Bus).all()
    return render_template('hoy.html', apphoy=hoy, appParadas=tpardas, appBuses=tbuses)

@app.route('/paradas/')
def ParadasPage():
    totalParadas = session.query(Paradas).all()
    return render_template('Paradas.html', appParadas=totalParadas)

@app.route('/paradas/newParada', methods=['POST'])
def newParada():
    print(request.form['paradaIP'])
    if session.query(Paradas).filter_by(parada_Ip=request.form['paradaIP']).first():
        return "La parada ya existe en la Base de Datos"

    if request.method == 'POST':
        nparada = Paradas(parada_Ip=request.form['paradaIP'], parada_Time=request.form['paradaTime'], parada_nombre=request.form['paradaNombre'], parada_desc=request.form['paradaDesc']) 
        session.add(nparada)
        session.commit()
        return redirect('/paradas/')
    else:
        pass

@app.route('/paradas/<path:paradaIp>/edit', methods=['GET', 'POST'])
def editParada(paradaIp):
    currentParada = session.query(Paradas).filter_by(parada_Ip=paradaIp).one_or_none()
    allParadas = session.query(Paradas).all()

    for iparada in allParadas:
        if iparada.parada_Ip == currentParada.parada_Ip:
            xparada = iparada

    if request.method == 'POST':
        print("it is a POST request")
        currentParada.parada_Ip = request.form['newParadaIp']
        currentParada.parada_Time = request.form['newParadaTime']
        currentParada.parada_nombre = request.form['newParadaName']
        currentParada.parada_desc = request.form['newParadaDesc']
        
        session.add(currentParada)
        session.commit()
        return redirect(url_for('ParadasPage'))


    else:
        print("it is a GET request")
        return render_template('editParada.html', appParada=currentParada)

@app.route('/paradas/<path:paradaIp>/delete', methods=['GET', 'POST'])
def deleteParada(paradaIp):
    delParada = session.query(Paradas).filter_by(parada_Ip=paradaIp).one_or_none()

    if request.method == 'POST':
        if delParada:
            session.delete(delParada)
            session.commit()
        return redirect(url_for('ParadasPage'))
    else:
        print("it is a GET request")
        return render_template('editParada.html', appParada=delParada)


@app.route('/buses/')
def busesPage():
    totalBuses = session.query(Bus).all()
    return render_template('buses.html', appBuses=totalBuses)

@app.route('/buses/newbus', methods=['POST'])
def newBus():
    print(request.form['busHex'])
    if session.query(Bus).filter_by(bus_Placa=request.form['placaBus']).first():
        return "el bus ya existe en la base de datos"

    if request.method == 'POST':
        nBus = Bus(bus_Hex=request.form['busHex'], bus_Placa=request.form['placaBus'], bus_chofer=request.form['choferBus'])
        session.add(nBus)
        session.commit()
        return redirect('/buses/')

@app.route('/buses/<path:busPlaca>/edit', methods=['GET', 'POST'])
def editBus(busPlaca):
    currentBus = session.query(Bus).filter_by(bus_Placa=busPlaca).one_or_none()
    if request.method == 'POST':
        print('This is a POST request')
        currentBus.bus_Hex = request.form['nRDFI']
        currentBus.bus_Placa = request.form['nPlaca']
        currentBus.bus_chofer = request.form['nChofer']
        session.add(currentBus)
        session.commit()
        return redirect(url_for('busesPage'))
    else:
        print("this is a GET request")
        return render_template('editBus.html', appBus=currentBus)

@app.route('/buses/<path:busPlaca>/delete', methods=['GET', 'POST'])
def deleteBus(busPlaca):
    delBus = session.query(Bus).filter_by(bus_Placa=busPlaca).one_or_none()
    if request.method == 'POST':
        if delBus:
            session.delete(delBus)
            session.commit()
        return redirect(url_for('busesPage'))
    else:
        print("this is the GET request")
        return render_template('editBus.html', appBus=delBus)

@app.route('/reporteDate/summary', methods=['GET', 'POST'])
def repDate():    
    if request.method == 'POST':
        sumDate = request.form['repDate']
        tpardas = session.query(Paradas).all()
        tbuses = session.query(Bus).all()
        allDates = session.query(Association).filter_by(pase_fecha=sumDate).all()
        for idate in allDates:
            print(idate.pase_fecha)
        return render_template('reporteFecha.html', appDate=sumDate, appSumary=allDates, appParadas=tpardas, appBuses=tbuses)
    else:
        print('this is the GET response so goes first')
        return render_template('reporteFecha.html')

@app.route('/busrecord/JSON/allBuses')
def allBusesCat():
    buses = session.query(Bus).all()
    return jsonify(allBuses=[bus.serialize for bus in buses])

@app.route('/busrecord/JSON/allParadas')
def allParadasCat():
    paradas = session.query(Paradas).all()
    return jsonify(allParadas=[parada.serialize for parada in paradas])

@app.route('/busrecord/JSON/allRecords')
def allRecords():
    records = session.query(Association).all()
    return jsonify(allRecords=[record.serialize for record in records])

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)