from types import TracebackType
import booking.contants as const
from selenium import webdriver
from selenium.webdriver.common.by import By

from booking.booking_filters import BookingFilter
from booking.booking_report import BookingReport

import time


class Booking(webdriver.Chrome):
    def __init__(self, teardown=False):
        self.teardown = teardown
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging','enable-automation'])
        options.add_experimental_option("detach", True)        
        super(Booking, self).__init__(options=options)
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type: type[BaseException] | None, exc: BaseException | None, traceback: TracebackType | None):
        if self.teardown:
            self.quit()
        # return super().__exit__(exc_type, exc, traceback)

    def land_first_page(self):
        self.get(const.BASE_URL)
        try:
            self.find_element(By.CSS_SELECTOR, '#b2indexPage > div.b9720ed41e.cdf0a9297c > div > div > div > div.dd5dccd82f > div.ffd93a9ecb.dc19f70f85.eb67815534 > div > button > span > span > svg > path').click()
        except:
            print('No element found for popup...')

    def change_currency(self, currency=None):
        currency_element = self.find_element(By.CSS_SELECTOR, 
                           'button[data-testid="header-currency-picker-trigger"]' 
                           )
        currency_element.click()

    def select_place_to_go(self, place_to_go):
        search_field = self.find_element(
            By.ID, ':re:'
        )
        search_field.clear()
        search_field.send_keys(place_to_go)

        first_result = self.find_element(
            By.ID, 'autocomplete-result-0'
        )

        # first_result_btn =  first_result.find_element(By.CSS_SELECTOR, 'div[role="button"]')

        # Wait to ensure selection is available
        time.sleep(const.WAIT_SECONDS)

        first_result.click()


    def select_dates(self, check_in, check_out):
        check_in_element = self.find_element(
            By.CSS_SELECTOR, 
            f'span[data-date="{check_in}"]'
        )

        check_in_element.click()

        check_out_element = self.find_element(
            By.CSS_SELECTOR, 
            f'span[data-date="{check_out}"]'
        )

        check_out_element.click()


    def select_adults(self, count=1):
        selection_element = self.find_element(
            By.CSS_SELECTOR,
            'button[data-testid="occupancy-config"]'
        )

        selection_element.click()

        # adult_count_element = self.find_element(
        #     By.CSS_SELECTOR,
        #     'div.a7a72174b8:nth-child(1) > div:nth-child(3) > span:nth-child(2)'
        # )

        # Alternative adult_count_element using id
        adult_count_element = self.find_element(By.ID, 'group_adults')
        
        decrease_adults_element = self.find_element(
            By.CSS_SELECTOR,
            'button.bb803d8689:nth-child(1)'
        )

        while int(adult_count_element.get_attribute('value')) > 1:
            decrease_adults_element.click()

        increase_adults_element = self.find_element(
            By.CSS_SELECTOR,
            'div.a7a72174b8:nth-child(1) > div:nth-child(3) > button:nth-child(3)'
        )

        while int(adult_count_element.get_attribute('value')) < count:
            increase_adults_element.click()

    def click_search(self):
        search_button = self.find_element(
            By.CSS_SELECTOR,
            'button[type="submit"]'
        )

        search_button.click()


    def apply_filters(self, star_rating):
        filters = BookingFilter(driver=self)
        filters.apply_star_rating(*star_rating)
        time.sleep(const.WAIT_SECONDS)

        filters.sort_price_lowest_first()

    def report_results(self):
        # self.find_element(By.CLASS_NAME, 'd4924c9e74')
        
        hotel_boxes = self.find_elements(By.CSS_SELECTOR, 'div[data-testid="property-card-container"]')

        report = BookingReport(hotel_boxes)

        report.get_deal_details()

        print(report.deals_df)



