from playwright.sync_api import Page, expect
import re
from time import sleep


def test_authentication(page: Page):
    sleep(3)
    page.goto("https://the-internet.herokuapp.com/")
    page.get_by_role("link", name="Form Authentication").click()
    sleep(3)
    username_field = page.get_by_role("textbox", name="username")
    username_field.fill("username")
    password_field = page.get_by_role("textbox", name="password")
    password_field.fill("password")
    sleep(3)
    page.get_by_role("button", name="Login").click()
    sleep(3)
