import sqlite3
import pandas as pd
import time
import sys
import os

def run_aggregation():
    db_path = "/data/simulation_registry.db" 
    output_path = "/data/final_summary.csv"
    
    try:
        print("[*] Starting data aggregation...")
        # Check if DB exists
        if not os.path.exists(db_path):
            print(f"[!] Database not found at {db_path}")
        else:
            conn = sqlite3.connect(db_path)
            df = pd.read_sql_query("SELECT * FROM results", conn)
            
            if df.empty:
                print("[!] Database is empty.")
                df.to_csv(output_path)
            else:
                summary = df.describe()
                summary.to_csv(output_path)
                print(f"[+] Aggregation successful. Saved to {output_path}")
            conn.close()
            print("[***] JOB COMPLETED SUCCESSFULLY [***]")

    except Exception as e:
        print(f"FAILED BUT STAYING ALIVE: {e}")

    finally:
        print("[*] Entering Grace Period: Holding pod for 200s for artifact extraction...")
        time.sleep(200) 
        
        # Check if we should exit with error or success
        if 'e' in locals():
            sys.exit(1)
        else:
            sys.exit(0)

if __name__ == "__main__":
    run_aggregation()