from playwright.sync_api import expect, Playwright


def test_radioValidation(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://letcode.in/")
    page.get_by_role("link", name="Work-Space").click()
    #Select any one
    page.locator("//a[@href='/radio']").click()
    page.locator("#yes").check()
    expect(page.locator("#yes")).to_be_checked()
    #Cofirm you can select only one radio button
    page.locator("#two").check()
    expect(page.locator("#two")).to_be_checked()
    expect(page.locator("#one")).not_to_be_checked()
    #Find the bug
    radio1 = page.locator("#nobug")
    radio1.check()
    radio2 = page.locator("#bug")
    radio2.check()
    if radio1.is_checked() and radio2.is_checked():
        print("Bug is found as both the radio buttons are selected")
    else:
        print("Bug is not found")

    #Find which one is selected
    radio3 = page.locator("#foo")
    radio4 = page.locator("#notfoo")
    if radio3.is_checked():
        print("Foo is selected")
    if radio4.is_checked():
        print("Bar is selected")
    else:
        print("Both the radio buttons are not selected")
    #Confirm last field is disabled
    lastField = page.locator("#maybe")
    if lastField.is_disabled():
        print("The last field is disabled")
    else:
        print("The last filed is enabled")
    #Find the checkbox is selected
    checkbox = page.get_by_text("Remember me")
    if checkbox.is_checked():
        print("checkbox is selected")
    else:
        print("checkbox is not selected")
    #Accept the T&C:
    checkbox2 = page.get_by_text("I agree to the")
    checkbox2.check()
    if checkbox2.is_checked():
        print("Check box is accepting the terms and conditions")
    else:
        print("Check box is not accepted")






