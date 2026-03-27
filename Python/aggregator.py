import pandas as pd
import sqlite3
import os
import sys
import time

def aggregate_data():
    db_path = '/data/simulation_registry.db'
    output_path = '/data/final_summary.csv'
    
    print("[*] Starting Aggregator...")
    
    for i in range(20): 
        if os.path.exists(db_path):
            print(f"[+] DB found after {i*30} seconds.")
            break
        print(f"[*] Waiting for DB... ({i+1}/20)")
        time.sleep(30)
    else:
        print("[-] DB never appeared. Failing fast.")
        sys.exit(1)

    try:
        conn = sqlite3.connect(db_path)
        df = pd.read_sql_query("SELECT * FROM simulations", conn)
        
        if df.empty:
            print("[!] No data found. Creating dummy signal file.")
            pd.DataFrame([{"status": "no_data"}]).to_csv(output_path)
        else:
            df.describe().to_csv(output_path)
            print(f"[+] Summary saved with {len(df)} rows.")
        
        conn.close()
        print("[***] SUCCESS: AGGREGATION COMPLETE [***]")
        os._exit(0) 
    except Exception as e:
        print(f"[-] Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    aggregate_data()