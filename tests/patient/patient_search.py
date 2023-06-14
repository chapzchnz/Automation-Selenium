import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

import pages.physiotherapy_dashboard_page as physiotherapy_dashboard_page
import pages.patient_page as patient_page
import resources.patient_detail as patient_detail


@pytest.mark.slow
def patient_search_init(driver):
    test_search(driver)


def test_search(driver):
    wait = WebDriverWait(driver, 20)
    search_text = wait.until(EC.visibility_of_element_located((By.XPATH, physiotherapy_dashboard_page.patient_search)))
    search_text.send_keys(
        patient_detail.patient_first_name)

    wait = WebDriverWait(driver, 10)

    table = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                         physiotherapy_dashboard_page.patient_detail_table)))

    html_table = table.get_attribute('outerHTML')
    soup = BeautifulSoup(html_table, 'html.parser')
    rows = soup.find_all('tr')[1:]
    found = False

    for row in rows:
        columns = row.find_all('td')
        if len(columns) >= 3 and columns[0].text.strip() == patient_detail.patient_first_name and columns[
            1].text.strip() == patient_detail.patient_last_name and columns[
            2].text.strip() == patient_detail.patient_reason:
            found = True
            break

    assert found, "The column with the specified values was not found."

# def test_exercise_search(driver):
#     wait = WebDriverWait(driver, 10)
#     search_text = wait.until(EC.visibility_of_element_located((By.XPATH, physiotherapy_dashboard_page.test)))
#     search_text.send_keys(
#         patient_detail.patient_exercise)
#
#     wait = WebDriverWait(driver, 10)
#
#     table = wait.until(EC.visibility_of_element_located((By.XPATH,
#                                                          physiotherapy_dashboard_page.patient_detail_table)))
#
#     html_table = table.get_attribute('outerHTML')
#     soup = BeautifulSoup(html_table, 'html.parser')
#     rows = soup.find_all('tr')[1:]
#     found = False
#
#     for row in rows:
#         columns = row.find_all('td')
#         if len(columns) >= 3 and columns[0].text.strip() == patient_detail.patient_first_name and columns[1].text.strip() == patient_detail.patient_last_name and columns[
#             2].text.strip() == patient_detail.patient_reason:
#             found = True
#             break
#
#     assert found, "The column with the specified values was not found."
