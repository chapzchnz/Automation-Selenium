import pytest

from tests import patient, login
import tests.patient.patient_search
import tests.patient.create_patient
import tests.patient.patient_view_info
import tests.patient.edit_patient_info
import tests.patient.patient_delete
import tests.patient.dashboard_exercises_search


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True)

if __name__ == '__main__':
    pytest.main()


@pytest.mark.slow
def test_home():
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    driver.get("https://breathment.com/home")
    driver.maximize_window()

    login.test_login(driver)
    patient.create_patient.test_patient_automation(driver)
    patient.patient_search.patient_search_init(driver)
    patient.patient_view_info.patient_view_info_init(driver)
    patient.edit_patient_info.edit_patient_info_init(driver)
    patient.patient_delete.patient_delete_init(driver)
    patient.dashboard_exercises_search.exercise_search_init(driver)
