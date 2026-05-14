import time

from playwright.sync_api import Playwright, expect


def test_radioValidation(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://letcode.in/")
    page.get_by_role("link", name="Work-Space").click()

    page.get_by_role("link",name="Tabs").click()
    with page.expect_popup() as popup_info:
        page.locator("#home").click()
    new_window = popup_info.value
    expect(new_window).to_have_url("https://letcode.in/test")
    print(new_window.title())
    page.close()
    new_window.close()


    #multiple window Handling:
    page2 = context.new_page()
    page2.goto("https://letcode.in/window")
    with page2.expect_popup() as all_pages:
        page2.locator("#multi").click()
    all_pages = context.pages
    for p in all_pages:
        print("childWindows:", p.title())
        print(len(context.pages))
        p.close()
    browser.close()


