import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Event, Person
from datetime import datetime

# Database connection
DATABASE_URL = "sqlite:///../database/events_company_people.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# Function to convert date strings to date objects
def parse_date(date_str):
    if pd.isna(date_str):
        return None
    try:
        return datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        return None

# Function to generate email address
def generate_email_address(first_name, last_name, email_pattern, homepage_base_url):
    if not email_pattern or pd.isna(email_pattern):
        return None
    
    first_name = str(first_name) if first_name else ''
    last_name = str(last_name) if last_name else ''
    first_initial = first_name[0].lower() if first_name else ''
    last_initial = last_name[0].lower() if last_name else ''
    domain = homepage_base_url

    email = email_pattern.lower()
    email = email.replace('[first]', first_name.lower())
    email = email.replace('[last]', last_name.lower())
    email = email.replace('[first_initial]', first_initial)
    email = email.replace('[last_initial]', last_initial)
    email = f"{email}@{domain}"

    return email

# Create tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Load data from CSV files
company_info = pd.read_csv('events-data/company_info.csv')
event_info = pd.read_csv('events-data/event_info.csv')
people_info = pd.read_csv('events-data/people_info.csv')

# Populate the Company table
with SessionLocal() as session:
    for _, row in company_info.iterrows():
        if not session.query(Company).filter_by(homepage_base_url=row['homepage_base_url']).first():
            company = Company(
                company_name=row.get('company_name', ''),
                company_logo_url=row.get('company_logo_url', ''),
                company_logo_text=row.get('company_logo_text', ''),
                relation_to_event=row.get('relation_to_event', ''),
                event_url=row.get('event_url', ''),
                company_revenue=row.get('company_revenue', ''),
                n_employees=row.get('n_employees', ''),
                company_phone=row.get('company_phone', ''),
                company_founding_year=row.get('company_founding_year', 0.0),
                company_address=row.get('company_address', ''),
                company_industry=row.get('company_industry', ''),
                company_overview=row.get('company_overview', ''),
                homepage_url=row.get('homepage_url', ''),
                linkedin_company_url=row.get('linkedin_company_url', ''),
                homepage_base_url=row['homepage_base_url'],
                company_logo_url_on_event_page=row.get('company_logo_url_on_event_page', ''),
                company_logo_match_flag=row.get('company_logo_match_flag', '')
            )
            session.add(company)
    session.commit()

# Populate the Event table
with SessionLocal() as session:
    for _, row in event_info.iterrows():
        if not session.query(Event).filter_by(event_url=row['event_url']).first():
            event_logo_url = row.get('event_logo_url', '')
            if not session.query(Event).filter_by(event_logo_url=event_logo_url).first():
                event = Event(
                    event_logo_url=event_logo_url,
                    event_name=row.get('event_name', ''),
                    event_start_date=parse_date(row.get('event_start_date', None)),
                    event_end_date=parse_date(row.get('event_end_date', None)),
                    event_venue=row.get('event_venue', ''),
                    event_country=row.get('event_country', ''),
                    event_description=row.get('event_description', ''),
                    event_url=row['event_url']
                )
                session.add(event)
    session.commit()

# Populate the Person table
with SessionLocal() as session:
    for _, row in people_info.iterrows():
        if not session.query(Person).filter_by(first_name=row['first_name'], last_name=row['last_name'], homepage_base_url=row['homepage_base_url']).first():
            email_address = generate_email_address(
                row.get('first_name', ''),
                row.get('last_name', ''),
                row.get('email_pattern', ''),
                row.get('homepage_base_url', '')
            )
            person = Person(
                first_name=row.get('first_name', ''),
                middle_name=row.get('middle_name', ''),
                last_name=row.get('last_name', ''),
                job_title=row.get('job_title', ''),
                person_city=row.get('person_city', ''),
                person_state=row.get('person_state', ''),
                person_country=row.get('person_country', ''),
                email_pattern=row.get('email_pattern', ''),
                homepage_base_url=row['homepage_base_url'],
                duration_in_current_job=row.get('duration_in_current_job', ''),
                duration_in_current_company=row.get('duration_in_current_company', ''),
                email_address=email_address
            )
            session.add(person)
    session.commit()
