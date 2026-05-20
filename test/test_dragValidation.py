import time

from playwright.sync_api import Playwright, expect


def test_dragValidation(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.wait_for_load_state()
    page.goto("https://letcode.in/")
    page.get_by_role("link", name="Work-Space").click()
    page.locator("//a[@href='/draggable']").click()
    # expect(page.locator("//h1[@class='title has-text-centered is-pulled-left']")).to_have_text("Drag")
    expect(page.locator("//h1[text()='Drag']")).to_have_text("Drag")
    expect(page.locator("#header")).to_contain_text("I can only be dragged within the dotted container")
    sample_box = page.locator("#sample-box")
    box = sample_box.bounding_box()
    start_x = box["x"] + box["width"] / 2
    start_y = box["y"] + box["height"] / 2
    page.mouse.move(start_x, start_y)
    page.mouse.down()
    page.mouse.move(start_x + 300, start_y + 100,steps=25)
    page.mouse.up()
    page.wait_for_timeout(3000)

