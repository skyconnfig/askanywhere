from typing import Dict
import os

class DatabaseConfig:
    def __init__(self):
        self.config: Dict[str, str] = {
            'driver': 'ODBC Driver 13 for SQL Server',
            'server': os.getenv('DB_SERVER', 'localhost'),
            'database': os.getenv('DB_NAME', 'deepseek'),
            'username': os.getenv('DB_USER', 'sa'),
            'password': os.getenv('DB_PASSWORD', 'saSA123')
        }
    
    def get_connection_string(self) -> str:
        return f"DRIVER={{{self.config['driver']}}};\
                SERVER={self.config['server']};\
                DATABASE={self.config['database']};\
                UID={self.config['username']};\
                PWD={self.config['password']}"