import os
import time

import requests

import pytest
import datetime
import logging
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.firefox.options import Options as FFOptions



@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.outcome != 'passed':
        item.status = 'failed'
    else:
        item.status = 'passed'


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default="https://sbis.ru/")
    parser.addoption("--log_level", action="store", default="INFO")



@pytest.fixture()
def set_logging(request):

    '''Создание экземпляра logger'''

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(
        filename=f"{os.getcwd()}/logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=request.config.getoption("--log_level"))
    return logger


@pytest.fixture()
def browser(request, set_logging):

    '''Создание экземпляра драйвера'''

    browser_name = request.config.getoption("--browser")
    url = request.config.getoption("--url")

    set_logging.info("===> Test %s started at %s" % (request.node.name, datetime.datetime.now()))

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless=new')
        prefs = {
            "download.default_directory" : f'{os.getcwd()}'
        }
        options.add_experimental_option("prefs", prefs)

        driver = webdriver.Chrome(service=ChromiumService(), options=options)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(options=FFOptions(), service=FFService())
    else:
        driver = webdriver.Safari()

    driver.maximize_window()

    driver.logger = set_logging

    driver.get(url)

    yield driver

    if request.node.status == "failed":
            allure.attach(
                name="failure_screenshot",
                body=driver.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG)

    driver.quit()

    set_logging.info("===> Test %s finished at %s" % (request.node.name, datetime.datetime.now()))





