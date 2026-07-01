from playwright.sync_api import Playwright, expect


def test_calendartablevalidation(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://letcode.in/")
    page.get_by_role("link", name="Work-Space").click()
    page.locator("//a[@href='/calendar']").click()
    page.wait_for_load_state("domcontentloaded")
    date_input = page.locator("#birthday")
    date_input.wait_for()
    date_input.fill("1994-06-10")


    expect(page.locator("//p[text()='1994-06-10']")).to_have_text("1994-06-10")
