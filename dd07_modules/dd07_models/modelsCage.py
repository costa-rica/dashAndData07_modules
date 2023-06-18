print("- in modelsCage")
# from .main import Base_cage, sess_cage
from .main import dict_base
# from sqlalchemy.orm import sessionmaker, Session, relationship
from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey, \
    Date, Boolean, Table

Base_cage = dict_base['Base_cage']

class CageCompanies(Base_cage):
    # __bind_key__ = 'Cage_bind'
    __tablename__ = 'cage_companies'
    CAGE_code = Column(String(5),primary_key=True)
    ADRS_NM_LN_NO__01 = Column(String(2))
    ADRS_NM_C_TXT1 = Column(String(36))
    ADRS_NM_LN_NO__2 = Column(String(2))
    ADRS_NM_C_TXT2 = Column(String(36))
    ST_ADDRESS1 = Column(String(36))
    ST_ADDRESS2 = Column(String(36))
    PO_BOX = Column(String(36))
    CITY = Column(String(36))
    ST_US_POSN = Column(String(2))
    ZIP_CODE = Column(String(10))
    COUNTRY = Column(String(36))
    TELEPHONE_NUMBER = Column(String(12))
    
    # def __init__(self, CAGE_code=None, ADRS_NM_LN_NO__01=None,ADRS_NM_C_TXT1=None,ADRS_NM_LN_NO__2=None,ADRS_NM_C_TXT2=None,ST_ADDRESS1=None,ST_ADDRESS2=None,PO_BOX=None,CITY=None,ST_US_POSN=None,ZIP_CODE=None,COUNTRY=None,TELEPHONE_NUMBER=None):
        # self.data =(CAGE_code,ADRS_NM_LN_NO__01,ADRS_NM_C_TXT1,ADRS_NM_LN_NO__2,ADRS_NM_C_TXT2,ST_ADDRESS1,ST_ADDRESS2,PO_BOX,CITY,ST_US_POSN,ZIP_CODE,COUNTRY,TELEPHONE_NUMBER)
    
    def __repr__(self):
        return f"CageCompanies({self.CAGE_code},{self.ADRS_NM_C_TXT1},{self.ST_US_POSN})"
        # return f"Industrynames({self.series_id},{self.series_title})"