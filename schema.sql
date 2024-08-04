-- schema.sql
CREATE TABLE companies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT,
    company_logo_url TEXT,
    relation_to_event TEXT,
    company_revenue TEXT,
    n_employees TEXT,
    company_phone TEXT,
    company_founding_year REAL,
    company_address TEXT,
    company_industry TEXT,
    homepage_base_url TEXT UNIQUE
);

CREATE TABLE events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_name TEXT,
    event_start_date DATE,
    event_end_date DATE,
    event_city TEXT,
    event_state TEXT,
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
    FOREIGN KEY (homepage_base_url) REFERENCES companies (homepage_base_url)
);

CREATE TABLE company_events (
    company_id INTEGER,
    event_id INTEGER,
    PRIMARY KEY (company_id, event_id),
    FOREIGN KEY (company_id) REFERENCES companies (id),
    FOREIGN KEY (event_id) REFERENCES events (id)
);
