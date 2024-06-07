import allure
from tensor_test_task.pages.sbis_main_page import SbisMainPage
from tensor_test_task.pages.sbis_download_page import SbisDownloadPage



@allure.title('Загрузка СБИС Плагина')
def test_download_web_installer_sbis_plagin(browser):
    with allure.step('Нажать на кнопку "Скачать локальные версии"'):
        SbisMainPage(browser).click_download_local_versions()
    with allure.step('Нажать на кнопку "СБИС Плагин"'):
        SbisDownloadPage(browser).click_sbis_plagin_button()
    with allure.step('Скачать СБИС Плагин для вашей для windows, веб-установщик в папку с данным тестом'):
        SbisDownloadPage(browser).click_on_download_web_installer_link()
    with allure.step('Убедиться, что плагин скачался'):
        assert SbisDownloadPage(browser).check_file('sbisplugin-setup-web.exe')


@allure.title('Проверка размера скачанного файла')
def test_check_size_downloaded_file(browser):
    with allure.step('Нажать на кнопку "Скачать локальные версии"'):
        SbisMainPage(browser).click_download_local_versions()
    with allure.step('Нажать на кнопку "СБИС Плагин"'):
        SbisDownloadPage(browser).click_sbis_plagin_button()
    with allure.step('Скачать СБИС Плагин для вашей для windows, веб-установщик в папку с данным тестом'):
        SbisDownloadPage(browser).click_on_download_web_installer_link()
    with allure.step('Сравнить размер скачанного файла в мегабайтах. Он должен совпадать с указанным на сайте'):
        assert SbisDownloadPage(browser).file_size('sbisplugin-setup-web.exe') == 7.22



