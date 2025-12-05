from selenium.webdriver.common.by import By
from utils.base_page import BasePage
import time

class FacebookLoginPage(BasePage):
    """Page Object Model for the Facebook Login Page."""

    
    _EMAIL_INPUT = (By.NAME, "email")
    _PASSWORD_INPUT = (By.NAME, "pass")
    _LOGIN_BUTTON = (By.NAME, "login")
    
    # A generic element expected on the subsequent page (e.g., the home feed)
    _FEED_HOME_LINK = (By.CSS_SELECTOR, "div[role='main']")

    
    def enter_credentials(self, email, password):
        """High-level method to input both fields."""
        self.log.info(f"Attempting login with email: {email}")
        
        # Uses self.find_element from BasePage (with smart waits)
        self.find_element(self._EMAIL_INPUT).send_keys(email)
        self.find_element(self._PASSWORD_INPUT).send_keys(password)

    def click_login_button(self):
        """Clicks the login button."""
        # Uses self.click_element from BasePage (with retry logic)
        self.click_element(self._LOGIN_BUTTON)
        
    def is_login_successful(self):
        """Verifies successful login by checking for an element on the next page."""
        try:
            # Waits for the home feed link to be visible (or whatever element confirms login)
            self.find_element(self._FEED_HOME_LINK)
            self.log.info("Verification passed: Home link found after login.")
            return True
        except Exception:
            self.log.error("Verification failed: Home link not found after login.")
            return False