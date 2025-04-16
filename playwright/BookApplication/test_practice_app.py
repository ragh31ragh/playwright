import json
import time

import pytest
from playwright.sync_api import Playwright
from pytest_playwright.pytest_playwright import page

from APIUtilities import apiUtilities
from login import LoginPage
from dashboardPage import DashboardPage
from orderHistoryPage import OrdersHistoryPage
from OrderDetails import OrderDetails

'''
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Browser selection"
    )


@pytest.fixture(scope="session")
def user_creds(request):
    return request.param

@pytest.fixture
def browserInstance(playwright,request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        browser = playwright.chromium.launch(headless=False)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()
'''
with open('credentials.json') as f:
    test_data = json.load(f)
    user_credentials_list = test_data["user_credentials"]

@pytest.mark.parametrize('user_creds',user_credentials_list)
def test_webFrameworkApp(playwright :Playwright ,user_creds):
    user_email  = user_creds["userEmail"]
    user_password = user_creds["password"]
    #print(user_email)
    #print(user_password)

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    api_Utilities =apiUtilities()
    orderId = api_Utilities.createOrder(playwright,user_creds)
    print("orderID")
    print(orderId)
    #loginPage =  LoginPage(browserInstance)
    loginPage = LoginPage(page)
    loginPage.Navigate()
    #loginPage.Navigate()
    loginPage.Login(user_email, user_password)
    time.sleep(5)
    print("############post sleep 5 seconds##########")
    dashBoard = DashboardPage(page)
    dashBoard.selectOrderNavigationLink()
    orderHistoryPage = OrdersHistoryPage(page)
    orderHistoryPage.selectOrder(orderId)
    orderDetails=OrderDetails(page)
    orderDetails.verifyOrderMessage()
    time.sleep(5)
    print("############post sleep 5 seconds---Test Completed##########")
