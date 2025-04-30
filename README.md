# PostgreSQL CLI Tool

This is a simple Python-based CLI utility that helps users interact with a PostgreSQL database.

### Features
- Test connection to PostgreSQL
- List databases
- List tables in a database
- Show schema of a specific table
- Export table data to CSV

### Requirements
- Python 3.x
- `psycopg2` package

Install with:
```bash
pip install psycopg2
```

### Usage
Set your PostgreSQL credentials as environment variables:
```bash
export PGHOST=localhost
export PGUSER=your_user
export PGPASSWORD=your_password
export PGDATABASE=your_database
```

Run the tool:
```bash
python pgcli.py
```
