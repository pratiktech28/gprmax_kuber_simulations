import pandas as pd
import sqlite3
import os
import sys 

def aggregate_data():
    db_path = '/data/simulation_registry.db'
    if not os.path.exists(db_path):
        print(f"[-] Error: Database not found at {db_path}")
        return

    try:
        conn = sqlite3.connect(db_path)
        query = "SELECT * FROM simulations WHERE status='completed'"
        df = pd.read_sql_query(query, conn)
        
        if df.empty:
            print("[!] No completed simulations found.")
            return

        summary = df.describe()
        summary.to_csv('/data/final_summary.csv')
        print("[+] Success: Summary saved to /data/final_summary.csv")
        conn.close()
    except Exception as e:
        print(f"[-] Database Error: {e}")
        raise e

if __name__ == "__main__":
    try:
        aggregate_data()
        print("[***] MISSION ACCOMPLISHED [***]")
        sys.exit(0)  
    except Exception:
        sys.exit(1)  