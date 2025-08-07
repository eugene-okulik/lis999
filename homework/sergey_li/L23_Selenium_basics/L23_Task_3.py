from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import pytest
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(5)
    chrome_driver.maximize_window()
    yield chrome_driver
    sleep(5)
    chrome_driver.quit()


def test_selected_language(driver):
    driver.get("https://www.qa-practice.com/elements/select/single_select")
    select_element = driver.find_element(By.ID, "id_choose_language")
    dropdown = Select(select_element)
    dropdown.select_by_visible_text("Ruby")
    submit_button = driver.find_element(By.CSS_SELECTOR, "#submit-id-submit")
    submit_button.click()

    result = WebDriverWait(driver, 5).until(
        ec.presence_of_element_located((By.ID, "result-text"))
    )
    assert result.text == "Ruby"


def test_loaded_result(driver):
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    id_button = driver.find_element(By.CSS_SELECTOR, "#start button")
    id_button.click()

    result = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, "finish"))
    )
    assert result.text == "Hello World!"
