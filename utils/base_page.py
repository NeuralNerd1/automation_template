# utils/base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
import time
from .logger import setup_logger

class BasePage:
    """Base class for all Page Object Models."""
    
    def __init__(self, driver):
        self.driver = driver
        self.log = setup_logger(self.__class__.__name__)
        self.TIMEOUT = 10
        self.POLL_FREQUENCY = 0.5
        self.MAX_RETRIES = 3

    def find_element(self, by_locator):
        """Finds an element using explicit wait."""
        try:
            element = WebDriverWait(self.driver, self.TIMEOUT).until(
                EC.presence_of_element_located(by_locator)
            )
            return element
        except TimeoutException:
            self.log.error(f"Timeout waiting for element: {by_locator}")
            raise

    def click_element(self, by_locator):
        """Clicks an element with built-in retry logic for StaleElement."""
        for attempt in range(self.MAX_RETRIES):
            try:
                element = WebDriverWait(self.driver, self.TIMEOUT).until(
                    EC.element_to_be_clickable(by_locator)
                )
                element.click()
                self.log.info(f"Clicked element: {by_locator}")
                return
            except StaleElementReferenceException:
                self.log.warning(f"Stale element on attempt {attempt+1}. Retrying...")
                time.sleep(self.POLL_FREQUENCY)
            except TimeoutException as e:
                self.log.error(f"Failed to click element {by_locator} after retries. Error: {e}")
                raise
        
        # If all retries fail, raise the exception
        raise TimeoutException(f"Failed to click element {by_locator} after {self.MAX_RETRIES} attempts.")
        
    def take_screenshot(self, test_name):
        """Captures a screenshot on failure."""
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filename = f"logs/FAILURE_{test_name}_{timestamp}.png"
        self.driver.get_screenshot_as_file(filename)
        self.log.info(f"Screenshot saved to: {filename}")
        return filename