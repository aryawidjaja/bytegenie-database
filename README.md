# ByteGenie Test - Database📊

## Why SQLite?

I chose SQLite for this database because it's lightweight, easy to set up, and perfect for a small to medium-sized dataset like this one. SQLite doesn't require a separate server process, which makes it straightforward to use and ideal for development and testing purposes. Plus, it's widely supported and has all the features we need to get started quickly.

### Tables:

- **companies**
  - `id`: Auto-incrementing ID.
  - `company_name`: Name of the company.
  - `company_logo_url`: URL to the company's logo.
  - `relation_to_event`: How the company is related to the event (like sponsor or partner).
  - `company_revenue`: The company's revenue.
  - `n_employees`: Number of employees.
  - `company_phone`: Phone number.
  - `company_founding_year`: Year the company was founded.
  - `company_address`: Company address.
  - `company_industry`: Industry the company is in.
  - `homepage_base_url`: The company's homepage URL (this needs to be unique).

- **events**
  - `id`: Auto-incrementing ID.
  - `event_name`: Name of the event.
  - `event_start_date`: When the event starts.
  - `event_end_date`: When the event ends.
  - `event_city`: City where the event is held.
  - `event_state`: State where the event is held.
  - `event_country`: Country where the event is held.
  - `event_description`: Description of the event.
  - `event_url`: URL to the event (this needs to be unique).

- **people**
  - `id`: Auto-incrementing ID.
  - `first_name`: First name of the person.
  - `middle_name`: Middle name of the person.
  - `last_name`: Last name of the person.
  - `job_title`: Job title.
  - `person_city`: City where the person is based.
  - `person_state`: State where the person is based.
  - `person_country`: Country where the person is based.
  - `email_pattern`: Pattern for the person's email.
  - `homepage_base_url`: The company's homepage URL this person works for.

- **company_events**
  - `company_id`: ID of the company.
  - `event_id`: ID of the event.

## What I Ran Into

1. **Unique Constraints:**
   - I had to make sure there were no duplicate entries for `homepage_base_url` in `companies` and `event_url` in `events`.

2. **Date Formatting:**
   - Converting date strings from the CSV files into proper date objects so SQLite would accept them.

3. **Missing and Inconsistent Data:**
   - Handling cases where some data was missing or didn't match up across the different CSV files.

## How I'd Improve It

1. **Normalization:**
   - Breaking things down even more to avoid redundant data and keep everything clean. Maybe separate tables for addresses, phone numbers, and industries.

2. **Indexing:**
   - Adding indexes on columns I query a lot to make things faster.

3. **Data Validation:**
   - Adding more checks during data import to catch and fix issues early.

4. **Scalability:**
   - Looking into ways to scale the database if I start getting a lot more data. Maybe partitioning tables or switching to a more scalable system.

## How to Get Started

1. **Setup Virtual Environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `.\venv\Scripts\activate`
   pip install -r requirements.txt
   ```

2. **Initialize Database:**
   ```sh
   python init_db.py
   ```

3. **Connecting to the Database Using DBeaver:**
    - Open DBeaver and set up a new SQLite connection.
    - Point it to the `events_company_people.db` file in the database directory.
    - You can now explore the tables and see all the data.
