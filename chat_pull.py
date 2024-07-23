from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

def download_chat_data(video_url, output_filename):
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")

    chrome_driver_path = "/opt/homebrew/bin/chromedriver" 

    driver = webdriver.Chrome(service=ChromeService(chrome_driver_path), options=chrome_options)
    driver.get("https://www.twitchchatdownloader.com/video/")

    try:
        # Wait for the input field to be present
        input_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, 'video-url'))
        )
        input_field.send_keys(video_url)
        input_field.send_keys(Keys.RETURN)

        # Wait for the download button to be clickable
        download_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//button[text()="Download chat"]'))
        )
        download_button.click()

        # Wait for the export button to be clickable
        export_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//button[text()="Export chat"]'))
        )
        export_button.click()

        # Wait for the file to be downloaded
        download_dir = "/Users/akashmohan/Downloads"  # Update this to your download directory
        timeout = 120  # Maximum wait time in seconds
        start_time = time.time()

        while time.time() - start_time < timeout:
            files = [f for f in os.listdir(download_dir) if f.endswith('.csv')]
            if files:
                file_path = os.path.join(download_dir, files[0])
                os.rename(file_path, output_filename)
                print(f"Chat data downloaded successfully and saved as {output_filename}")
                break
            time.sleep(1)
        else:
            print("Failed to download chat data within the timeout period.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        driver.quit()
