from selenium import webdriver
from selenium.webdriver.chrome.options import ChromiumOptions
from selenium.webdriver.common.by import By
import time

wait_time=1
url = "https://jamaicanpatwah.com/translator"
english = input()

options = ChromiumOptions()
options.add_argument("--headless=new")

driver = webdriver.Chrome(options=options)
driver.get(url)

input_element = driver.find_element(By.ID, "original_text")
input_element.send_keys(english)

submit_element = driver.find_element(By.ID, "main_trans_btn")
submit_element.click()

time.sleep(wait_time)
output_element = driver.find_element(By.ID, "translated_text")
patwah = output_element.get_attribute("value")
patwah = patwah[:-1]
print(patwah)

driver.quit() 
