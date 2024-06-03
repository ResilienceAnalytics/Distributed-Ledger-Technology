from sqlalchemy import Column, Integer, String, Float, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Block(Base):
    __tablename__ = 'blocks'
    id = Column(Integer, primary_key=True)
    index = Column(Integer)
    timestamp = Column(Float)
    data = Column(JSON)
    proof = Column(Integer)
    previous_hash = Column(String)

class Node(Base):
    __tablename__ = 'nodes'
    id = Column(Integer, primary_key=True)
    address = Column(String)

engine = create_engine('sqlite:///blockchain.db')
Base.metadata.create_all(engine)
