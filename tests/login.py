import time

from selenium.common import TimeoutException

import pages.login_page as x_path
import resources.application_settings as resources
import resources.error_message as error_message
import utils.locale_utils as locale_utils
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.slow
def test_login(driver):
    before_login_allow_all_btn_click(driver)
    change_language(driver)
    test_click_login_navbar_btn(driver)
    test_login_error_wrong_email_test(driver)
    test_login_success(driver)
    # logout(driver)


def test_click_login_navbar_btn(driver):
    time.sleep(5)
    links = driver.find_elements("xpath", x_path.heading_anchor_links)
    login_text = locale_utils.get("login")
    for link in links:
        if login_text in link.get_attribute("innerHTML"):
            link.click()
            break


def logout(driver):
    profile_icon = driver.find_element("xpath", x_path.logout_btn).click()

    # actions = ActionChains(driver)
    # actions.move_to_element(profile_icon).perform()

    # logout_link = driver.find_element_by_xpath(x_path.logout_btn)
    # actions.move_to_element(logout_link).click().perform()

    driver.quit()


def test_login_error_wrong_email_test(driver):
    driver.find_element("xpath", x_path.email_input).send_keys(
        'abc@gmail.com')
    driver.find_element("xpath", x_path.password_input).send_keys(resources.password)
    driver.find_element("xpath", x_path.login_btn).click()

    wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds
    login_error_msg = wait.until(EC.visibility_of_element_located((By.XPATH, x_path.login_alert_danger)))
    assert login_error_msg.text == locale_utils.get("login_error_msg")
    time.sleep(5)
    clear_fields(driver)


def clear_fields(driver):
    driver.find_element("xpath", x_path.email_input).clear()
    driver.find_element("xpath", x_path.password_input).clear()


def test_login_success(driver):
    driver.find_element("xpath",
                        x_path.email_input).send_keys(
        resources.username)
    driver.find_element("xpath",
                        x_path.password_input).send_keys(
        resources.password)
    driver.find_element("xpath", x_path.login_btn).click()


def before_login_allow_all_btn_click(driver):
    # Click the XPath button
    driver.find_element("xpath", x_path.before_login_allow_all_btn).click()


def change_language(driver):

    if resources.APPLICATION_LOCALE == "en_EN":
        links = driver.find_elements("xpath", "//span | //img[contains(@src, 'uk-flag.png')]")
    else:
        links = driver.find_elements("xpath", "//span | //img[contains(@src, 'germany-flag.png')]")

    for link in links:
        if link.tag_name == 'img':
            link.click()
            break
