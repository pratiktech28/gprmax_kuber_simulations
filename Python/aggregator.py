import matplotlib.pyplot as plt
import sqlite3
import pandas as pd
import os

def aggregate_data():
    db_path = '/data/simulation_registry.db'
    if not os.path.exists(db_path):
        print("[!] No database found. Waiting for workers...")
        return

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

if __name__ == "__main__":
    aggregate_data()