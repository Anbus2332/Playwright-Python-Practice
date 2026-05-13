import time

from playwright.sync_api import Playwright, expect


def test_alertValidation(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://letcode.in/")
    page.get_by_role("link", name="Work-Space").click()
    page.locator("//a[@href='/alert']").click()

    page.once("dialog", lambda dialog:dialog.accept())
    page.locator("#accept").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.once("dialog", lambda dialog:print(dialog.message))
    page.locator("#confirm").click()

    page.once("dialog", lambda dialog: dialog.accept("Anbu"))
    page.locator("#prompt").click()
    expect(page.locator("#myName")).to_have_text("Your name is: Anbu")
    page.once("dialog", lambda dialog: dialog.accept())
    page.locator("#modern").click()
    expect(page.get_by_text("Modern Alert - Some people address me as sweet alert as well")).to_be_visible()
    page.locator("//button[@aria-label='close']").click()






