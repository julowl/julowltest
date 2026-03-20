from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from driver import chrome_web_driver as driver

def test_abtest_one(driver):
    driver.get("https://the-internet.herokuapp.com/")
    element = driver.find_element(By.CSS_SELECTOR, 'a[href="/abtest"]')
    assert element is not None
    element.click()
    assert driver.current_url == "https://the-internet.herokuapp.com/abtest"

def test_add_remove_elements_click(driver):
    driver.get("https://the-internet.herokuapp.com/")
    element = driver.find_element(By.CSS_SELECTOR, 'a[href="/add_remove_elements/"]')
    assert element is not None
    element.click()
    assert driver.current_url == "https://the-internet.herokuapp.com/add_remove_elements/"

def test_examle_batton_click(driver):
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
    element = driver.find_element(By.CSS_SELECTOR, "div.example button")
    assert element is not None
    element.click()

    del_button = driver.find_element(By.CSS_SELECTOR, "div#elements button")
    assert del_button is not None
    del_button.click()


def test_basic_auth_click(driver):
    driver.get("https://the-internet.herokuapp.com/")
    element = driver.find_element(By.CSS_SELECTOR,'a[href="/basic_auth"]')
    assert element is not None
    element.click()
    assert driver.current_url == "https://the-internet.herokuapp.com/basic_auth"


