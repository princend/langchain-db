
from langchain_community.utilities.sql_database import SQLDatabase
from db_connection import MySqlConnection ,SQLliteConnection
from langchain_community.agent_toolkits import create_sql_agent
from langchain_google_genai import ChatGoogleGenerativeAI
import settings

# 構建連接字串
db_connection_string = MySqlConnection().getUri()
# db_connection_string = SQLliteConnection().getUri()

# 資料庫連線
db = SQLDatabase.from_uri(db_connection_string)

#LLM模型串接
llm = ChatGoogleGenerativeAI(model="gemini-pro",google_api_key=settings.google_api_key)
agent_executor = create_sql_agent(llm, db=db, verbose=True)
# agent_executor = create_sql_agent(llm, db=db, agent_type="openai-tools", verbose=True)

# 問話-自然語言搜尋
answer=agent_executor.invoke(
    "give AC/DC all album names "
)
# answer=agent_executor.invoke(
#     "how many albums Pablo Picasso have?"
# )
# answer=agent_executor.invoke(
#     "list all table names"
# )
# answer=agent_executor.invoke(
#     "I want to find name is ju which's description"
# )

try:
    print(answer['output'])
except Exception as e:
    print(e)
