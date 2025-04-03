import time

from playwright.sync_api import Playwright, expect

from utils.api_base import APIUtils


def test_e2e_web_api(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client")
    #create order and grab order id

    api_utils = APIUtils()
    orderId = api_utils.createOrder(playwright)

    #login
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.get_by_role("button",name="Login").click()
    time.sleep(5)
    page.get_by_role("button",name="ORDERS").click()
    row_item = page.locator("tr").filter(has_text=orderId)
    row_item.get_by_role("button",name="View").click()
    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
    time.sleep(5)


    #orders page . order is present .
    #order history page - order is present
