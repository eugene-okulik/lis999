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
    email = page.locator("#userEmail")
    email.press_sequentially("sergo@gmail.com", delay=500)
    sleep(3)
    page.locator("#gender-radio-1").click()
    sleep(3)
    mobile = page.get_by_placeholder("Mobile Number")
    mobile.fill("4252555225")
    sleep(3)
