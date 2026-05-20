
from playwright.sync_api import Playwright, expect


def test_sortValidation(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.wait_for_load_state()
    page.goto("https://letcode.in/")
    page.get_by_role("link", name="Work-Space").click()
    page.locator("//a[@href='/selectable']").click()
    expect(page.locator("//h1[text()='Selectable']")).to_have_text("Selectable")
    select = page.locator("//label[@class='label']/following-sibling::div/div/div")
    count = select.count()
    print(count)
    for i in range(count):
        selected_item = select.nth(i)
        selected_item.click()
        print(selected_item.text_content())
        page.wait_for_timeout(2000)
    page.wait_for_timeout(2000)
    browser.close()
