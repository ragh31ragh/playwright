import json
import time

import pytest
from playwright.sync_api import Playwright, expect

from PageObjects.login import LoginPage
from utils.api_base2 import APIUtils2

#json file reading
with open('data/credentials.json') as f:
    test_data = json.load(f)
    print(test_data)
    user_crendentials_list = test_data["user_credentials"]





@pytest.mark.parametrize('user_creds',user_crendentials_list)
def test_e2e_web_api(playwright:Playwright,user_creds):
    userEmail = user_creds["userEmail"]
    userPassword =  user_creds["password"]
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()



    #create order and grab order id

    api_utils = APIUtils2()
    orderId = api_utils.createOrder(playwright,user_creds)

    #login
    loginPage = LoginPage(page)
    loginPage.navigate()
    print("############Navigated to Login Page##########")

    dashboardPage = loginPage.login(userEmail,userPassword )

    time.sleep(5)
    print("############post sleep 5 seconds##########")
    #oder Navigation
    ordersHistoryPage =dashboardPage.seletOrderNavigationLink()
    orderDetails = ordersHistoryPage.selectOrder(orderId)
    orderDetails.verifyOrderMessage()
    time.sleep(5)


    #orders page . order is present .
    #order history page - order is present
