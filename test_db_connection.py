import sys
sys.path.append('.')

from src.storage.database import Database

def test_connection():
    db = Database()
    if db.connect():
        print('数据库连接成功！')
        result = db.execute_query('SELECT @@VERSION as version')
        if result:
            print(f'SQL Server版本: {result[0]["version"]}')
        db.disconnect()
    else:
        print('数据库连接失败！')

if __name__ == '__main__':
    test_connection()