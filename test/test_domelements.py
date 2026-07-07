from playwright.sync_api import Playwright, expect


def test_domelements(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://letcode.in/")
    page.get_by_role("link", name="Work-Space").click()
    page.locator("//a[@href='/shadow']").click()

    page.locator("#fname").fill("Anbuselvan")
    expect(page.locator("#fname")).to_have_value("Anbuselvan")
    expect(page.get_by_text("Enter your first name")).to_be_visible()
