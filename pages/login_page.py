from core.element_resolver import resolve_element

class LoginPage:
    def __init__(self, driver, elements, yaml_path):
        self.driver = driver
        self.elements = elements
        self.yaml_path = yaml_path

    def click_login(self):
        btn = resolve_element(
            self.driver,
            "login_button",
            self.elements["login_button"],
            self.yaml_path
        )
        btn.click()
