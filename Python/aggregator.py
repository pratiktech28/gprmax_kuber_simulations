import matplotlib.pyplot as plt
import sqlite3
import pandas as pd
import os
import time  

def aggregate_data():
    db_path = '/data/simulation_registry.db'
    
    max_retries = 20  
    retry_count = 0
    
    print("[*] Aggregator started. Checking for database...")
    
    while not os.path.exists(db_path):
        if retry_count >= max_retries:
            print("[!] Timeout: Workers failed to create database. Exiting...")
            return
        
        print(f"[!] No database found. Waiting for workers... (Attempt {retry_count+1}/{max_retries})")
        time.sleep(30) 
        retry_count += 1
    
    print("[+] Database found! Starting aggregation...")

    try:
        conn = sqlite3.connect(db_path)
        df = pd.read_sql_query("SELECT * FROM results", conn)

        print("--- SIMULATION SUMMARY ---")
        print(df)

        df['status'].value_counts().plot(kind='bar', color=['green', 'red'])
        plt.title('GSoC: gprMax 10-Pod Cluster Status')
        plt.xlabel('Status')
        plt.ylabel('Count')

        plt.savefig('/data/final_performance_report.png')
        print("[+] Final Report Generated: /data/final_performance_report.png")

        conn.close()
    except Exception as e:
        print(f"[!] Error during aggregation: {e}")

if __name__ == "__main__":
    aggregate_data()