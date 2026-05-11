import logging
import time

from playwright.sync_api import Playwright, expect


def test_inputValidation(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://letcode.in/")
    #Enter your full Name
    # page.locator('//a[@id="testing" and @href="/test"]').click()
    page.get_by_role("link", name="Work-Space").click()

    #performing click opertion input title
    page.locator('//a[@href="/edit"]').click()
    page.locator("#fullName").fill("Anbuselvan M")
    expect(page.locator("#fullName")).to_have_value("Anbuselvan M")
    logging.info("Verified inout title")

#Append a text and press keyboard tab
    page.locator("#join").click()
    time.sleep(1)
    page.locator("#join").press_sequentially(" player")
    expect(page.locator("#join")).to_have_value("I am good player")
    page.keyboard.press("Tab")
    logging.info("Verified Append a text and press keyboard tab")

#What is inside the text box

    text_validation = page.locator("#getMe").input_value()
    print(text_validation)
    # assert text_validation == "Anbuselvan M"
    expect(page.locator("#getMe")).to_have_value("ortonikc")
    logging.info("verified What is inside the text box")

#Clear the text
    page.locator("#clearMe").clear()
    expect(page.locator("#clearMe")).to_have_value("")
    logging.info("verified Clear text")

#Confirm edit field is disabled
    expect(page.locator("#noEdit")).to_be_disabled()
    expect(page.locator("#noEdit")).to_have_attribute("disabled","")
    logging.info("verified edit field is disabled")

#Confirm text is readonly
    page.locator("#dontwrite").is_editable()
    expect(page.locator("#dontwrite")).to_have_attribute("readonly","")
    logging.info("verified text is readonly")