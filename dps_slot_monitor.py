import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.txdpsscheduler.com/")
    page.get_by_role("button", name="English").first.click()
    expect(page.get_by_role("spinbutton", name="Texas Card Number (DL, ID,")).to_be_visible()

    page.locator("div").filter(has_text=re.compile(r"^First Name$")).first.click()
    page.get_by_role("textbox", name="First Name").fill("md")
    page.get_by_role("textbox", name="Last Name").click()
    page.get_by_role("textbox", name="Last Name").fill("rubel")
    page.locator("div").filter(has_text=re.compile(r"^Date of Birth \(mm/dd\/yyyy\)event$")).first.click()
    page.get_by_role("textbox", name="Date of Birth (mm/dd/yyyy)").fill("11/01/1985")
    page.locator("div").filter(has_text=re.compile(r"^Last four of SSNvisibility$")).first.click()
    page.get_by_role("spinbutton", name="Last four of SSN").fill("1234")
    page.get_by_role("textbox", name="Cell Phone").click()
    page.get_by_role("textbox", name="Cell Phone").fill("(972) 793-0528")
    page.get_by_role("button", name="Log On").click()
    expect(page.get_by_role("button", name="VERIFY")).to_be_visible()

    page.locator("#input-84").click()
    page.locator("#input-84").fill("176775")
    page.get_by_role("button", name="VERIFY").click()
    expect(page.get_by_role("button", name="Log Out")).to_be_visible()

    page.get_by_role("button", name="New Appointment").click()
    expect(page.get_by_role("heading", name="Please select the option that")).to_be_visible()

    page.get_by_role("button", name="Service not listed or my").click()
    expect(page.get_by_role("button", name="Yes")).to_be_visible()

    page.get_by_role("button", name="No").click()
    expect(page.get_by_role("textbox", name="First Name")).to_be_visible()

    page.get_by_role("textbox", name="Email", exact=True).click()
    page.get_by_role("textbox", name="Email", exact=True).fill("rubeldm123@gmail.com")
    page.get_by_role("textbox", name="Verify Email").click()
    page.get_by_role("textbox", name="Verify Email").fill("rubeldm123@gmail.com")
    page.get_by_role("textbox", name="Zip Code").click()
    page.get_by_role("textbox", name="Zip Code").fill("75061")
    page.get_by_role("button", name="Next").click()
    expect(page.get_by_role("row", name="Fort Worth Mega Center 8301")).to_be_visible()

    page.get_by_text("arrow_forward_ios").click()
    expect(page.get_by_role("row", name="Thursday 7/9/2026 Friday 7/10")).to_be_visible()

    page.get_by_role("button", name="Log Out").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
