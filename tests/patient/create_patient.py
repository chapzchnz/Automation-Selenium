import pytest

import pages.patient_page as patient_xpath
import resources.patient_detail as new_patient_detail

from selenium.webdriver.common.by import By

from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages import x_path
from resources import error_message


@pytest.mark.slow
def test_patient_automation(driver):
    print("patient automation")
    # print(driver.page_source)
    # for btn in buttons:
    #    print(btn.get_attribute("innerHTML"));

    # driver.find_elements("xpath", ui_binding.patient_create_btn).click()
    # Find and click the "Create patient" button

    test_create_patient_btn_click(driver)
    test_create_patient_popup_click(driver)
    test_create_patient_with_wrong_data(driver)
    test_fill_create_patient_form(driver)
    test_fill_mandatory_lifestyle(driver)


def test_create_patient_popup_click(driver):
    wait = WebDriverWait(driver, 10)
    create_patient_button = wait.until(presence_of_element_located((By.XPATH, x_path.patient_create_popup_yes_btn)))
    # Click the "Create patient" button
    try:
        create_patient_button.click()
        print("Clicked the 'Create patient' popup yes btn")
    except:
        print("Failed to click the 'Create patient' yes button")


def test_create_patient_btn_click(driver):
    # Wait for the button to be present in the DOM
    wait = WebDriverWait(driver, 10)
    create_patient_button = wait.until(presence_of_element_located((By.XPATH, x_path.patient_create_btn)))
    # Click the "Create patient" button
    try:
        create_patient_button.click()
        print("Clicked the 'Create patient' button")
    except:
        print("Failed to click the 'Create patient' button")


def test_fill_create_patient_form(driver):
    driver.find_element("xpath", x_path.patient_first_name).send_keys(
        new_patient_detail.patient_first_name)
    driver.find_element("xpath", x_path.patient_last_name).send_keys(
        new_patient_detail.patient_last_name)
    driver.find_element("xpath", x_path.patient_birth_date).send_keys(
        new_patient_detail.patient_dob)
    driver.find_element("xpath", x_path.patient_email).send_keys(
        new_patient_detail.patient_email)
    driver.find_element("xpath", x_path.patient_phone_number).send_keys(
        new_patient_detail.patient_mobile)
    driver.find_element("xpath", x_path.patient_contact_reason).send_keys(
        new_patient_detail.patient_reason)
    driver.find_element("xpath", x_path.patient_explanation).send_keys(
        new_patient_detail.patient_sickness)
    driver.find_element("xpath", x_path.patinet_next_btn).click()


def test_fill_mandatory_lifestyle(driver):
    driver.find_element("xpath", x_path.chronic_disease).click()
    driver.find_element("xpath", x_path.receiving_treatments).click()
    driver.find_element("xpath", x_path.other_symptoms).click()
    driver.find_element("xpath", x_path.veins).click()
    driver.find_element("xpath", x_path.diabetes).click()
    driver.find_element("xpath", x_path.cardiovasculor_diseases).click()
    driver.find_element("xpath", x_path.concentration).click()
    driver.find_element("xpath", x_path.stress).click()
    driver.find_element("xpath", x_path.sleep).click()
    driver.find_element("xpath", x_path.back_pain).click()
    driver.find_element("xpath", x_path.surgery).click()
    driver.find_element("xpath", x_path.life_style_next_btn).click()
    driver.find_element("xpath", x_path.employment_state).click()
    driver.find_element("xpath", x_path.sitting).click()
    driver.find_element("xpath", x_path.lunch_break).click()
    driver.find_element("xpath", x_path.regular_breaks).click()
    driver.find_element("xpath", x_path.smoke).click()
    driver.find_element("xpath", x_path.sports).click()
    driver.find_element("xpath", x_path.jogging).click()
    driver.find_element("xpath", x_path.next_version2).click()
    wait = WebDriverWait(driver, 10)
    # alert = wait.until(EC.visibility_of_element_located(By.XPATH, "//*[contains(text(), 'Patient Successfully Created!')]"))
    #
    # print(alert)


def test_create_patient_with_wrong_data(driver):
    wait = WebDriverWait(driver, 10)
    next_btn = wait.until(EC.visibility_of_element_located((By.XPATH, x_path.patinet_next_btn)))
    next_btn.click()
    login_error_msg = wait.until(EC.visibility_of_element_located((By.XPATH, patient_xpath.patient_create_first_name_error)))
    assert login_error_msg.text == error_message.this_field_is_required_error_msg

