import requests
import time

class VideoTranslationClient:
    def __init__(self, base_url, max_retries=5, backoff_factor=1.5):
        self.url = f"{base_url}/status"
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor

    def check_status(self):
        delay = 1  # Init with 1-second delay.
        retries = 0

        while retries < self.max_retries:
            try:
                response = requests.get(self.url)
                response.raise_for_status()
                status = response.json().get("result")

                print(f"Attempt {retries + 1}: Status is '{status}'")

                if status == "completed":
                    return "Job completed successfully."
                elif status == "error":
                    return "Job encountered an error."

                # Retry with increased delay.
                time.sleep(delay)
                delay *= self.backoff_factor
                retries += 1

            except requests.RequestException as e:
                print(f"Request error: {e}")
                return "Failed to connect to server."

        return "Max retries exceeded."

if __name__ == "__main__":
    client = VideoTranslationClient(base_url="http://localhost:5000")
    result = client.check_status()
    print(result)
