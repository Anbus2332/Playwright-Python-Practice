from playwright.sync_api import Playwright


def test_inputValidation(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://letcode.in/")
    page.get_by_role("link", name="Work-Space").click()

#Goto Home and come back here using driver commanda
    page.locator('//a[@href="/button"]').click()
    page.locator("#home").click()
    page.go_back()

#Get the X & Y co-ordinates
    # page.get


