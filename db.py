from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.dialects.sqlite import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class Vehicule(Base):
    __tablename__ = 'Vehicule'
    id = Column(Integer, primary_key=True, nullable=False)
    immatricule = Column(String(50), unique=True)
    owner = Column(String(50))
    cotation = Column(FLOAT)
    facture = Column(FLOAT)
class Proprio(Base):
    __tablename__ = 'Propio'
    id = Column(Integer, primary_key=True, nullable=False)
    immatricule=Column(String(50), unique=True)
    owner = Column(String(50))
    cotation = Column(FLOAT)
    facture = Column(FLOAT)
    total = Column(FLOAT)

Base.metadata.create_all(bind=engine)
