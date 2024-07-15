# Function to verify the URL

import requests

def is_valid_url(url):
    try:
        response = requests.head(url, allow_redirects=True, timeout=8)
        return response.status_code == 200
    except requests.RequestException as e:
        print(f"Error reaching {url}: {e}")
        return False