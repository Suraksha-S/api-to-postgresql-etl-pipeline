# API to PostgreSQL ETL Pipeline

A simple end-to-end ETL (Extract, Transform, Load) pipeline built using Python.

The pipeline extracts user data from a public REST API, transforms and cleans the data using Pandas, and loads the processed data into PostgreSQL.

## Project Architecture

```text
Public REST API
       │
       ▼
   EXTRACT
   (Requests)
       │
       ▼
   Raw JSON Data
       │
       ▼
   TRANSFORM
   (Pandas)
       │
       ▼
 Cleaned DataFrame
       │
       ▼
     LOAD
 (SQLAlchemy)
       │
       ▼
   PostgreSQL
```

## Features

* Extracts user data from a public REST API.
* Transforms raw JSON data into a Pandas DataFrame.
* Cleans and standardizes data.
* Removes duplicate records.
* Handles missing required values.
* Loads transformed data into PostgreSQL.
* Uses PostgreSQL UPSERT to prevent duplicate records.
* Supports idempotent pipeline execution.
* Uses environment variables for database configuration.
* Includes logging.
* Includes automated tests using Pytest.

## Technologies Used

* Python
* Requests
* Pandas
* PostgreSQL
* SQLAlchemy
* psycopg2
* python-dotenv
* Pytest

## Project Structure

```text
api-to-postgresql-etl-pipeline/
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── logger.py
│   └── main.py
│
├── sql/
│   └── create_tables.sql
│
├── tests/
│   └── test_transform.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## ETL Process

### 1. Extract

Data is extracted from the following public REST API:

`https://jsonplaceholder.typicode.com/users`

The Python `requests` library is used to retrieve the user data.

### 2. Transform

The extracted JSON data is transformed using Pandas.

The transformation process includes:

* Selecting required columns.
* Renaming `id` to `user_id`.
* Removing unnecessary spaces.
* Standardizing email addresses.
* Handling missing required values.
* Removing duplicate records.

### 3. Load

The transformed data is loaded into PostgreSQL.

SQLAlchemy and the PostgreSQL driver (`psycopg2`) are used to connect Python with PostgreSQL.

The pipeline uses PostgreSQL UPSERT functionality:

```text
INSERT
   ↓
If record already exists
   ↓
UPDATE
```

This prevents duplicate records.

## Idempotency

The pipeline is designed to be idempotent.

This means that running the pipeline multiple times produces the same final result without creating duplicate records.

Example:

```text
Run 1 → 10 users
Run 2 → 10 users
Run 3 → 10 users
```

The PostgreSQL UPSERT functionality ensures that existing records are updated instead of duplicated.

## Prerequisites

Make sure the following are installed:

* Python 3
* PostgreSQL
* pip

## Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
```

Navigate to the project directory:

```bash
cd api-to-postgresql-etl-pipeline
```

### 2. Create a Virtual Environment

```bash
python3 -m venv .venv
```

Activate the virtual environment:

Linux/WSL:

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Database Setup

Create the PostgreSQL database:

```sql
CREATE DATABASE etl_pipeline_db;
```

Create a database user and grant the required permissions.

Run the table creation script:

```bash
psql -h localhost -U etl_user -d etl_pipeline_db -f sql/create_tables.sql
```

## Environment Variables

Create a `.env` file in the project root.

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=etl_pipeline_db
DB_USER=etl_user
DB_PASSWORD=your_password
```

Do not commit the `.env` file to GitHub.

## Run the Pipeline

From the project root:

```bash
python src/main.py
```

## Run Tests

Run:

```bash
pytest -v
```

The tests verify transformation logic, including:

* Data cleaning
* Missing required values
* Duplicate records

## Verify Data

Connect to PostgreSQL:

```bash
psql -h localhost -U etl_user -d etl_pipeline_db
```

Check the number of records:

```sql
SELECT COUNT(*) FROM users;
```

Check the stored data:

```sql
SELECT * FROM users;
```

## Future Improvements

Possible improvements for this project include:

* Schedule the pipeline using Apache Airflow.
* Deploy the pipeline using Google Cloud Run.
* Use Cloud Scheduler for automated execution.
* Add data validation.
* Add more automated tests.
* Add structured logging.
* Add retry mechanisms for API and database failures.
* Store raw data before transformation.
* Add CI/CD using GitHub Actions.

## Author

Suraksha

## Learning Outcomes

Through this project, I learned:

* Data Engineering fundamentals.
* ETL pipeline architecture.
* Extracting data from REST APIs.
* Transforming data using Pandas.
* Loading data into PostgreSQL.
* Database connectivity using SQLAlchemy.
* PostgreSQL UPSERT.
* Idempotency.
* Environment variables.
* Logging.
* Basic automated testing using Pytest.


