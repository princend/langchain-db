from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

# 連接到本地的 Chinook SQLite 數據庫
engine = create_engine('sqlite:///Chinook.db')

# 創建一個新的元數據對象
metadata = MetaData()

# 定義新表的結構
new_table = Table(
    'Album', metadata,
    Column('AlbumId', Integer, primary_key=True),
    Column('Title', String),
    Column('ArtistId', String)
)

# 新增表到數據庫中
metadata.create_all(engine)

print("Table created successfully")
