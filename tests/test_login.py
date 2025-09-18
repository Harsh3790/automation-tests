import pytest
from pages.login_page import LoginPage

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url
    
def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("wrong_user", "wrong_pass")
    assert "inventory" not in driver.current_url

def test_invalid_password(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user","wrong_pass")
    assert "Epic sadface" in driver.page_source