import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from tensor_test_task.pages.base_page import  BasePage




class ContactsPage(BasePage):
    TENSOR_IMAGE = (By.XPATH, "//div[starts-with(@class, 'sbisru-Contacts__border')]//img")
    REGION_TEXT = (By.XPATH, "//span[@class='sbis_ru-Region-Chooser ml-16 ml-xm-0']/span")
    PARTNERS_LIST = (By.XPATH, "//div[@class='sbisru-Contacts-List__col ws-flex-shrink-1 ws-flex-grow-1']")
    KAMCHATSKIY_KRAY_IN_REGIONS = (By.XPATH, "//span[text()='41 Камчатский край']")
    REGION_IN_PARTNERS_LIST = (By.XPATH, "//div[@id='city-id-2']")

    @allure.step('Нажимается на надпись определившегося региона')
    def click_on_located_region(self):
        self.click(self.REGION_TEXT)


    @allure.step('В списке регионов выбирается "41 Камчатский край"')
    def select_kamchatskiy_kray_in_regions(self):
        self.click(self.KAMCHATSKIY_KRAY_IN_REGIONS)

    @property
    @allure.step('Проверяется, отображается ли список партнеров')
    def partners_list_located(self):
        try:
            self.wait.until(EC.presence_of_element_located(self.PARTNERS_LIST))
            return True
        except TimeoutException:
            return False


    @allure.step('Проверяется значение региона значению {value}')
    def check_located_region(self, value):
        try:
            self.wait.until(EC.text_to_be_present_in_element(self.REGION_TEXT, value))
            return True
        except TimeoutException:
            return False

    @allure.step('Проверяется значение региона в списке партнеров значению {value}')
    def check_region_in_partners(self, value):
        try:
            self.wait.until(EC.text_to_be_present_in_element(self.REGION_IN_PARTNERS_LIST, value))
            return True
        except TimeoutException:
            return False


    @allure.step('Нажимается на изображение "Тензор"')
    def click_on_tensor_image(self):
        self.click(self.TENSOR_IMAGE)

