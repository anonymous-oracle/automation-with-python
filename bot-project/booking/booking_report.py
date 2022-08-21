# parses the data needed obtained from the deal boxes and will present the parsed data
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class BookingReport():

    def __init__(self, boxes_section_element: WebElement):
        self.boxes_section_element = boxes_section_element
        self.boxes_section_element_parent = self.boxes_section_element.parent

    def _pull_deal_boxes(self):
        return self.boxes_section_element.find_elements(By.XPATH,
                                                               '//div[@data-testid="property-card"]')
    def _pull_deal_boxes_iter(self):
        for deal_box in self.boxes_section_element_parent.find_elements(By.XPATH,
                                                               '//div[@data-testid="property-card"]'):
            yield deal_box

    def _pull_deal_titles(self):
       # avoid debugging in the debugger otherwise the elements will become stale
        return [deal.find_element(By.CSS_SELECTOR, '[data-testid="title"]').text for deal in self.deal_boxes]

    def _pull_deal_prices(self):
        # data-testid="price-and-discounted-price"
        return [deal.find_element(By.CSS_SELECTOR, 'data-testid="price-and-discounted-price"').text for deal in self.deal_boxes]
    def _pull_review_score(self):
            pass

    def _get_review_score(self, deal_text):
        pass

    def _pull_deal_attributes(self):
        results = []
        for deal in self.deal_boxes:
            deal_attributes = []
            # deal_attributes.append(deal.find_element(By.CSS_SELECTOR, '[data-testid="title"]').text)
            # deal_attributes.append(deal.find_element(By.CSS_SELECTOR, '[data-testid="price-and-discounted-price"]').text)
            deal_attributes.append(deal.text.split('\n')[4]+'|'+deal.text )
            results.append(deal_attributes)
        return results




    deal_boxes = property(_pull_deal_boxes)
    deal_boxes_iter = property(_pull_deal_boxes_iter)
    deal_titles = property(_pull_deal_titles)
    deal_prices = property(_pull_deal_prices)
    deal_scores = property(_pull_review_score) # not implemented
    deal_title_price_score_attributes = property(_pull_deal_attributes)