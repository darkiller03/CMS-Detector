# Function for the web scrapping

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from includes.valid import is_valid_url

def scrap_cms(driver, data):
    for entry in data:
        url = entry['url']
        entry['CMS_info'] = {} 
        
        if is_valid_url(url):
            try:
                driver.get("https://seranking.com/free-tools/cms-detector.html")

                input_element = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "microtool-form__field"))
                )
                
                input_element.clear()
                input_element.send_keys(url + Keys.ENTER)

                # Wait for JS to load DOM
                time.sleep(10)

                cms_info = driver.execute_script(
                    "return document.querySelector('.tool-data-table__value.tool-data-table__cms')?.innerText || 'N/A';"
                )

                prog_lg = driver.execute_script(
                    "return document.querySelector('.tool-data-table__value.tool-data-table__programming-languages')?.innerText || 'N/A';"
                )

                db = driver.execute_script(
                    "return document.querySelector('.tool-data-table__value.tool-data-table__databases')?.innerText || 'N/A';"
                )

                web_server = driver.execute_script(
                    "return document.querySelector('.tool-data-table__value.tool-data-table__web-servers')?.innerText || 'N/A';"
                )

                analyt = driver.execute_script(
                    "return document.querySelector('.tool-data-table__value.tool-data-table__analytics')?.innerText || 'N/A';"
                )

                widg = driver.execute_script(
                    "return document.querySelector('.tool-data-table__value.tool-data-table__widgets')?.innerText || 'N/A';"
                )

                plugs = driver.execute_script(
                    "return document.querySelector('.tool-data-table__value.tool-data-table__plugin')?.innerText || 'N/A';"
                )

                lv_chats = driver.execute_script(
                    "return document.querySelector('.tool-data-table__value.tool-data-table__live-chat')?.innerText || 'N/A';"
                )

                cdn = driver.execute_script(
                    "return document.querySelector('.tool-data-table__value.tool-data-table__cdn')?.innerText || 'N/A';"
                )

                # Update entry with CMS info
                entry['CMS_info'] = {
                    'CMS': cms_info,
                    'Programming_languages': prog_lg,
                    'Databases': db,
                    'Web_server': web_server,
                    'Analytics': analyt,
                    'Widgets': widg,
                    'Plugins': plugs,
                    'Live_chats': lv_chats,
                    'CDN': cdn
                }

                print("Updated URL:", url)

            except Exception as e:
                print("Error processing URL:", url, "Error:", e)

                # Set CMS_info to N/A if error
                entry['CMS_info'] = {
                    'CMS': 'N/A',
                    'Programming_languages': 'N/A',
                    'Databases': 'N/A',
                    'Web_server': 'N/A',
                    'Analytics': 'N/A',
                    'Widgets': 'N/A',
                    'Plugins': 'N/A',
                    'Live_chats': 'N/A',
                    'CDN': 'N/A'
                }
        else:
            print(f"Invalid URL: {url}")

            # Set CMS_info to N/A if URL is invalid
            entry['CMS_info'] = {
                'CMS': 'N/A',
                'Programming_languages': 'N/A',
                'Databases': 'N/A',
                'Web_server': 'N/A',
                'Analytics': 'N/A',
                'Widgets': 'N/A',
                'Plugins': 'N/A',
                'Live_chats': 'N/A',
                'CDN': 'N/A'
            }

    driver.quit()
