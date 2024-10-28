import subprocess
import time
from client import VideoTranslationClient

def run_test():
    # Start the server in a separate process.
    server_process = subprocess.Popen(["python", "server.py"])
    time.sleep(1)

    try:
        # Run the client.
        client = VideoTranslationClient(base_url="http://127.0.0.1:5000")
        result = client.check_status()
        print("Integration test result:", result)

    finally:
        # Terminate the server in the end.
        server_process.terminate()

if __name__ == "__main__":
    run_test()
