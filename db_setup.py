import random
import string
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from passlib.apps import custom_app_context as pwd_context

from itsdangerous import   TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired

Base = declarative_base()

# secret key generation

secret_key = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(32))

class Bus(Base): # parent
    __tablename__ = 'bus' # left - The left side of the relationship references the association object via one-to-many,
    id = Column(Integer, primary_key=True)
    bus_Hex = Column(String(15), nullable=False)
    bus_Placa = Column(String(7), nullable=False)
    bus_chofer = Column(String(100), nullable=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'bus_Hex': self.bus_Hex,
            'bus_Placa': self.bus_Placa,
            'bus_chofer': self.bus_chofer
        }
    

class Paradas(Base): # child
    __tablename__ = 'paradas' # right -association class references the right side via many-to-one
    id = Column(Integer, primary_key=True)
    parada_Ip = Column(String(15), nullable=False)
    parada_Time = Column(String(20), nullable=False)
    parada_nombre = Column(String(100), nullable=False)
    parada_desc = Column(String(200), nullable=False)

    @property
    def serialize(self):
        return{
            'id': self.id,
            'parada_Ip': self.parada_Ip,
            'parada_Time': self.parada_Time,
            'parada_nombre': self.parada_nombre,
            'parada_desc': self.parada_desc
        }


class Association(Base):
    __tablename__ = 'association'
    id = Column(Integer, primary_key=True)
    bus_id = Column(Integer, ForeignKey('bus.id', ondelete="CASCADE"))
    relationBus = relationship(Bus)
    parada_id = Column(Integer, ForeignKey('paradas.id', ondelete="CASCADE"))
    relationParada = relationship(Paradas)
    pase_hora = Column(String(30), nullable=False)
    pase_fecha = Column(String(30), nullable=False)
    resultado = Column(String(30), nullable=False)

    @property
    def serialize(self):
        return{
            'id': self.id,
            'bus_id': self.bus_id,
            'parada_id': self.parada_id,
            'pase_hora': self.pase_hora,
            'pase_fecha': self.pase_fecha,
            'resultado': self.resultado
        }


engine = create_engine('sqlite:///busControlApp.db')
Base.metadata.create_all(engine)
