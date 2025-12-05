# tests/test_facebook_login.py
from pages.facebook_login_page import FacebookLoginPage
import pytest

# Test function MUST start with 'test_' and accept 'driver' and 'base_url' fixtures
def test_unsuccessful_login_attempt(driver, base_url):
    """Test scenario for logging in with known bad credentials."""
    
    # --- 1. Initialization ---
    login_page = FacebookLoginPage(driver)
    
    # --- 2. Actions ---
    driver.get(base_url) 
    
    # Use placeholder credentials (Facebook typically blocks automation, but this demonstrates the flow)
    login_page.enter_credentials("fake@email.com", "badpassword")
    login_page.click_login_button()
    
    # Wait briefly for potential redirection or error message to appear
    # NOTE: You would normally assert for an ERROR message, but for this template, 
    # we'll assert that the SUCCESS element is NOT found.
    
    # --- 3. Assertion ---
    # Assert that the success element is NOT present, confirming the login FAILED.
    assert login_page.is_login_successful() == False, \
        "ERROR: Successful login element was found despite using bad credentials."