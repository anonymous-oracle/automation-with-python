import os

import camelot
import pandas as pd

# # read data from html pages
# SUPERNATURAL_EPISODES_LIST = 'https://en.wikipedia.org/wiki/List_of_Supernatural_episodes'
# supernatural_seasons_tables_list = pd.read_html(SUPERNATURAL_EPISODES_LIST)
# print(supernatural_seasons_tables_list[1].to_dict())

# # read data from https://www.football-data.co.uk/englandm.php
# football_data = pd.read_csv('https://www.football-data.co.uk/mmz4281/2122/E0.csv')  # reads from the url instead of a
# # filepath or buffer
# # rename column names
# football_data.rename(columns={'FTHG':'home_goals', 'FTAG':'away_goals'}, inplace=True)
# print(football_data.to_dict().keys())

# extract tables from pdf files
table_from_pdf = camelot.read_pdf('foo.pdf', pages="1",  flavor='stream')
print(os.getcwd())
table_from_pdf.export(os.path.join(os.getcwd(), 'foo.csv'), 'csv', compress=False)