import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from tensor_test_task.pages.base_page import  BasePage




class SbisMainPage(BasePage):
    CONTACTS_BUTTON = (By.LINK_TEXT, 'Контакты')
    DOWNLOAD_LOCAL_VERSIONS = (By.XPATH, "//a[text()='Скачать локальные версии']")


    @allure.step('Нажимается кнопка "Скачать локальные версии"')
    def click_download_local_versions(self):
        elem = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='sbis_ru-CookieAgreement__close']")))
        elem.click()
        self.click(self.DOWNLOAD_LOCAL_VERSIONS)


    @allure.step('Нажимается кнопка "Контакты"')
    def click_contacts_button(self):
        self.click(self.CONTACTS_BUTTON)

