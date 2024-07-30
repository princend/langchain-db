import abc 
from abc import ABCMeta
import settings 
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
            connection_string = f'mysql+pymysql://{username}@{host}/{database}'
            return connection_string
          