import allure
from tensor_test_task.pages.sbis_main_page import SbisMainPage
from tensor_test_task.pages.contacts_page import ContactsPage
from tensor_test_task.pages.tensor_main_page import TensorMainPage
from tensor_test_task.pages.tensor_about_page import TensorAboutPage


@allure.title('Наличие блока "Сила в людях" на главной странице "tensor.ru"')
def test_check_people_power_textblock_on_main_page(browser):
    with allure.step('Перейти на https://sbis.ru/ в раздел "Контакты"'):
        SbisMainPage(browser).click_contacts_button()
    with allure.step('Найти баннер Тензор, кликнуть по нему'):
        ContactsPage(browser).click_on_tensor_image()
    with allure.step('Перейти на https://tensor.ru/'):
        ContactsPage(browser).switch_to_window_number(2)
    with allure.step('Проверить, что есть блок "Сила в людях"'):
        assert TensorMainPage(browser).block_power_in_people_on_page


@allure.title('Нажатие кнопки "Подробнее" в блоке "Сила в людях" на главной странице "tensor.ru"')
def test_click_more_details_on_people_power_textblock(browser):
    with allure.step('Перейти на https://sbis.ru/ в раздел "Контакты"'):
        SbisMainPage(browser).click_contacts_button()
    with allure.step('Найти баннер Тензор, кликнуть по нему'):
        ContactsPage(browser).click_on_tensor_image()
    with allure.step('Перейти на https://tensor.ru/'):
        ContactsPage(browser).switch_to_window_number(2)
    with allure.step('Перейдите в этом блоке в "Подробнее"'):
        TensorMainPage(browser).click_more_detains_on_power_in_people()
    with allure.step('Убедитесь, что открывается https://tensor.ru/about'):
        assert TensorAboutPage(browser).page_opened


@allure.title('Проверка высоты и ширины картинок в блоке "Хронология"')
def test_check_height_and_width_images(browser):
    with allure.step('Перейти на https://sbis.ru/ в раздел "Контакты"'):
        SbisMainPage(browser).click_contacts_button()
    with allure.step('Найти баннер Тензор, кликнуть по нему'):
        ContactsPage(browser).click_on_tensor_image()
    with allure.step('Перейти на https://tensor.ru/'):
        ContactsPage(browser).switch_to_window_number(2)
    with allure.step('Перейдите в этом блоке в "Подробнее"'):
        TensorMainPage(browser).click_more_detains_on_power_in_people()
    with allure.step(
            'Находим раздел Работаем и проверяем,'
            ' что у всех фотографии хронологии одинаковые высота (height) и ширина (width)'):
        assert TensorAboutPage(browser).check_working_block_images_sizes()













