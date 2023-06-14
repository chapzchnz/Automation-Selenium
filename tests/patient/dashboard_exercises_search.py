import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

import pages.physiotherapy_dashboard_page as physiotherapy_dashboard_page
import resources.patient_detail as patient_detail


@pytest.mark.slow
def exercise_search_init(driver):
    test_exercise_search(driver)


def test_exercise_search(driver):
    driver.execute_script("window.scrollTo(0, 500);")

    wait = WebDriverWait(driver, 50)
    search_text = wait.until(EC.visibility_of_element_located((By.XPATH, physiotherapy_dashboard_page.exercise_search)))
    search_text.send_keys(patient_detail.exercise_name)

    wait = WebDriverWait(driver, 50)
    table = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                         physiotherapy_dashboard_page.exercise_detail_table)))
    html_table = table.get_attribute('outerHTML')
    print(html_table)
    soup = BeautifulSoup(html_table, 'html.parser')
    rows = soup.find_all('tr')[1:]
    found = False

    for row in rows:
        columns = row.find_all('td')
        if len(columns) >= 1 and columns[0].text.strip() == patient_detail.exercise_full_name and columns[
            1].text.strip() == patient_detail.exercise_category:

            found = True
            break

    assert found, "The column with the specified values was not found."
