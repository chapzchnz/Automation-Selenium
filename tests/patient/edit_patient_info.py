import time

import pytest
import pages.patient.edit_patient_info_page as edit_patient_info_page
import pages.patient.exercise.available_exercises as available_exercises

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages import patient_view_page


@pytest.mark.slow
def edit_patient_info_init(driver):
    edit_first_patient_btn_click(driver)
    clear_fields(driver)
    edit_patient_details(driver)
    scroll_to_calender(driver)
    click_create_exercise_btn(driver)
    add_exercises(driver)
    select_calender_date(driver)
    scroll_bottom(driver)
    click_back_btn(driver)


def edit_first_patient_btn_click(driver):
    wait = WebDriverWait(driver, 10)
    edit_first_patient_btn = wait.until(
        EC.visibility_of_element_located((By.XPATH, edit_patient_info_page.edit_patient_info_btn)))
    edit_first_patient_btn.click()


def edit_patient_details(driver):
    driver.execute_script("window.scrollTo(0, 300);")
    driver.find_element("xpath", edit_patient_info_page.edit_first_name_input).send_keys("Tikiri")
    driver.find_element("xpath", edit_patient_info_page.edit_last_name_input).send_keys("Liya")
    driver.find_element("xpath", edit_patient_info_page.edit_birthdate_input).send_keys("09/09/1999")
    driver.find_element("xpath", edit_patient_info_page.edit_email_input).send_keys("tikiriliya@gmail.com")
    # driver.find_element("xpath", edit_patient_info_page.edit_save_btn).click()

    wait = WebDriverWait(driver, 20)
    save_btn = wait.until(
        EC.visibility_of_element_located((By.XPATH, edit_patient_info_page.edit_save_btn)))
    save_btn.click()
    edit_confirm_btn = wait.until(
        EC.visibility_of_element_located((By.XPATH, edit_patient_info_page.edit_confirm_btn)))
    edit_confirm_btn.click()


def click_back_btn(driver):
    wait = WebDriverWait(driver, 10)
    back_btn = wait.until(EC.visibility_of_element_located((By.XPATH, patient_view_page.back_btn)))
    back_btn.click()


def clear_fields(driver):
    driver.find_element("xpath", edit_patient_info_page.edit_first_name_input).clear()
    driver.find_element("xpath", edit_patient_info_page.edit_last_name_input).clear()
    driver.find_element("xpath", edit_patient_info_page.edit_birthdate_input).clear()
    driver.find_element("xpath", edit_patient_info_page.edit_email_input).clear()


def scroll_to_calender(driver):
    driver.execute_script("window.scrollTo(0, 2300);")


def click_create_exercise_btn(driver):
    wait = WebDriverWait(driver, 10)
    create_exercise_btn = wait.until(EC.visibility_of_element_located((By.XPATH, edit_patient_info_page.create_exercise_btn)))
    create_exercise_btn.click()


def add_exercises(driver):
    wait = WebDriverWait(driver, 10)
    abdominal_muscle_exercise = wait.until(
        EC.visibility_of_element_located((By.XPATH, available_exercises.abdominal_muscle_add_icon)))
    abdominal_muscle_exercise.click()
    cosmic_center_exercise = wait.until(
        EC.visibility_of_element_located((By.XPATH, available_exercises.cosmic_center_add_icon)))
    cosmic_center_exercise.click()
    cosmic_grounding_exercise = wait.until(
        EC.visibility_of_element_located((By.XPATH, available_exercises.cosmic_grounding_add_icon)))
    cosmic_grounding_exercise.click()
    cosmic_unity_exercise = wait.until(
        EC.visibility_of_element_located((By.XPATH, available_exercises.cosmic_unit_add_icon)))
    cosmic_unity_exercise.click()
    cosmic_victory_exercise = wait.until(
        EC.visibility_of_element_located((By.XPATH, available_exercises.cosmic_victory_add_icon)))
    cosmic_victory_exercise.click()

    next_btn = wait.until(
        EC.visibility_of_element_located((By.XPATH, available_exercises.next_btn)))
    next_btn.click()


def select_calender_date(driver):
    wait = WebDriverWait(driver, 10)
    calender_cell_1 = wait.until(
        EC.visibility_of_element_located((By.XPATH, available_exercises.calender_cell_1)))
    calender_cell_1.click()

    create_btn = wait.until(
        EC.visibility_of_element_located((By.XPATH, available_exercises.create_btn)))
    create_btn.click()


def scroll_bottom(driver):
    time.sleep(10)
    driver.execute_script("window.scrollTo(0, 2500);")
