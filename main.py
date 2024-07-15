import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from includes.scrap import scrap_cms

# Options for Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("--silent")

service = Service(executable_path="driver/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

# Read JSON data from input file
input_file = 'data_test.json'
output_file = 'output_data.json'

with open(input_file, 'r') as f:
    data = [json.loads(line) for line in f]

scrap_cms(driver, data)

# Write updated data to output JSON file, each entry on a new line
with open(output_file, 'w') as f:
    for entry in data:
        json.dump(entry, f)
        f.write('\n')

print("Data written to", output_file)
