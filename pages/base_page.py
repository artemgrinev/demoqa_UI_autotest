from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):  # Если необходимо чтобы элемент был видимым
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def element_are_visible(self, locator, timeout=5):  # Если необходимо чтобы все элементы были видимыми
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=5):  # Если необходимо проверить присутствия элемента в DOM.
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def element_are_present(self, locator, timeout=5):  # Если необходимо проверить присутствия элементов в DOM.
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def go_to_element(self, element):  # проскролить к искомому элементу
        self.driver.execute_script("arguments[0].scrollIntoView();", element)