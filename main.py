import os
from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase

load_dotenv()
connection_string=os.getenv('DATABASE_URL')
print(connection_string)

# Database connection
query="SELECT * FROM tbl_record_import LIMIT 10"
db=SQLDatabase.from_uri(connection_string)
data=db.run(query)
print(data)