from playwright.sync_api import Playwright, expect


def test_formsvalidation(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://letcode.in/")
    page.get_by_role("link", name="Work-Space").click()
    page.locator("//a[@href='/forms']").click()
    page.locator("#firstname").fill("Anbu")
    expect(page.locator("#firstname")).to_have_value("Anbu")
    page.locator("#lasttname").fill("M")
    expect(page.locator("#lasttname")).to_have_value("M")
    page.locator("#email").fill("anbu@gmail.com")
    expect(page.locator("#email")).to_have_value("anbu@gmail.com")
    page.get_by_role("combobox").first.select_option("India (+91)")
    expect(page.get_by_role("combobox").first).to_have_value("91")
    page.locator("#Phno").fill("2456987456")
    expect(page.locator("#Phno")).to_have_value("2456987456")
    page.locator("#Addl1").fill("2/565,london pet")
    expect(page.locator("#Addl1")).to_have_value("2/565,london pet")
    page.locator("#Addl2").fill("kaveripattinam")
    expect(page.locator("#Addl2")).to_have_value("kaveripattinam")
    page.locator("#state").fill("Tamilnadu")
    expect(page.locator("#state")).to_have_value("Tamilnadu")
    page.locator("#postalcode").fill("6351001")
    expect(page.locator("#postalcode")).to_have_value("6351001")
    page.get_by_role("combobox").nth(1).select_option("India")
    expect(page.get_by_role("combobox").nth(1)).to_have_value("India")
    page.locator("#Date").fill("1994-06-10")
    expect(page.locator("#Date")).to_have_value("1994-06-10")
    page.locator("#male").check()
    expect(page.locator("#male")).to_be_checked()
    page.locator("//input[@type='checkbox']").click()
    expect(page.locator("//input[@type='checkbox']")).to_be_checked()
    page.locator("//input[@type='submit']").click()




