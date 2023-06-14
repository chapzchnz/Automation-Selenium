import pytest
import pages.patient_delete_page as patient_delete_page

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

import pages.physiotherapy_dashboard_page as physiotherapy_dashboard_page
import resources.patient_detail as patient_detail


@pytest.mark.slow
def patient_delete_init(driver):
    delete_first_patient(driver)
    click_delete_patient_confirm_btn(driver)


def delete_first_patient(driver):
    wait = WebDriverWait(driver, 10)
    delete_first_patient_btn = wait.until(
        EC.visibility_of_element_located((By.XPATH, patient_delete_page.delete_first_patient_icon)))
    delete_first_patient_btn.click()


def click_delete_patient_confirm_btn(driver):
    wait = WebDriverWait(driver, 10)
    delete_first_patient_confirm_btn = wait.until(
        EC.visibility_of_element_located((By.XPATH, patient_delete_page.delete_patient_confirm_popup_btn)))
    delete_first_patient_confirm_btn.click()
