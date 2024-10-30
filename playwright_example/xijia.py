# -*- coding: UTF-8 -*-
import asyncio
import time
from playwright import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.newContext()

    # Open new page
    page = context.newPage()

    # Go to http://
    page.goto("http://")

    # Click input[name="txtUsername"]
    page.click("input[name=\"txtUsername\"]")

    # Fill input[name="txtUsername"]
    page.fill("input[name=\"txtUsername\"]", "account")

    # Click input[name="txtPass"]
    page.click("input[name=\"txtPass\"]")

    # Fill input[name="txtPass"]
    page.fill("input[name=\"txtPass\"]", "passwd")

    # Click input[name="btnLogin"]
    page.click("input[name=\"btnLogin\"]")
    # assert page.url == "http://"


    # Open new page
    page1 = context.newPage()
    page1.goto('http://')

    print(page.frames)


    # Click text="CIQ Management"
    with page1.expect_popup() as popup_info:
        page1.click("text=\"CIQ Management\"")
    page2 = popup_info.value

    # Click text="CIQ Details"
    page2.click("text=\"CIQ Details\"")
    # assert page2.url == "http://"


    # Upload 表格.xlsx
    page2.setInputFiles("input[name=\"ctl00$ContentPlaceHolder1$fileupload\"]", r"C:\Users\EDZ\Desktop\解压缩文件夹\RY570\表格.xlsx")

    # Click input[name="ctl00$ContentPlaceHolder1$Button1"]
    # page2.once("dialog", lambda dialog: asyncio.create_task(dialog.dismiss()))
    page2.on("dialog", lambda dialog: (print("Dialog %s" % dialog.message),
                                      dialog.accept(),
                                      ))
    # with page2.expect_navigation(url="http://"):
    with page2.expect_navigation():
        # 点击 Upload
        page2.click("input[name=\"ctl00$ContentPlaceHolder1$Button1\"]")

    # Click text="CIQ Batch Files"
    page2.click("text=\"CIQ Batch Files\"")
    # assert page2.url == "http://"

    # Click input[name="ctl00$head$CiqContent$txtciq_id"]
    page2.click("input[name=\"ctl00$head$CiqContent$txtciq_id\"]")

    # Fill input[name="ctl00$head$CiqContent$txtciq_id"]
    page2.fill("input[name=\"ctl00$head$CiqContent$txtciq_id\"]", "RY570")

    # Go to http://
    page2.click('//*[@id="ctl00_head_CiqContent_btnSearch"]')



    # ---------------------------------
    # Click text="Upload File"
    page2.click('//*[@id="ctl00_ContentPlaceHolder1_gridView"]/tbody/tr[2]/td[7]/a')
    # assert page2.url == "http://"

    # Upload 卫生证书.pdf
    page2.setInputFiles("input[name=\"ctl00$ContentPlaceHolder1$FileUpload1\"]", r"C:\Users\EDZ\Desktop\解压缩文件夹\RY570\CIQ证书\卫生证书.pdf")

    # Click input[name="ctl00$ContentPlaceHolder1$btnUpdate"]
    page2.click("input[name=\"ctl00$ContentPlaceHolder1$btnUpdate\"]")
    # assert page2.url == "http://"

    # Click input[name="ctl00$ContentPlaceHolder1$btnReturn"]
    page2.click("input[name=\"ctl00$ContentPlaceHolder1$btnReturn\"]")
    # assert page2.url == "http://"
    # ---------------------------------


    # ---------------------------------
    # Click //td[8]/a[normalize-space(.)='Upload File']
    page2.click('//*[@id="ctl00_ContentPlaceHolder1_gridView"]/tbody/tr[2]/td[8]/a')
    # assert page2.url == "http://"

    # Upload 222520201000305059报关单.pdf
    page2.setInputFiles("input[name=\"ctl00$ContentPlaceHolder1$FileUpload1\"]", r"C:\Users\EDZ\Desktop\解压缩文件夹\RY570\报关单\222520201000305059报关单.pdf")

    # Click input[name="ctl00$ContentPlaceHolder1$btnUpdate"]
    page2.click("input[name=\"ctl00$ContentPlaceHolder1$btnUpdate\"]")
    # assert page2.url == "http://"

    # Click input[name="ctl00$ContentPlaceHolder1$btnReturn"]
    page2.click("input[name=\"ctl00$ContentPlaceHolder1$btnReturn\"]")
    # assert page2.url == "http://"
    # ---------------------------------


    # ---------------------------------
    # Click //td[9]/a[normalize-space(.)='Upload File']
    page2.click('//*[@id="ctl00_ContentPlaceHolder1_gridView"]/tbody/tr[2]/td[9]/a')
    # assert page2.url == "http://"

    # Upload 税单.pdf
    page2.setInputFiles("input[name=\"ctl00$ContentPlaceHolder1$FileUpload1\"]", r"C:\Users\EDZ\Desktop\解压缩文件夹\RY570\税单.pdf")

    # Click input[name="ctl00$ContentPlaceHolder1$btnUpdate"]
    page2.click("input[name=\"ctl00$ContentPlaceHolder1$btnUpdate\"]")
    # assert page2.url == "http://"

    # Click input[name="ctl00$ContentPlaceHolder1$btnReturn"]
    page2.click("input[name=\"ctl00$ContentPlaceHolder1$btnReturn\"]")
    # assert page2.url == "http://"
    # ---------------------------------


    # Click text="CIQ Details"
    page2.click("text=\"CIQ Details\"")
    # assert page2.url == "http://"

    # Click input[name="ctl00$head$CiqContent$txtciq_id"]
    page2.click("input[name=\"ctl00$head$CiqContent$txtciq_id\"]")

    # Fill input[name="ctl00$head$CiqContent$txtciq_id"]
    page2.fill("input[name=\"ctl00$head$CiqContent$txtciq_id\"]", "RY570")

    # Go to http://
    page2.click('//*[@id="ctl00_head_CiqContent_btnSearch"]')


    # Close page
    page2.close()

    # Close page
    page1.close()

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
