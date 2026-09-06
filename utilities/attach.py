import allure

from allure_commons.types import AttachmentType


def add_screenshot(driver):
    png = driver.get_screenshot_as_png()

    allure.attach(
        body=png,
        name="screenshot",
        attachment_type=AttachmentType.PNG,
        extension=".png",
    )


def add_logs(driver):
    log = "".join(
        f"{text}\n"
        for text in driver.get_log(log_type="browser")
    )

    allure.attach(
        body=log,
        name="browser_logs",
        attachment_type=AttachmentType.TEXT,
        extension=".log",
    )


def add_html(driver):
    html = driver.page_source

    allure.attach(
        body=html,
        name="page_source",
        attachment_type=AttachmentType.HTML,
        extension=".html",
    )