import sqlite3
import os

def init_shared_db():
    db_path = '/data/simulation_registry.db'
    if not os.path.exists('/data'):
        os.makedirs('/data')
        
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS results (
            pod_id TEXT,
            file TEXT,
            status TEXT,
            duration TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    print(f"[+] Database Initialized at {db_path}")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_shared_db()