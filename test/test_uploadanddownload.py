from playwright.sync_api import Playwright, expect


def test_uploadanddownload(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://letcode.in/")
    page.get_by_role("link", name="Work-Space").click()
    page.locator("//a[@href='/file']").click()
    expect(page.get_by_role("heading", name="Upload and Download")).to_be_visible()

    # File Upload Scenario:
    file_upload = page.locator("//span[text()='Choose a file…']")
    file_path = "downloads/sample.xlsx"
    file_upload.set_input_files(file_path)
    expect(page.get_by_text("Selected File: sample.xlsx")).to_be_visible()

    # File Download:
    file_excel = page.locator("#xls")
    file_pdf = page.locator("#pdf")
    file_text = page.locator("#txt")

    # Excel validation
    with page.expect_download() as download_info:
        file_excel.click()
        file_excel = download_info.value
        assert file_excel.suggested_filename == "sample.xlsx"
        file_excel.save_as("downloads/sample.xlsx")

    # PDF validation
    with page.expect_download() as download_info:
        file_pdf.click()
        file_pdf = download_info.value
        assert file_pdf.suggested_filename == "sample.pdf"
        file_pdf.save_as("downloads/sample.pdf")

        #text validation
        with page.expect_download() as download_info:
            file_text.click()
            file_text = download_info.value
            assert file_text.suggested_filename == "sample.txt"
            file_text.save_as("downloads/sample.txt")