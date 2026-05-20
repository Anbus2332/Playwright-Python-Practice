import time

from playwright.sync_api import Playwright, expect


def test_frameValidation(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://letcode.in/")
    page.get_by_role("link", name="Work-Space").click()
    page.get_by_role("link",name="Inner HTML").click()
    page.wait_for_load_state("load")
    #First Name
    page.frame_locator("#firstFr").get_by_placeholder("Enter name").fill("Anbuselvan")
    expect(page.frame_locator("#firstFr").get_by_placeholder("Enter name")).to_have_value("Anbuselvan")
    #Last Name
    page.frame_locator("#firstFr").locator("//input[@name='lname']").fill("M")
    expect(page.frame_locator("#firstFr").locator("//input[@name='lname']")).to_have_value("M")
    expect(page.frame_locator("#firstFr").get_by_text("You have entered Anbuselvan M")).to_be_visible()
    #Email
    (page.frame_locator("#firstFr").frame_locator("//iframe[@src='innerframe']").locator("//input[@name='email']")
     .fill("anbus@gmail.com"))
    expect(page.frame_locator("#firstFr").frame_locator("//iframe[@src='innerframe']").locator("//input[@name='email']")).to_have_value("anbus@gmail.com")
