import time


def test_BrowserLaunchTest(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.wikipedia.org/")
    time.sleep(2)

def test_2():
    x=5
    y=4
    assert x == y , "x is not equal to y"


