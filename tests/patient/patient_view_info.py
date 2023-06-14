import pytest
import pages.patient_view_page as patient_view_page

import pytest


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.slow
def patient_view_info_init(driver):
    click_patient_info_icon(driver)
    # click_back_btn(driver)


def click_patient_info_icon(driver):
    driver.find_element("xpath", patient_view_page.patient_table_first_row_info_icon).click()

