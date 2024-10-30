# -*- coding: UTF-8 -*-
import time

from playwright import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.newContext()

    # Open new page
    page = context.newPage()

    try:
        page.goto('http://')
        print('VPN已经登录')
    except:
        # Go to https://
        page.goto("https://")

        # Click input[name="login"]
        page.click("input[name=\"login\"]")

        # Fill input[name="login"]
        page.fill("input[name=\"login\"]", "account")

        # Click input[name="passwd"]
        page.click("input[name=\"passwd\"]")

        # Fill input[name="passwd"]
        page.fill("input[name=\"passwd\"]", "passwd")

        # Press Enter
        page.press("input[name=\"passwd\"]", "Enter")
        # assert page.url == "https://"

        # Click input[name="cm"]
        # with page.expect_navigation(url="https://"):
        with page.expect_navigation():
            try:
                page.click("input[name=\"cm\"]")
            except:
                print('没有出现按钮')
            finally:
                for i in range(10):
                    if page.url == 'http://':
                        print('VPN登陆成功')
                        break
                    time.sleep(1)
    finally:
        # Close page
        page.close()

        # ---------------------
        context.close()
        browser.close()

with sync_playwright() as playwright:
    run(playwright)
