# models.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Company(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True)
    company_name = Column(String)
    company_logo_url = Column(String)
    relation_to_event = Column(String)
    company_revenue = Column(String)
    n_employees = Column(String)
    company_phone = Column(String)
    company_founding_year = Column(Float)
    company_address = Column(String)
    company_industry = Column(String)
    homepage_base_url = Column(String, unique=True)

    events = relationship('CompanyEvent', back_populates='company')
    people = relationship('Person', back_populates='company')

class Event(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True)
    event_name = Column(String)
    event_start_date = Column(Date)
    event_end_date = Column(Date)
    event_city = Column(String)
    event_state = Column(String)
    event_country = Column(String)
    event_description = Column(String)
    event_url = Column(String, unique=True)

    companies = relationship('CompanyEvent', back_populates='event')

class Person(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    middle_name = Column(String)
    last_name = Column(String)
    job_title = Column(String)
    person_city = Column(String)
    person_state = Column(String)
    person_country = Column(String)
    email_pattern = Column(String)
    homepage_base_url = Column(String, ForeignKey('companies.homepage_base_url'))

    company = relationship('Company', back_populates='people')

class CompanyEvent(Base):
    __tablename__ = 'company_events'
    company_id = Column(Integer, ForeignKey('companies.id'), primary_key=True)
    event_id = Column(Integer, ForeignKey('events.id'), primary_key=True)

    company = relationship('Company', back_populates='events')
    event = relationship('Event', back_populates='companies')
