from playwright.sync_api import Playwright, expect


def test_advancedtablevalidation(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://letcode.in/")
    page.get_by_role("link", name="Work-Space").click()
    page.locator("//a[@href='/advancedtable']").click()
    # page.locator("//span[text()='UNIVERSITY NAME']").click()
    #
    # #sorting
    # all_values = []
    # while True:
    #     ascending_names = page.locator("//tbody/tr/td[@class='sorting_1']").all_text_contents()
    #     print(ascending_names)
    #     all_values.extend(ascending_names)
    #
    #     next_button = page.locator("//button[@aria-label='Next']")
    #     if next_button.is_disabled():
    #         break
    #
    #     next_button.click()
    #
    #
    # print(all_values)
    #
    #
    # expected_names = sorted(all_values)
    # print(expected_names)
    # assert expected_names == all_values

    # descending order
    page.get_by_text("UNIVERSITY NAME").dblclick()

    descending_values = []
    while True:

        descending_results = page.locator("//tbody/tr/td[@class='sorting_1']").all_text_contents()

        descending_values.extend(descending_results)

        next_icon = page.get_by_role("button", name="Next")
        if next_icon.is_disabled():
            break
        next_icon.click()
        print(descending_values)

        expected_descending_names = sorted(descending_values, reverse=True)
        print(expected_descending_names)
        assert descending_values == expected_descending_names

    # check search is working
    search_values = ["University of Paisley", "https://www.rfhsm.ac.uk/", "32", "89"]
    search_box = page.locator("//input[@type='search']")

    for value in search_values:

        # Enter search value
        search_box.fill(value)

        # Validate entered value
        expect(search_box).to_have_value(value)

        print(f"Search worked for : {value}")

        results = [
            text.strip()
            for text in page.locator("//tbody/tr/td").all_text_contents()
            if text.strip() != ""
        ]

        print(results)

        # Check no records message
        if "No matching records found" in results:

            print(f"No results found for : {value}")

        else:

            matched = False  # initialize variable

            # Validate all rows
            for result in results:

                if value.lower() in result.lower():
                    matched = True
                    break

            assert matched

            print(f"Results validated for : {value}")

        search_box.clear()

        # Check dropdown selection is working fine
        dropdown = page.locator("//select/option[@value='25']")
        options = dropdown.locator("option").all_text_contents()
        print(options)





