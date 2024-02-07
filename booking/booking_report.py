'''
This file is going to include methods that will parse
the specific data that we need from each one of the deal boxes
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

import pandas as pd

class BookingReport:
    def __init__(self, boxes_section_element:WebElement) -> None:
        self.boxes_section_element = boxes_section_element
        # self.deal_boxes = self.pull_deal_boxes()
        self.deal_boxes = boxes_section_element
        self.deal_details = []

    def pull_deal_boxes(self):
        return ''
    
    def get_deal_details(self):
        for deal_box in self.deal_boxes:
            hotel_name = deal_box.find_element(
                By.CSS_SELECTOR, 
                'div[data-testid="title"]'
                ).get_attribute('innerHTML').strip()
            
            hotel_price = deal_box.find_element(
                By.CSS_SELECTOR,
                'span[data-testid="price-and-discounted-price"]'
            ).get_attribute('innerHTML').strip().split(';')[1]

            hotel_score = deal_box.find_element(
                By.CSS_SELECTOR,
                'div[aria-label^="Scored"]'
            ).get_attribute('innerHTML').strip()

            self.deal_details.append({
                'Name': hotel_name,
                'Price': hotel_price,
                'Score': hotel_score
            })

        self.deals_df = pd.DataFrame(self.deal_details)