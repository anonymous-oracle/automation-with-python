import os

from booking.booking import Booking
from selenium.webdriver.chrome.options import Options

# # inst = Booking(driver_path=os.path.join(os.getcwd(), 'chromedriver'))
# inst = Booking()
#
# inst.land_first_page()

options = Options()
# options.headless = True

# IMPLEMENTING CONTEXT MANAGERS
with Booking(teardown=True, options=options) as bot:
    bot.land_first_page()
    bot.change_currency()
    bot.select_place_to_go('California')
    bot.select_dates(check_in_date='2023-09-20', check_out_date='2023-10-25')
    bot.select_rooms_and_people(adults=5, rooms=2)
    bot.click_search()
    bot.apply_filtrations()
    bot.refresh() # allows the bot to grab data properly
    bot.report_results()
    print("Exiting...")


# inst.quit()