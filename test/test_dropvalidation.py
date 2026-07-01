from playwright.sync_api import Playwright


def test_dropValidation(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.wait_for_load_state()
    page.goto("https://letcode.in/")
    page.get_by_role("link", name="Work-Space").click()
    page.locator("//a[@href='/droppable']").click()
    source_element = page.locator("#draggable")
    target_element = page.locator("#droppable")

    box1 = source_element.bounding_box()
    box2 = target_element.bounding_box()

    x1 = (box1["x"] + box1["width"] / 2)
    y1 = (box1["y"] + box1["height"] / 2)
    x2 = (box2["x"] + box2["width"] / 2)
    y2 = (box2["y"] + box2["height"] / 2)
    source_element.hover()
    page.mouse.move(x1,y1)
    page.mouse.down()
    page.mouse.move(x2, y2,steps=30)
    page.mouse.up()
    page.wait_for_timeout(3000)

