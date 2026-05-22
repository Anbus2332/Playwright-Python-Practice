from playwright.sync_api import Playwright


def test_sliderValidation(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.wait_for_load_state()
    page.goto("https://letcode.in/")
    page.get_by_role("link", name="Work-Space").click()
    page.locator("//a[@href='/slider']").click()
    # Multiple slider values
    slider_values = [2, 20, 30, 50]

    for value in slider_values:
        print("Testing Slider Value:", value)

        # Move slider
        page.locator("#generate").fill(str(value))
    page.get_by_role("button",name="Get Countries").click()
    page.wait_for_timeout(2000)
    countries = page.locator("//p[@class='has-text-primary-light']").text_content()
    print(countries)

    # Split countries dynamically
    country_list = countries.split(" - ")

    # Count countries
    actual_count = len(country_list)

    print("Country Count:", actual_count)

    # Validation
    assert actual_count == 50
    page.wait_for_timeout(3000)

    browser.close()
