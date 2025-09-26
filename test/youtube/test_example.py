from playwright.sync_api import Page, expect
from elements import HomePage
from core.host import Host
from test_data.youtube import TestData


def test_has_logo(page: Page):
    page.goto(Host.Youtube)

    expect(page.locator(HomePage.LOGO)).to_be_visible()


def test_search_element(page: Page):
    channelName = TestData.SearchChannel
    page.goto(Host.Youtube)
    page.locator(HomePage.SEARCH_INPUT).fill(channelName)
    page.locator(HomePage.SEARCH_BUTTON).click()
    contentResults = page.locator(HomePage.CONTENT_RESULTS)
    firstChannelName = contentResults.locator(HomePage.FIRS_CHANNEL)

    expect(firstChannelName.get_by_text(channelName).first) \
        .to_have_text(channelName)
