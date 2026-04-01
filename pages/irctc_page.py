from pages.base_page import BasePage
from playwright.sync_api import expect

class IRCTCPage(BasePage):

    def open(self):
        self.page.goto("https://www.irctc.co.in/nget/train-search")

    def select_from(self, city):
        self.page.get_by_label("Enter From station. Input is Mandatory.").fill(city)
        self.page.wait_for_selector(".ui-autocomplete-items li")
        self.page.locator(".ui-autocomplete-items li").first.click()

    def select_to(self, city):
        self.page.get_by_label("Enter To station. Input is Mandatory.").fill(city)
        self.page.wait_for_selector(".ui-autocomplete-items li")
        self.page.locator(".ui-autocomplete-items li").first.click()

    def select_date(self, day):
        self.page.click("#jDate")
        self.page.wait_for_selector(".ui-datepicker")
        self.page.locator(f".ui-datepicker-calendar td >> text={day}").click()

    def select_class(self, cls):
        self.page.locator("#journeyClass").click()
        option = self.page.get_by_text(cls)
        expect(option).to_be_visible()
        option.click()

    def train_search(self):
        self.page.locator("button:has-text('Search')").click()

    def get_train_list(self):
        self.page.wait_for_selector(".train-name")
        return self.page.locator(".train-name").all_text_contents()