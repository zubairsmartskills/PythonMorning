import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser=='edge':
        driver= webdriver.Edge()
    elif browser=='chrome':
        driver=webdriver.Chrome()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

def pytest_metadata(metadata):
    metadata["Project Name"]='Fb'
    metadata["window"]="10"



