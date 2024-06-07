from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
import allure


class BasePage:
   def __init__(self, browser):
            self.browser = browser
            self.actions = ActionChains(browser)
            self.wait = WebDriverWait(browser, 5)


   @allure.step('Переключается на окно номер {value}')
   def switch_to_window_number(self, value):
        windows = self.browser.window_handles
        self.browser.switch_to.window(windows[value - 1])


   def click(self, locator):
       elem = self.wait.until(EC.element_to_be_clickable(locator))
       try:
           elem.click()
       except StaleElementReferenceException:
           elem = self.wait.until(EC.element_to_be_clickable(locator))
           elem.click()
       except ElementNotInteractableException:
           self.actions.move_to_element(elem)
           self.actions.click().perform()


   @allure.step('Проверяется, что URL страницы содержит {value}')
   def check_url_contains(self, value):
       try:
           self.wait.until(EC.url_contains(value))
           return True
       except TimeoutException:
           return False

   @allure.step('Проверяется, что Title страницы содержит {value}')
   def check_title_contains(self, value):
       try:
           self.wait.until(EC.title_contains(value))
           return True
       except TimeoutException:
           return False


