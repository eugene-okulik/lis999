from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
import pytest
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()
# options.add_argument("start-maximized")


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(5)
    chrome_driver.maximize_window()
    yield chrome_driver
    sleep(5)
    chrome_driver.quit()


def test_first_name(driver):
    driver.get(" https://demoqa.com/automation-practice-form")

    first_name = driver.find_element(By.ID, "firstName")
    first_name.send_keys("Sergey")

    last_name = driver.find_element(By.ID, "lastName")
    last_name.send_keys("Li")

    user_email = driver.find_element(By.ID, "userEmail")
    user_email.send_keys("sergey.sergey@yahoo.com")

    male = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located(
            (By.CSS_SELECTOR, "#genterWrapper label.custom-control-label")
        )
    )
    male.click()

    user_number = driver.find_element(By.ID, "userNumber")
    user_number.send_keys("123456789")

    date_of_birth = driver.find_element(By.ID, "dateOfBirthInput")
    date_of_birth.click()
    date_of_birth.send_keys(Keys.CONTROL + "a")
    date_of_birth.send_keys("30 May 1984")
    date_of_birth.send_keys(Keys.ENTER)

    # subject_container = driver.find_element(By.ID, "subjectContainer")
    # subject_container.send_keys("Filling the practice form")

    hobby = driver.find_element(By.XPATH, "//label[contains(text(), 'Music')]")
    hobby.click()

    current_address = driver.find_element(By.ID, "currentAddress")
    current_address.send_keys("somewhere in Seattle")

    select_state = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.ID, "react-select-3-input"))
    )
    select_state.send_keys("Uttar Pradesh")
    select_state.send_keys(Keys.ENTER)

    select_city = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.ID, "react-select-4-input"))
    )
    select_city.send_keys("Merrut")
    select_city.send_keys(Keys.ENTER)

    submit = driver.find_element(By.CSS_SELECTOR, "#submit")
    submit.click()

    print(first_name.get_attribute("value"))
    print(last_name.get_attribute("value"))
    print(user_email.get_attribute("value"))
    print(male.text)
    print(user_number.get_attribute("value"))
    print(date_of_birth.get_attribute("value"))
    print(hobby.text)
    print(current_address.get_attribute("value"))
    print(select_state.get_attribute("value"))
    print(select_city.get_attribute("value"))
