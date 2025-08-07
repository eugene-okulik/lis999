from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

options = Options()
options.add_argument("start-maximized")
# options.add_experimental_option('detach', True) # this option helps to keep the browser open
driver = webdriver.Chrome(options=options)
# driver.maximize_window()
# driver.set_window_size(500, 800)
driver.get("https://www.qa-practice.com/elements/input/simple")
search_field = driver.find_element(By.ID, "id_text_string")
search_field.send_keys("Test_text")
search_field.submit()
result_text = driver.find_element(By.ID, "result-text")
print(result_text.text)
