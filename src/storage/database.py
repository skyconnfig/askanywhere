import pyodbc
from typing import List, Dict, Optional
from ..config.database import DatabaseConfig

class Database:
    def __init__(self):
        self.config = DatabaseConfig()
        self.conn = None

    def connect(self):
        try:
            self.conn = pyodbc.connect(self.config.get_connection_string())
            return True
        except Exception as e:
            print(f"数据库连接失败: {str(e)}")
            return False

    def disconnect(self):
        if self.conn:
            self.conn.close()

    def execute_query(self, query: str, params: tuple = None) -> Optional[List[Dict]]:
        try:
            if not self.conn:
                if not self.connect():
                    return None

            cursor = self.conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)

            if cursor.description:
                columns = [column[0] for column in cursor.description]
                results = [dict(zip(columns, row)) for row in cursor.fetchall()]
                return results

            return None

        except Exception as e:
            print(f"查询执行失败: {str(e)}")
            return None
        finally:
            if cursor:
                cursor.close()

    def execute_procedure(self, proc_name: str, params: tuple = None) -> Optional[List[Dict]]:
        try:
            if not self.conn:
                if not self.connect():
                    return None

            cursor = self.conn.cursor()
            if params:
                cursor.execute(f"EXEC {proc_name} {','.join(['?' for _ in params])}", params)
            else:
                cursor.execute(f"EXEC {proc_name}")

            if cursor.description:
                columns = [column[0] for column in cursor.description]
                results = [dict(zip(columns, row)) for row in cursor.fetchall()]
                return results

            return None

        except Exception as e:
            print(f"存储过程执行失败: {str(e)}")
            return None
        finally:
            if cursor:
                cursor.close()

    def commit(self):
        if self.conn:
            self.conn.commit()

    def rollback(self):
        if self.conn:
            self.conn.rollback()