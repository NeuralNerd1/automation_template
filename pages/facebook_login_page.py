from selenium.webdriver.common.by import By
from utils.base_page import BasePage
from core.element_resolver import resolve_healing_element
import time

class FacebookLoginPage(BasePage):
    """Page Object Model for the Facebook Login Page."""

    
    _EMAIL_INPUT = (By.NAME, "email")
    _PASSWORD_INPUT = (By.NAME, "pass")
    _LOGIN_BUTTON = (By.NAME, "login")
    
    # A generic element expected on the subsequent page (e.g., the home feed)
    _FEED_HOME_LINK = (By.CSS_SELECTOR, "div[role='main']")

    
    def enter_credentials(self, email, password):
        email_el = resolve_healing_element(
            self.driver, "EMAIL_INPUT", self._ELEMENTS_YAML
        )
        password_el = resolve_healing_element(
            self.driver, "PASSWORD_INPUT", self._ELEMENTS_YAML
        )

        email_el.send_keys(email)
        password_el.send_keys(password)

    def click_login_button(self):
        btn = resolve_healing_element(
            self.driver, "LOGIN_BUTTON", self._ELEMENTS_YAML
        )
        btn.click()
        
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