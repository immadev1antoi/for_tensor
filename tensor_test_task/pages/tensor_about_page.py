import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from tensor_test_task.pages.base_page import  BasePage




class TensorAboutPage(BasePage):
    WORKING_BLOCK_IMAGES = (By.XPATH, "//a[@class='tensor_ru-About__block3-link']//img")


    @allure.step('Проверяется, одинаковая ли высота и ширина картинок в блоке "Работаем"')
    def check_working_block_images_sizes(self):
        images = self.wait.until(EC.presence_of_all_elements_located(self.WORKING_BLOCK_IMAGES))
        height = {img.get_attribute('height') for img in images}
        width = {img.get_attribute('width') for img in images}
        return len(height) == 1 and len(width) == 1


    @property
    @allure.step('Проверяется, что страница открылась')
    def page_opened(self):
        try:
            self.wait.until(EC.url_to_be('https://tensor.ru/about'))
            return True
        except TimeoutException:
            return None