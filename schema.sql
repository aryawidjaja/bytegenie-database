DROP TABLE IF EXISTS companies;
DROP TABLE IF EXISTS events;
DROP TABLE IF EXISTS people;

CREATE TABLE companies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_logo_url TEXT,
    company_logo_text TEXT,
    company_name TEXT,
    relation_to_event TEXT,
    event_url TEXT,
    company_revenue TEXT,
    n_employees TEXT,
    company_phone TEXT,
    company_founding_year REAL,
    company_address TEXT,
    company_industry TEXT,
    company_overview TEXT,
    homepage_url TEXT,
    linkedin_company_url TEXT,
    homepage_base_url TEXT UNIQUE,
    company_logo_url_on_event_page TEXT,
    company_logo_match_flag TEXT
);

CREATE TABLE events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_logo_url TEXT,
    event_name TEXT,
    event_start_date DATE,
    event_end_date DATE,
    event_venue TEXT,
    event_country TEXT,
    event_description TEXT,
    event_url TEXT UNIQUE
);

CREATE TABLE people (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    middle_name TEXT,
    last_name TEXT,
    job_title TEXT,
    person_city TEXT,
    person_state TEXT,
    person_country TEXT,
    email_pattern TEXT,
    homepage_base_url TEXT,
    duration_in_current_job TEXT,
    duration_in_current_company TEXT,
    email_address TEXT,
    FOREIGN KEY (homepage_base_url) REFERENCES companies (homepage_base_url)
);

CREATE TABLE conversations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_query_summary TEXT,
    user_query TEXT,
    retrieved_data TEXT,
    model_response TEXT,
    date_time TEXT,
    query_status TEXT
);