import sqlite3
import pandas as pd
import time
import sys
import os

def run_aggregation():
    db_path = "/data/simulation_registry.db"
    output_path = "/data/final_summary.csv"
    
    print("[*] Aggregator started. Searching for database...")
    found = False
    for i in range(160):
        if os.path.exists(db_path):
            print(f"[+] Database found after {i*30} seconds!")
            found = True
            break
        print(f"[*] Database not ready yet... Retrying ({i+1}/200)")
        time.sleep(30)

    if not found:
        print("[-] FATAL: Database file never appeared. Check worker pods.")

        sys.exit(1)
    # --- 📊 Data Processing ---
    try:
        print("[*] Starting data aggregation...")
        conn = sqlite3.connect(db_path)
        df = pd.read_sql_query("SELECT * FROM results", conn)
        
        if df.empty:
            print("[!] Database is empty. Nothing to aggregate.")
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
        print("[*] Entering Grace Period: Holding pod for 200s...")
        import time # Safety import
        time.sleep(200)

        if 'e' in locals():
            sys.exit(1) 
        else:
            sys.exit(0) #
if __name__ == "__main__":
    run_aggregation()