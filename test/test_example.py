from playwright.sync_api import Page, expect
from elements import HomePage
from time import sleep


def test_has_logo(page: Page):
    page.goto("https://www.youtube.com/")

    expect(page.locator(HomePage.LOGO)).to_be_visible()


def test_search_element(page: Page):
    page.goto("https://www.youtube.com/")
    channelName = "P-chan band"
    page.locator(HomePage.SEARCH_INPUT).fill(channelName)
    page.locator(HomePage.SEARCH_BUTTON).click()
    contentResults = page.locator(HomePage.CONTENT_RESULTS)
    firstChannelName = contentResults.locator(HomePage.FIRS_CHANNEL)

    expect(firstChannelName.get_by_text(channelName).first) \
        .to_have_text(channelName)
