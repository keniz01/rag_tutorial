# Create virtual environment
python3 -m venv .venv && source .venv/bin/activate 

# Freeze and install packages
pip3 freeze > requirements.txt
pip3 install -r requirements.txt

# Create user role (Postgres SQL)
CREATE ROLE read_access;
GRANT CONNECT ON DATABASE postgres TO read_access;
GRANT USAGE ON SCHEMA public TO read_access;
GRANT SELECT ON tbl_record_import TO read_access;
CREATE USER usr_reader WITH PASSWORD 'your_password';
GRANT read_access TO usr_reader;