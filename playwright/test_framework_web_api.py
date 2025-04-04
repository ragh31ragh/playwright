import json
import time

import pytest
from playwright.sync_api import Playwright, expect

from utils.api_base import APIUtils

#json file reading
with open('data/credentials.json') as f:
    test_data = json.load(f)
    print(test_data)
    user_crendentials_list = test_data["user_credentials"]

@pytest.mark.parametrize('user_creds',user_crendentials_list)
def test_e2e_web_api(playwright:Playwright,user_creds):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()



    page.goto("https://rahulshettyacademy.com/client")
    #create order and grab order id

    api_utils = APIUtils()
    orderId = api_utils.createOrder(playwright)

    #login
    page.get_by_placeholder("email@example.com").fill(user_creds["userEmail"])
    page.get_by_placeholder("enter your passsword").fill(user_creds["password"])
    page.get_by_role("button",name="Login").click()
    time.sleep(5)
    page.get_by_role("button",name="ORDERS").click()
    row_item = page.locator("tr").filter(has_text=orderId)
    row_item.get_by_role("button",name="View").click()
    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
    time.sleep(5)


    #orders page . order is present .
    #order history page - order is present
