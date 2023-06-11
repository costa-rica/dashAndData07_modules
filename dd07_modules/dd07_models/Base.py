print("- in modelsBase")
from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship
from .config import config
import os


Base = declarative_base()
engine_users = create_engine(config.SQL_URI_USERS, echo = False, connect_args={"check_same_thread": False})
engine_cage = create_engine(config.SQL_URI_CAGE, echo = False, connect_args={"check_same_thread": False})
engine_bls = create_engine(config.SQL_URI_BLS, echo = False, connect_args={"check_same_thread": False})

SessionUsers = sessionmaker(bind = engine_users)
SessionCage = sessionmaker(bind = engine_cage)
SessionBls = sessionmaker(bind = engine_bls)

sess_users = SessionUsers()
sess_cage = SessionCage()
sess_bls = SessionBls()


