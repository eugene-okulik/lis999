from playwright.sync_api import Page, expect, BrowserContext, Dialog
import re
from time import sleep


def test_accept_alert(page: Page):
    page.goto("https://www.qa-practice.com/elements/alert/confirm#")
    sleep(3)
    page.get_by_role("link", name="Click").click()
    sleep(3)
