print("- in modelsBls")
from .main import Base, sess_bls
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey, \
    Date, Boolean, Table


#From folioApp.models.py
class IndustryNames(Base):
    # __bind_key__ = 'dbBls'
    __tablename__ = 'industry_names'
    # id = Column(Integer, primary_key=True)
    series_id = Column(String(200), primary_key=True)
    industry_code = Column(String(100))
    product_code = Column(String(100))
    seasonal = Column(String(10))
    base_date = Column(String(10))
    series_title = Column(String(200))
    footnote_codes = Column(String(10))
    begin_year = Column(Integer)
    begin_period = Column(String(3))
    end_year = Column(Integer)
    end_period = Column(String(3))
    values = relationship('IndustryValues', backref='values', lazy=True)


    def __repr__(self):
        return f"IndustryNames({self.series_id},{self.series_title})"

class IndustryValues(Base):
    # __bind_key__ = 'dbBls'
    __tablename__ = 'industry_values'
    id = Column(Integer, primary_key=True)
    series_id = Column(String(200), ForeignKey('industry_names.series_id'))
    # series_id = Column(String(200), ForeignKey('industrynames.series_id'))
    year = Column(Integer)
    period = Column(String(3))
    value = Column(Float)
    footnote_codes = Column(String(10))
    # namesId = Column(Integer, ForeignKey('industrynames.id'))

    def __repr__(self):
        return f"IndustryValues({self.id},{self.series_id},{self.year},{self.period},{self.value})"


class CommodityNames(Base):
    # __bind_key__ = 'dbBls'
    __tablename__ = 'commodity_names'
    series_id = Column(String(200), primary_key=True)
    group_code = Column(String(100))
    item_code = Column(String(100))
    seasonal = Column(String(10))
    base_date = Column(String(10))
    series_title = Column(String(200))
    footnote_codes = Column(String(10))
    begin_year = Column(Integer)
    begin_period = Column(String(3))
    end_year = Column(Integer)
    end_period = Column(String(3))
    values = relationship('CommodityValues', backref='values', lazy=True)


    def __repr__(self):
        return f"CommodityNames({self.series_id},{self.series_title})"

class CommodityValues(Base):
    # __bind_key__ = 'dbBls'
    __tablename__ = 'commodity_values'
    id = Column(Integer, primary_key=True)
    series_id = Column(String(200), ForeignKey('commodity_names.series_id'))
    year = Column(Integer)
    period = Column(String(3))
    value = Column(Float)
    footnote_codes = Column(String(10))


    def __repr__(self):
        return f"CommodityValues({self.id},{self.series_id},{self.year},{self.period},{self.value})"