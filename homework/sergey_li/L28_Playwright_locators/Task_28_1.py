from playwright.sync_api import Page, expect
import re
from time import sleep


def test_authentication(page: Page):
    page.goto("https://the-internet.herokuapp.com/")
    page.get_by_role("link", name="Form Authentication").click()
    username_field = page.get_by_role("textbox", name="username")
    username_field.fill("username")
    password_field = page.get_by_role("textbox", name="password")
    password_field.fill("password")
    page.get_by_role("button", name="Login").click()


def test_practice_form(page: Page):
    page.goto("https://demoqa.com/automation-practice-form")
    first_name = page.get_by_role("textbox", name="First Name")
    first_name.fill("Sergo")
    last_name = page.get_by_placeholder("Last Name")
    last_name.fill("Lee")
    page.locator("#userEmail").fill("sergo@gmail.com")
    page.locator("label[for='gender-radio-1']").click()
    mobile = page.get_by_placeholder("Mobile Number")
    mobile.fill("4252555225")
    date_of_birth = page.locator("#dateOfBirthInput")
    date_of_birth.fill("May 30 1984")
    date_of_birth.press("Enter")
    object_field = page.locator(
        'div[class = "subjects-auto-complete__value-container subjects-auto-complete__value-container--is-multi css-1hwfws3"]'
    )
    object_field.click()
    sleep(2)
    object_field.press_sequentially("Computer", delay=500)
    object_field.press("Enter")
    page.locator('label[for="hobbies-checkbox-1"]').click()
    address_field = page.get_by_placeholder("Current Address")
    address_field.fill("10450 NE 10th St, Bellevue, WA 98004")
    # address_field.press("Tab")
    select_state = page.locator('//div[text()="Select State"]')
    select_state.click()
    select_state.press_sequentially("Haryana", delay=500)
    page.keyboard.press("ArrowDown")
    page.keyboard.press("Enter")
    select_city = page.locator('//div[text()="Select City"]')
    select_city.click()
    select_city.press_sequentially("Karnal", delay=500)
    page.keyboard.press("ArrowDown")
    page.keyboard.press("Enter")
    page.get_by_role("button", name="Submit").click()
