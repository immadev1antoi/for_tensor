import os.path
import time

import allure
from tensor_test_task.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



class SbisDownloadPage(BasePage):
    SBIS_PLAGIN_BUTTON = (By.XPATH, "//div[text()='СБИС Плагин']")
    WEB_INSTALLER_DOWNLOAD_LINK = (By.XPATH, "//a[contains(@href, 'sbisplugin-setup-web.exe')]")


    @allure.step('Нажимается кнопка "СБИС Плагин"')
    def click_sbis_plagin_button(self):
        elem = self.wait.until(EC.presence_of_element_located(self.SBIS_PLAGIN_BUTTON))
        self.actions.move_to_element(elem).pause(1).click().perform()



    @allure.step('Нажимается на ссылку для скачивания Web-установщика')
    def click_on_download_web_installer_link(self):
        self.click(self.WEB_INSTALLER_DOWNLOAD_LINK)
        while True:
            if os.path.isfile(f'{os.getcwd()}/sbisplugin-setup-web.exe'):
                break
            else:
                time.sleep(1)

    @allure.step('Проверяется наличие файла {value} в директории')
    def check_file(self, value):
        return os.path.isfile(f'{os.getcwd()}/{value}')


    @allure.step('Возвращается размер файла {value}')
    def file_size(self, value):
        file_size = os.path.getsize(f'{os.getcwd()}/{value}')
        return round(file_size / (1024 ** 2), 2)
