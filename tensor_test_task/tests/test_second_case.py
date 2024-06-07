import allure
from tensor_test_task.pages.sbis_main_page import SbisMainPage
from tensor_test_task.pages.contacts_page import ContactsPage


@allure.title('Определение региона на странице "Контакты"')
def test_check_region(browser):
    with allure.step('Перейти на https://sbis.ru/ в раздел "Контакты"'):
        SbisMainPage(browser).click_contacts_button()
    with allure.step('Проверить, что определился ваш регион'):
        assert ContactsPage(browser).check_located_region('Республика Башкортостан')


@allure.title('Отображение списка партнеров на странице "Контакты"')
def test_check_partners_list_opened(browser):
    with allure.step('Перейти на https://sbis.ru/ в раздел "Контакты"'):
        SbisMainPage(browser).click_contacts_button()
    with allure.step('Проверить, что отображается список партнеров'):
        assert ContactsPage(browser).partners_list_located


@allure.title('Отображение региона после изменения на странице "Контакты"')
def test_check_region_after_change(browser):
    with allure.step('Перейти на https://sbis.ru/ в раздел "Контакты"'):
        SbisMainPage(browser).click_contacts_button()
    with allure.step('Нажать на определившийся регион'):
        ContactsPage(browser).click_on_located_region()
    with allure.step('Выбрать из списка "41 Камчатский край"'):
        ContactsPage(browser).select_kamchatskiy_kray_in_regions()
    with allure.step('Проверить, что подставился выбранный регион'):
        assert ContactsPage(browser).check_located_region('Камчатский край')

@allure.title('Отображение региона в списке партнеров после изменения на странице "Контакты"')
def test_check_region_in_partners_after_change(browser):
    with allure.step('Перейти на https://sbis.ru/ в раздел "Контакты"'):
        SbisMainPage(browser).click_contacts_button()
    with allure.step('Нажать на определившийся регион'):
        ContactsPage(browser).click_on_located_region()
    with allure.step('Выбрать из списка "41 Камчатский край"'):
        ContactsPage(browser).select_kamchatskiy_kray_in_regions()
    with allure.step('Проверить, что список партнеров изменился'):
        ContactsPage(browser).check_region_in_partners('Петропавловск-Камчатский')


@allure.title('После изменения региона URl страницы содержит информацию о выбранном регионе')
def test_check_url_contains_after_change(browser):
    with allure.step('Перейти на https://sbis.ru/ в раздел "Контакты"'):
        SbisMainPage(browser).click_contacts_button()
    with allure.step('Нажать на определившийся регион'):
        ContactsPage(browser).click_on_located_region()
    with allure.step('Выбрать из списка "41 Камчатский край"'):
        ContactsPage(browser).select_kamchatskiy_kray_in_regions()
    with allure.step('Проверить, что url содержит информацию выбранного региона'):
        ContactsPage(browser).check_url_contains('41-kamchatskij-kraj')

@allure.title('После изменения региона Title страницы содержит информацию о выбранном регионе')
def test_check_title_contains_after_change(browser):
    with allure.step('Перейти на https://sbis.ru/ в раздел "Контакты"'):
        SbisMainPage(browser).click_contacts_button()
    with allure.step('Нажать на определившийся регион'):
        ContactsPage(browser).click_on_located_region()
    with allure.step('Выбрать из списка "41 Камчатский край"'):
        ContactsPage(browser).select_kamchatskiy_kray_in_regions()
    with allure.step('Проверить, что Title содержит информацию выбранного региона'):
        ContactsPage(browser).check_title_contains('Камчатский край')

