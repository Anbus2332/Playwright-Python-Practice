from playwright.sync_api import Playwright, expect


def test_inputValidation(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://letcode.in/")
    page.get_by_role("link", name="Work-Space").click()

    # Goto Home and come back here using driver commanda
    page.locator('//a[@href="/button"]').click()
    page.locator("#home").click()
    page.go_back()
    # expect(page).to_have_url("https://letcode.in/button")
    # expect(page).to_have_title("Buttons | LetCode with Koushik")
    expect(page.get_by_label("Button")).to_be_visible()

    # Get the X & Y co-ordinates
    button = page.locator("#position")
    box = button.bounding_box()
    print(("X coordinate:", box["x"]))
    print(("Y coordinate:", box["y"]))
    assert box is not None
    assert box["x"] > 0
    assert box["y"] > 0

    # Find the color of the button
    button = page.locator("#color")
    color = button.evaluate("element => getComputedStyle(element).backgroundColor")
    print(color)
    assert color == "rgb(42, 157, 144)"

    # Find the height & width of the button
    heightButton = page.locator("#property")
    box = heightButton.bounding_box()
    print("Width:", box["width"])
    print("Height:", box["height"])
    assert box is not None
    assert box["width"] > 0
    assert box["height"] > 0

    #Confirm button is disabled
    expect(page.get_by_role("button", name="Disabled")).to_be_disabled()

    #Click and Hold Button
    hold = page.get_by_text("Button Hold!")
    hold.hover()
    page.mouse.down()
    page.wait_for_timeout(3000)
    page.mouse.up()
    expect(page.get_by_text("Button has been long pressed")).to_have_text("Button has been long pressed")