from playwright.sync_api import Playwright, expect


def test_waitValidation(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.wait_for_load_state()
    page.goto("https://letcode.in/")
    page.get_by_role("link", name="Work-Space").click()

    #Add all the prices and check if the total is correct
    page.locator("//a[@href='/table']").click()
    prices = page.locator("//table[@id='shopping']//tbody/tr/td[2]").all_inner_texts()
    total = 0
    for price in prices:
        total += int(price)

    print(price)

    defined_total = page.locator("//tfoot/td[2]").text_content()
    defined_total = int(defined_total)
    print(defined_total)

    assert total == defined_total
    print("Total is matching")



    #Mark Raj as present
    check_box2 = page.locator("//table[@id='simpletable']//input[@class='qe']")
    check_box2.click()
    expect(check_box2).to_be_checked()
    check_box1 = page.locator("//table[@id='simpletable']//input[@class='q']")
    expect(check_box1).not_to_be_checked()
    check_box3 = page.locator("//table[@id='simpletable']//input[@class='qd']")
    expect(check_box3).not_to_be_checked()

    page.get_by_role("columnheader", name="Dessert (100g)").click()
    names = page.locator("//tr[@class='ng-star-inserted']//td[1]").all_text_contents()
    print(names)
    expected_names = sorted(names)
    assert expected_names == names
    print(expected_names)