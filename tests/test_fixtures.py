"""
Сделайте разные фикстуры для каждого теста
"""

import pytest
from selene.support.shared import browser
from selene import have


@pytest.fixture(scope='function')
def desktop_fixture():
    browser.config.window_height = 1080
    browser.config.window_width = 1920


@pytest.fixture(scope='function')
def mobile_fixture():
    browser.config.window_height = 800
    browser.config.window_width = 900


def test_github_desktop(desktop_fixture):
    browser.open('https://github.com')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))


def test_github_mobile():
    browser.open('https://github.com')
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))