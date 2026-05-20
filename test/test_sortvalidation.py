from playwright.sync_api import Playwright


def test_sortValidation(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.wait_for_load_state()
    page.goto("https://letcode.in/")
    page.get_by_role("link", name="Work-Space").click()
    page.locator("//a[@href='/sortable']").click()

    todo_list = page.locator('//h2[text()="To do"]/following-sibling::div/div')
    done_list = page.locator('//h2[text()="Done"]/following-sibling::div')

    todo_count = todo_list.count()
    print(todo_count)

    for i in range(todo_count):
        # Always select first remaining item
        item = todo_list.nth(0)

        # Source coordinates
        source_box = item.bounding_box()

        # Target coordinates
        target_box = done_list.bounding_box()

        # Move mouse to source
        page.mouse.move(
            source_box["x"] + source_box["width"] / 2,
            source_box["y"] + source_box["height"] / 2
        )

        # Hold item
        page.mouse.down()

        # Drag slowly to DONE section
        page.mouse.move(
            target_box["x"] + 150,
            target_box["y"] + 150,
            steps=50
        )

        # Release item
        page.mouse.up()

        page.wait_for_timeout(2000)

    page.wait_for_timeout(5000)

    browser.close()

