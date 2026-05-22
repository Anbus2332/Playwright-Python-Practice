from playwright.sync_api import Playwright


def test_waitValidation(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.wait_for_load_state()
    page.goto("https://letcode.in/")
    page.get_by_role("link", name="Work-Space").click()
    page.locator("//a[@href='/waits']").click()
    page.locator("#accept").click()
    dialog = page.wait_for_event("dialog")
    print(dialog.message)
