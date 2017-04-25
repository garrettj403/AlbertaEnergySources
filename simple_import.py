from lxml import html
import requests
import pandas as pd 

ab_power_address = 'http://ets.aeso.ca/ets_web/ip/Market/Reports/CSDReportServlet'

data = pd.read_html(ab_power_address, match='GROUP')[1]
data = data.iloc[2:]  # Remove header rows
data.columns = ['Source', 'MC', 'TNG', 'DCR']
data.set_index('Source', inplace=True, drop=True)

tng = data['TNG']  # TNG - Total Net Generation
mc = data['MC']    # MC  - Maximum Capacity

print data