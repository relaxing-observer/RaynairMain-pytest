from utils.browser_helper import ElementInteractions


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.element_interactions = ElementInteractions(self.browser)

    def open(self):
        self.browser.get(self.url)