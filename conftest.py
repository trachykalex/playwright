import logging
import os
import json
import pytest
from setings import *
from pytest import fixture
import playwright.sync_api
import page_object.application

@fixture(autouse=True, scope='session')
def precondition():
    logging.info('preconditions started')
    yield
    logging.info('postconditions started')

@fixture(scope='session')
def get_playwright():
    with synk_playwright() as playwright:
        yield playwright

@fixture(scope='session', params=['chromium'])
def get_browser(get_playwright, request):
    browser = request.param
    os.environ['PWBROWSER'] = browser
    headless = request.config.getoption('headless')
    if headless == True:
        headless = True
    else:
        headless = False

    if browser == 'chromium':
        bro = get_playwright.chromium.launch(headless=headless)
    elif browser == 'firefix':
        bro = get_playwright.firefix.launch(headless=headless)
    elif browser == 'webkit':
        bro = get_playwright.webkit.launch(headless=headless)
    else:
        assert False, 'unsupported browser type'

    yield bro
    bro.closed()
    del os.environ['PWBROWSER']



@fixture(scope='session')
def desktop_app(get_browser, request):
    base_url = request.config.getoption('base_url')
    app = page_object.application.App(get_browser, base_url=base_url, **BROWSER_OPTIONS)
    app.goto('/')
    yield app
    app.close()

@fixture(scope='session')
def desktop_app_auth(desktop_app, request):
    secure = request.config.getoption('--secure')
    config = load_config(secure)
    app = desktop_app
    app.goto('/login')
    app.login(**config)
    yield app
    
@fixture(scope='session', params=['iPhone 11', 'Pixel 2'])
def mobile_app(get_playwright, get_browser, request):
    if os.environ.get('PWBROWSER') == 'firefox':
        pytest.skip()
    base_url = request.config.getoption('base_url')
    device = request.param
    device_config = get_playwright.devices.get(device)
    if device_config is not None:
        device_config.update(BROWSER_OPTIONS)
    else:
        device_config = BROWSER_OPTIONS
    app = page_object.application.App(get_playwright, base_url=base_url, **BROWSER_OPTIONS)
    app.goto('/')
    yield app
    app.close()

@fixture(scope='session')
def mobile_app_auth(mobile_app, request):
    secure = request.config.getoption('--secure')
    config = load_config(secure)
    app = mobile_app
    app.goto('/login')
    app.login(**config)
    yield app

def pytest_addoption(parser):
    parser.addoption('--secure', action='store', default='secure.json')
    parser.addoption('--device', action='store', default='')
    parser.addoption('--browser', action='store', default='chromium')
    parser.addini('base_url', help='base url site under test', default='http://127.0.0.0:8000')
    parser.addini('headless', help='run browser in headless mode', default=True)