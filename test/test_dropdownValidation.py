import time

from playwright.sync_api import Playwright, expect


def test_inputValidation(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://letcode.in/")
    page.get_by_role("link", name="Work-Space").click()
    page.locator("//a[@href='/dropdowns']").click()

    # Select the apple using visible text
    dropdown = page.locator("//select[@id='fruits']")
    dropdown.select_option(label="Apple")
    expect(dropdown.locator("option:checked")).to_have_text("Apple")
    expect(page.get_by_text("You have selected Apple")).to_be_visible()

    # Select your super hero's
    dropdown = page.locator("#superheros")
    dropdown.select_option(label=["Wonder Woman", "Wolverine", "Thor"])
    expect(dropdown.locator("option:checked")).to_have_text(["Thor", "Wolverine", "Wonder Woman"])
    expect(page.get_by_text("You have selected Thor")).to_be_visible()

    #Select the last programming language and print all the options
    dropdown = page.locator("#lang")
    options = dropdown.locator("option").all_text_contents()
    print(options)
    print(dropdown.select_option(index=len(options)-1))
    expect(dropdown.locator("option:checked")).to_have_text(options[-1])

    dropdown = page.locator("#country")
    dropdown.select_option(value="Colombia")
    print(dropdown.locator("option:checked").text_content())
    expect(dropdown.locator("option:checked")).to_have_text("Colombia")


