import time


from playwright.sync_api import Page, expect


def test_UIChecks(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button",name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()
    time.sleep(2)

    #Alert Handling
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button",name="Confirm")
    time.sleep(2)

    #Mouse Hover
    page.locator("#mousehover").hover()
    page.get_by_role("link",name="Top").click()


# identify price column
# identify rice column
# extract the price
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    page.locator("th")
    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count() > 0 :
            colValue = index
            print(f"Price column value{colValue}")
            break
    riceRow = page.locator("tr").filter(has_text="Rice")
    expect(riceRow.locator("td").nth(colValue)).to_contain_text("39")