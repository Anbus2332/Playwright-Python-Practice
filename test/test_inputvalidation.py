from playwright.sync_api import Playwright


def test_inputValidation(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://letcode.in/")
    page.get_by_test_id("testing").click()
    page.get_by_label("edit").click()
