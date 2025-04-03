import time

from playwright.sync_api import expect, Page


def test_UIValidationsDynamicScript(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    #expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    #adding items and verifying if its showing in cart
    iphoneProduct = page.locator("app-card").filter(has_text="iphone X")
    iphoneProduct.get_by_role("button").click()
    nokiaEdge = page.locator("app-card").filter(has_text="Nokia Edge")
    nokiaEdge.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)
    time.sleep(5)

def test_childWindowHandles(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise")
    with page.expect_popup() as newPageInfo:
        page.locator(".blinkingText").click()
        childPage = newPageInfo.value
        text = childPage.locator(".red").text_content()
        print(text)
        #Please email us at mentor@rahulshettyacademy.com with below template to receive response
        words = text.split("at")
        email = words[1].strip().split(" ")[0]
        print("Email")
        print(email)
        assert email == "mentor@rahulshettyacademy.com"
