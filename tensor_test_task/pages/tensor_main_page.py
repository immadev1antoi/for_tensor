import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from tensor_test_task.pages.base_page import  BasePage




class TensorMainPage(BasePage):
    POWER_IN_PEOPLE_TEXT_BLOCK = (By.XPATH, "//p[text()='Сила в людях']")
    DETAILS_BUTTON_ON_POWER_IN_PEOPLE_TEXT_BLOCK = (By.XPATH,
                                                   "//div[starts-with(@class, 'tensor_ru-Index__block4')]//a[text("
                                                   ")='Подробнее']")
    NEWS_BLOCK = (By.XPATH, "//div[text()='Новости']")




    @allure.step('Нажимается кнопка "Подробнее" в блоке "Сила в людях"')
    def click_more_detains_on_power_in_people(self):
        news = self.wait.until(EC.presence_of_element_located(self.NEWS_BLOCK))
        self.actions.move_to_element(news).perform()
        self.click(self.DETAILS_BUTTON_ON_POWER_IN_PEOPLE_TEXT_BLOCK)

    @property
    @allure.step('Проверяется наличие на странице блока "Сила в людях"')
    def block_power_in_people_on_page(self):
        try:
            self.wait.until(EC.presence_of_element_located(self.POWER_IN_PEOPLE_TEXT_BLOCK))
            return True
        except TimeoutException:
            return False