from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains


options = Options()
# options.add_argument("start-maximized")


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


def test_product_new_tab(driver):
    driver.get("http://testshop.qa-practice.com/")
    wait = WebDriverWait(driver, 10)
    action = ActionChains(driver)
    main_window = driver.current_window_handle
    initial_tabs = len(driver.window_handles)

    product = wait.until(
        ec.element_to_be_clickable((By.CSS_SELECTOR, 'img[alt="Customizable Desk"]'))
    )

    action.key_down(Keys.CONTROL).click(product).key_up(Keys.CONTROL).perform()

    wait.until(lambda d: len(d.window_handles) > initial_tabs)
    driver.switch_to.window(driver.window_handles[-1])

    add_to_cart_button = wait.until(ec.element_to_be_clickable((By.ID, "add_to_cart")))
    add_to_cart_button.click()

    modal = wait.until(
        ec.visibility_of_element_located((By.CLASS_NAME, "modal-content"))
    )
    modal.click()

    continue_button = wait.until(
        ec.element_to_be_clickable(
            (By.XPATH, '//button[.//span[text()="Continue Shopping"]]')
        )
    )
    continue_button.click()
    wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, "modal-content")))
    driver.close()
    wait.until(lambda d: len(d.window_handles) == 1)
    driver.switch_to.window(main_window)

    shopping_cart = wait.until(
        ec.element_to_be_clickable(
            (By.CSS_SELECTOR, "a[href='/shop/cart'][aria-label='eCommerce cart']")
        )
    )
    shopping_cart.click()
    cart_items = wait.until(ec.presence_of_element_located((By.ID, "cart_products")))
    assert "Customizable Desk" in cart_items.text


def test_compare_products(driver):
    driver.get("https://magento.softwaretestingboard.com/gear/bags.html")
    wait = WebDriverWait(driver, 10)
    action = ActionChains(driver)

    product = wait.until(
        ec.element_to_be_clickable(
            (By.CSS_SELECTOR, 'img[alt="Push It Messenger Bag"]')
        )
    )
    compare_button = driver.find_element(By.CSS_SELECTOR, "a[title='Add to Compare']")
    action.move_to_element(product).perform()
    action.move_to_element(compare_button).click().perform()

    items_to_compare = wait.until(
        ec.visibility_of_element_located((By.CSS_SELECTOR, ".block-compare"))
    )
    assert "Push It Messenger Bag" in items_to_compare.text
