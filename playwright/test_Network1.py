import time

from playwright.sync_api import Playwright, Page

fakePayloadOrderResponse = {"data": [], "message": "No Orders"}


def intercept_response(route):
    route.fulfill(
        json=fakePayloadOrderResponse
    )
    print ( " In intercept_response function ")


def test_Network(page: Page):
    page.goto("https://rahulshettyacademy.com/client")
    #page.route("https://rahulshettyacademy.com/api/ecom/user/get-cart-count/*", intercept_response)
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    # login
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.get_by_role("button", name="Login").click()
    time.sleep(5)
    page.get_by_role("button", name="ORDERS").click()
    order_text = page.locator(".mt-4").text_content()
    print("##########order_text")
    print(order_text)
