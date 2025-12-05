"""
===========================================================
 AUTO-GENERATED SELENIUM TEST SCRIPT
 Source: No-Code Automation Builder
===========================================================

Prerequisites:
-------------
1. Install Python 3.8+
2. Install dependencies:
   pip install selenium webdriver-manager

To Run:
-------
python automation_script.py

Structure:
----------
- Each Test Case is generated from your lanes in the builder.
- Test Case count: 1
- Variables and elements come from the Variables / Elements panels.

Notes:
------
- This file is auto-generated; prefer editing flows in the builder UI.
- You can customize small details here if needed.
===========================================================
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# ===========================
# Global Variables
# ===========================
variables = {
    "URL": "https://git.pod-staging.com/HAJ0rW/onboarding-landing/hfgwBiKZnpSe0bDK112TQwL9Z_2mUahLQYnH5xRAvGFa3D-p3Z0J6oMhxyxEd9WNjq_U2ZnU-YkM74mgFajwZQ/e314d36ad4e84079011b355e00253e32c2b13040?invited_by_admin=True"
}

# ===========================
# Element Repository (Reference)
# ===========================
# No elements saved in the builder.

# ===========================
# Helper Functions
# ===========================
def wait_for_element(driver, locator_type, locator_value, timeout=10):
    by_map = {
        "id": By.ID,
        "xpath": By.XPATH,
        "css": By.CSS_SELECTOR,
        "name": By.NAME,
        "tag": By.TAG_NAME,
        "class": By.CLASS_NAME,
        "link_text": By.LINK_TEXT,
    }
    by = by_map.get(locator_type.lower())
    if by is None:
        raise ValueError(f"Unsupported locator type: {locator_type}")
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((by, locator_value))
    )

# ====================================================
#                     TEST CASES
# ====================================================

def test_case_1(driver):
    print("Running test_case_1 - Login")
    # Step 1: Navigate to URL
    driver.get(variables["URL"])
    driver.implicitly_wait(10)
    # Wait strategy: load

    # Step 2: Type text
    el = wait_for_element(driver, "css", "#input_0", timeout=10)
    el.send_keys("password1")
    driver.implicitly_wait(10)

    # Step 3: Type text
    el = wait_for_element(driver, "css", "#input_1", timeout=10)
    el.send_keys("password1")
    time.sleep(1)

    # Step 4: Click element
    el = wait_for_element(driver, "css", ".action.md-button.md-ink-ripple", timeout=10)
    el.click()
    time.sleep(5)


# ====================================================
#                    MAIN EXECUTION
# ====================================================
if __name__ == "__main__":
    from selenium.webdriver.chrome.service import Service
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        test_case_1(driver)
    finally:
        driver.quit()