from flask import Flask, jsonify
import time
import random
from threading import Thread

app = Flask(__name__)

# Global variable of job status.
job_status = "pending"
# Randomize delay time.
delay_time = random.randint(50, 100)

def simulate_job():
    global job_status
    # Simulate the processing time.
    time.sleep(delay_time)
    if random.random() < 0.05:  # Random chance for an error.
        job_status = "error"
    else:
        job_status = "completed"

# Start job simulation.
Thread(target=simulate_job).start()

@app.route('/status', methods=['GET'])
def get_status():
    return jsonify({"result": job_status})

if __name__ == '__main__':
    app.run(port=5000)
