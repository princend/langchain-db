import abc 
from abc import ABCMeta
import settings 
import urllib.parse

class DBBaseConnection(metaclass=ABCMeta):
     @abc.abstractmethod
     def getUri(self)->str:
         return ''
     
     
# Sqlite 連接字串
class SQLliteConnection(DBBaseConnection): 
     def getUrui(self)->str:
         return 'sqlite:///Chinook.db'
    
# mysql連接字串    
class MySqlConnection(DBBaseConnection):
      def getUri(self) -> str:
            username = settings.db_username
            password = settings.db_password  # 替換為您的 MySQL 密碼
            host = settings.db_host
            database = settings.db_name  # 替換為您的數據庫名稱
            port=settings.db_port
            encoded_password = urllib.parse.quote(password)
            connection_string = f'mysql+pymysql://{username}:{encoded_password}@{host}:{port}/{database}'
            return connection_string
          