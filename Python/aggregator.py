import os
import time
import sys
import sqlite3
import pandas as pd

def run_aggregation():
    db_path = '/data/simulation_registry.db'
    output_path = '/data/final_summary.csv'

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

        # --- ✅ FINAL SUCCESS SIGNAL & GRACE PERIOD ---
        print("[***] JOB COMPLETED SUCCESSFULLY [***]")
        print("[*] Sleeping for 180s to allow GitHub to extract artifacts...")
        
        time.sleep(200) 
        sys.exit(0)

    except Exception as e:
        print(f"[-] Error during processing: {e}")
        time.sleep(10)
        sys.exit(1)

if __name__ == "__main__":
    run_aggregation()