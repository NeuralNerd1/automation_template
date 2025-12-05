# tests/conftest.py
import pytest
from utils.driver_factory import DriverFactory
from utils.base_page import BasePage
import os

# --- Fixtures for driver and base_url ---
@pytest.fixture(scope="session")
def base_url():
    """Provides the base URL from the CLI runner's environment variables."""
    return os.environ.get('TEST_BASE_URL')

@pytest.fixture(scope="function")
def driver(request):
    """Initializes, quits, and handles screenshot on failure."""
    browser = os.environ.get('TEST_BROWSER', 'chrome')
    headless = os.environ.get('TEST_HEADLESS', 'False').lower() == 'true'
    
    web_driver = DriverFactory.get_driver(browser, headless)
    
    yield web_driver # EXECUTES THE TEST
    
    # Teardown logic
    if request.node.rep_call.failed:
        base_page = BasePage(web_driver)
        base_page.take_screenshot(request.node.name)
        
    web_driver.quit()

# --- Pytest Hook (DO NOT CHANGE) ---
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)