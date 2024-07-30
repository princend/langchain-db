from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, insert, select

# 連接到本地的 Chinook SQLite 數據庫
engine = create_engine('sqlite:///Chinook.db')

# 創建一個新的元數據對象
metadata = MetaData()

# 定義 NewTable 表的結構
new_table = Table(
    'NewTable', metadata,
    autoload_with=engine
)

# 連接到數據庫並插入新資料
with engine.begin() as connection:
    # 插入一筆新資料到 NewTable
    ins = insert(new_table).values(id=2, name='Ju', description='handsome guy')
    result = connection.execute(ins)

print("Row inserted successfully")

# 檢查資料
with engine.connect() as connection:
    sel = select(new_table)
    result = connection.execute(sel)
    for row in result:
        print(row)
