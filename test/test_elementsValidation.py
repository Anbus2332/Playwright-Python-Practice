
from playwright.sync_api import Playwright, expect


def test_elementsValidation(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.wait_for_load_state()
    page.goto("https://letcode.in/")
    page.get_by_role("link", name="Work-Space").click()
    page.get_by_text(" Find Elements ").click()
    page.locator("//input[@type='text']").fill("anbus2332")
    page.locator("#search").click()
    # profile_picture = page.locator(".media img")
    # expect(profile_picture).to_be_visible()
    page.wait_for_load_state()
    expect(page.get_by_text("Anbuselvan M")).to_have_text("Anbuselvan M")
    count_of_repositories = int(page.locator("//p[text()='Public Repos']/following-sibling::p").text_content())
    print( count_of_repositories)
        # Get repo count from UI
    actual_count = page.locator("//article").count()
    # Assertion
    assert actual_count == count_of_repositories
    browser.close()



