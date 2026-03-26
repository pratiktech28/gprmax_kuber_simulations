import os
import subprocess
import sqlite3
from datetime import datetime

def run_simulation(input_file):
    print(f"[*] Starting Simulation: {input_file}")
    try:
        pod_id = os.getenv('HOSTNAME', 'local-worker')
        start_time = datetime.now()
        
        subprocess.run(["python3", "-m", "gprMax", input_file, "-n", "1"], check=True)
        
        end_time = datetime.now()
        save_to_db(pod_id, input_file, "SUCCESS", start_time, end_time)
        print(f"[+] Simulation Complete on {pod_id}")
        
    except Exception as e:
        print(f"[!] Error: {str(e)}")
        save_to_db(pod_id, input_file, "FAILED", start_time, datetime.now())

def save_to_db(pod_id, file_name, status, start, end):
    conn = sqlite3.connect('/data/simulation_registry.db') # PVC path
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS results 
                     (pod_id TEXT, file TEXT, status TEXT, duration TEXT)''')
    duration = str(end - start)
    cursor.execute("INSERT INTO results VALUES (?, ?, ?, ?)", (pod_id, file_name, status, duration))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    run_simulation("user_input.in")