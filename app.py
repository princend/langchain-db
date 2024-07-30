
from langchain_community.utilities.sql_database import SQLDatabase

# 資料庫連線
db = SQLDatabase.from_uri("sqlite:///Chinook.db")

# print(db)
# print(db.get_usable_table_names())
from langchain_community.agent_toolkits import create_sql_agent

from langchain_google_genai import ChatGoogleGenerativeAI


llm = ChatGoogleGenerativeAI(model="gemini-pro",google_api_key='AIzaSyAkWbuYTAjbg3fr-biNzCs_O4zAqwvVe7o')
agent_executor = create_sql_agent(llm, db=db, verbose=True)
# agent_executor = create_sql_agent(llm, db=db, agent_type="openai-tools", verbose=True)
# agent_executor.invoke(
#     "List the total sales per country. Which country's customers spent the most?"
# )
agent_executor.invoke(
    "list all table names"
)