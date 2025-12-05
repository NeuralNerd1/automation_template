# utils/driver_factory.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

class DriverFactory:
 
    
    @staticmethod
    def get_driver(browser_name, headless=False, options=None):
        driver = None
        
        if options is None:
            options = []

        if browser_name.lower() == 'chrome':
            chrome_options = webdriver.ChromeOptions()
            for opt in options:
                chrome_options.add_argument(opt)
            if headless:
                chrome_options.add_argument("--headless")
            
            # Use Service object for modern Selenium versions
            chrome_service = ChromeService(ChromeDriverManager().install())
            
            driver = webdriver.Chrome(
                service=chrome_service,
                options=chrome_options
            )
        
        

        else:
            raise ValueError(f"Unsupported browser: {browser_name}")

        return driver