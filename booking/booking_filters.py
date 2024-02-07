'''
This file will include a class with instance methods thatwill be responsible
for interacting with out website

After we have some results, apply filters
'''
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class BookingFilter:
    def __init__(self, driver:WebDriver):
        self.driver = driver
        self.dismiss_popup()

    def dismiss_popup(self):
        try:
            element = self.driver.find_element(By.CSS_SELECTOR, '#b2searchresultsPage > div.b9720ed41e.cdf0a9297c > div > div > div > div.dd5dccd82f > div.ffd93a9ecb.dc19f70f85.eb67815534 > div > button')
            element.click()
        except:
            pass

    def apply_star_rating(self, *star_values) :
        property_rating_box = self.driver.find_element(By.CSS_SELECTOR, 'div[data-filters-group="class"]')
        property_rating_child_elements = property_rating_box.find_elements(By.TAG_NAME, 'input')

        for star_value in star_values:
            for star_element in property_rating_child_elements:
                # if str(star_element.get_attribute('innerHTML')).strip() == f'{star_value} stars':
                if star_element.get_attribute('name').strip() == f'class={star_value}':
                    star_element.click()

    def sort_price_lowest_first(self):
        self.driver.find_element(By.CSS_SELECTOR, 'button[data-testid="sorters-dropdown-trigger"]').click()
        self.driver.find_element(By.CSS_SELECTOR, 'button[data-id="price"]').click()
