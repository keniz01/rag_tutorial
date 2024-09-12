import os
from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase
from langchain_core.prompts.few_shot import FewShotPromptTemplate
from langchain_core.prompts import PromptTemplate

load_dotenv()
connection_string=os.getenv('DATABASE_URL')
print(connection_string)

# 1. Database connection
db=SQLDatabase.from_uri(connection_string)
query="SELECT * FROM tbl_record_import LIMIT 10"
data=db.run(query)

# 2. Construct prompt
prompt_template = """
You are a {dialect} expert. Generate SQL statements using the table information provided below:
{table_info}

Generate SQL statements based on the examples provided.
{examples}

Use the following format:
Question: {question}
SQL Query:
"""

example_prompt=PromptTemplate.from_template(prompt_template, input_variables[
    "dialect",
    "table_info",
    "question",
    "sql_query"
])

examples = [
    {
        "question": "How many artists are there?",
        "query": "SELECT COUNT(*) artists from table"
    }
]
one_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    input_variables["dialect","table_info","question","sql_query"]
)

# 3. Generate SQL


# 4. Execute SQL

