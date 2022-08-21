# This class will be responsible for applying filtrations on results
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException



class BookingFiltrations:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def apply_star_rating_filter(self, *star_rating):
        star_filtration_box = self.driver.find_element(By.XPATH, '//div[@class="ffa9856b86 ad9a06523f" and '
                                                                 '@data-filters-group="class"]')
        star_child_elements = star_filtration_box.find_elements(By.XPATH, './/*')

        for star in star_rating:
            for star_element in star_child_elements:
                if str(star_element.get_attribute('innerHTML')).strip() == f'{star} stars': # 'innerHTML' attribute
            # returns
            # content within the html tag
                    star_element.click()

    def sort_lowest_to_highest_price(self):

        try:
            sort_by_lowest_price_link = self.driver.find_element(By.XPATH, '//li[@data-id="price"]')
        except NoSuchElementException as e:
            sorting_options_dropdown = self.driver.find_element(By.XPATH, '//button[@data-testid="sorters-dropdown-trigger"]')
            sorting_options_dropdown.click()
            sort_by_lowest_price_link = self.driver.find_element(By.XPATH, '//button[@data-id="price"]')
        sort_by_lowest_price_link.click()
