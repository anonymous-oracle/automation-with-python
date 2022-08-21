from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from datetime import date, timedelta
from booking.bookingfiltrations import BookingFiltrations
import os
import booking.constants as const
from booking.booking_report import BookingReport

class Booking(webdriver.Chrome):
    def __init__(self, driver_path=None, teardown=False, **kwargs):
        self.driver_path = driver_path
        self.teardown = teardown
        if not driver_path:
            self.driver_path = os.getcwd()
        os.environ['PATH'] += f"{self.driver_path}:"
        os.environ['PATH'] += f"{os.path.dirname(self.driver_path)}:"
        # print(os.environ['PATH'])
        super().__init__(**kwargs)
        self.implicitly_wait(3) # implicitly wait until next element is found but it won't wait complete 15 seconds
        # always
        self.maximize_window()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def __exit__(self, exc_type, exc_val, exc_tb): # implementing the context teardown
        if self.teardown:
            self.quit()

    def change_currency(self, currency='USD'):
        # currency_element = self.find_element(by=By.CSS_SELECTOR, value='button[data-tooltip-text="Choose your
        # currency"]') # using CSS
        # selector
        currency_element = self.find_element(by=By.XPATH, value='//button[@data-tooltip-text="Choose your '
                                                                'currency"]') # by XPATH
        currency_element.click()

        currency_option_xpath = f"//a[contains(@data-modal-header-async-url-param, 'selected_currency={currency}')]"

        self.find_element(by=By.XPATH, value=currency_option_xpath).click()

    def select_place_to_go(self, place_to_go="zurich"):
        input_field = self.find_element(by=By.ID, value='ss')
        input_field.clear() # clears any existing text
        input_field.send_keys(place_to_go)

        # to select the first result from drop down options
        first_result = self.find_element(by=By.XPATH, value='//li[@data-i="0"]')
        first_result.click()

    def num_month_clicks(self, datestamp):
    #     returns number of month clicks needed to select the date range for check in and check out
        today = date.today()
        year, month, day = [int(e) for e in datestamp.split('-')]
        check_in = date(year=year, month=month, day=day)
        delta_days = (check_in - today).days
        if delta_days < 30:
            return 0
        # delta = timedelta(days=delta.days) + today
        years = delta_days / 365
        delta_days = delta_days % delta_days
        months = delta_days / 30
        delta_days = delta_days % 30
        return int((years * 12) + months)

    def select_dates(self, check_in_date, check_out_date):
        # DATE FORMAT: YYYY-MM-DD
        clicks = self.num_month_clicks(check_in_date)

        for click in range(clicks):
            calendar_next_element = self.find_element(By.XPATH, "//div[@data-bui-ref='calendar-next']")
            calendar_next_element.click()

        check_in_date_element = self.find_element(By.XPATH, f"""//td[@data-date="{check_in_date}"]""")
        check_in_date_element.click()
        check_out_date_element = self.find_element(By.XPATH, f"""//td[@data-date="{check_out_date}"]""")
        check_out_date_element.click()

    def select_rooms_and_people(self, adults=1, rooms=1, children=0):
        dropdown_selection = self.find_element(By.ID, 'xp__guests__toggle')
        dropdown_selection.click()

        adult_decrease = self.find_element(By.XPATH, '//button[@aria-label="Decrease number of Adults"]')
        adult_increase = self.find_element(By.XPATH, '//button[@aria-label="Increase number of Adults"]')
        children_decrease = self.find_element(By.XPATH, '//button[@aria-label="Decrease number of Children"]')
        children_increase = self.find_element(By.XPATH, '//button[@aria-label="Increase number of Children"]')
        room_decrease = self.find_element(By.XPATH, '//button[@aria-label="Decrease number of Rooms"]')
        rooms_increase = self.find_element(By.XPATH, '//button[@aria-label="Increase number of Rooms"]')

        # adult_count = int(adult_increase.find_element(By.XPATH, '..').find_element(By.XPATH, './span[text()]').text)
        # room_count = int(rooms_increase.find_element(By.XPATH, '..').find_element(By.XPATH, './span[text()]').text)
        # children_count = int(children_increase.find_element(By.XPATH, '..').find_element(By.XPATH, './span[text()]').text)

        adult_count = int(self.find_element(By.ID, 'group_adults').get_attribute('value'))
        children_count = int(self.find_element(By.ID, 'group_children').get_attribute('value'))
        room_count = int(self.find_element(By.ID, 'no_rooms').get_attribute('value'))

        adult_change = adults - adult_count
        children_change = children - children_count
        room_change = rooms - room_count

        if adult_change > 0:
            for i in range(adult_change):
                adult_increase.click()
        else:
            for i in range(abs(adult_change)):
                adult_decrease.click()

        if children_change > 0:
            for i in range(children_change):
                children_increase.click()
        else:
            for i in range(abs(children_change)):
                children_decrease.click()

        if room_change > 0:
            for i in range(room_change):
                rooms_increase.click()
        else:
            for i in range(abs(room_change)):
                room_decrease.click()


    def click_search(self):
        search_button = self.find_element(By.XPATH, '//button[@type="submit" and @class="sb-searchbox__button "]')
        search_button.click()

    def apply_filtrations(self):
        filtration = BookingFiltrations(driver=self)
        filtration.apply_star_rating_filter(5,4)
        filtration.sort_lowest_to_highest_price()


    def report_results(self):
        hotel_boxes_container = self.find_element(By.ID, 'search_results_table')
        # hotel_boxes = self.find_elements(By.XPATH, '//div[@data-testid="property-card"]')
        report = BookingReport(hotel_boxes_container)
        [print(f"{deal}\n") for deal in report.deal_title_price_score_attributes]

        pass
