import datetime
from time import sleep

from selenium import webdriver
import pytest

@pytest.fixture(scope="class", autouse=True)
def open_tearDown(request):
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://devdreamcity.kolonizer.in/login")
    request.cls.driver = driver
    yield
    sleep(2)
    driver.quit()


@pytest.fixture(scope="function", autouse=True)
def wait(request):
    driver.implicitly_wait(15)


def pytest_html_report_title(report):
    report.title = "CRM"


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        feature_request = item.funcargs['request']
        extra.append(pytest_html.extras.url('http://devdreamcity.kolonizer.in/login'))
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            driver.get_screenshot_as_file('C:\\Users\\Lenovo\\PycharmProjects\\WebAutomation_Python\\Screenshots\\failed.png')
            extra.append(pytest_html.extras.image('C:\\Users\\Lenovo\\PycharmProjects\\WebAutomation_Python\\Screenshots\\failed.png'))
            extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
        report.extra = extra
