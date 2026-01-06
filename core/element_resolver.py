import yaml
import datetime
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

BY_MAP = {
    "css": By.CSS_SELECTOR,
    "xpath": By.XPATH,
    "id": By.ID,
    "name": By.NAME
}

def resolve_element(driver, element_name, element_config, yaml_path):
    # 1. Try primary locator
    try:
        return _find(driver, element_config["primary"])
    except NoSuchElementException:
        pass

    # 2. Try fallback locators
    for fallback in element_config.get("fallbacks", []):
        try:
            element = _find(driver, fallback)
            _heal_locator(element_name, fallback, yaml_path)
            return element
        except NoSuchElementException:
            continue

    # 3. Heuristic recovery
    element = _heuristic_search(driver, element_config.get("metadata"))
    if element:
        _auto_update_locator(element_name, element, yaml_path)
        return element

    raise Exception(f"Element '{element_name}' not found")

def resolve_healing_element(driver, element_key, yaml_path):
    with open(yaml_path, "r") as f:
        elements = yaml.safe_load(f)

    config = elements[element_key]

    # 1️⃣ Try primary
    try:
        return driver.find_element(
            BY_MAP[config["primary"]["by"]],
            config["primary"]["value"]
        )
    except NoSuchElementException:
        pass

    # 2️⃣ Try fallbacks
    for fb in config.get("fallbacks", []):
        try:
            element = driver.find_element(
                BY_MAP[fb["by"]],
                fb["value"]
            )
            _heal(element_key, fb, yaml_path)
            return element
        except NoSuchElementException:
            continue

    raise Exception(f"[SELF-HEAL FAILED] {element_key}")

def _heal(element_key, new_locator, yaml_path):
    with open(yaml_path, "r") as f:
        data = yaml.safe_load(f)

    data[element_key]["primary"] = new_locator
    data[element_key]["last_healed"] = datetime.datetime.now().isoformat()

    with open(yaml_path, "w") as f:
        yaml.safe_dump(data, f)

    print(f"[SELF-HEAL] Locator updated for {element_key}")

def _find(driver, locator):
    return driver.find_element(
        BY_MAP[locator["by"]],
        locator["value"]
    )

def _heal_locator(element_name, new_locator, yaml_path):
    with open(yaml_path, "r") as f:
        data = yaml.safe_load(f)

    data[element_name]["primary"] = new_locator
    data[element_name]["last_healed"] = datetime.datetime.now().isoformat()

    with open(yaml_path, "w") as f:
        yaml.safe_dump(data, f)

def _heuristic_search(driver, meta):
    if not meta:
        return None

    if meta.get("text"):
        xpath = f"//{meta.get('tag','*')}[normalize-space()='{meta['text']}']"
        try:
            return driver.find_element(By.XPATH, xpath)
        except:
            pass

    return None

def _auto_update_locator(element_name, element, yaml_path):
    locator = {
        "by": "xpath",
        "value": _generate_xpath(element)
    }
    _heal_locator(element_name, locator, yaml_path)

def _generate_xpath(element):
    return f"//{element.tag_name}[normalize-space()='{element.text}']"
