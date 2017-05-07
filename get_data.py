import datetime
from pytz import timezone 
import pandas as pd 

csv_file = '/Volumes/Data/garrett/GoogleDrive/Projects/AlbertaEnergy/data.csv'
ab_power_address = 'http://ets.aeso.ca/ets_web/ip/Market/Reports/CSDReportServlet'

# Generate timestamp
calgary = timezone('Canada/Mountain')
now = datetime.datetime.now(calgary)

# Get summary
data = pd.read_html(ab_power_address, match='SUMMARY', skiprows=range(1))[1]
data.columns = ['Description', 'Power']
summary = data['Power']

# Get generation data
data = pd.read_html(ab_power_address, match='GROUP', header=1)[1]
tng = data['TNG']  # TNG - Total Net Generation
mc = data['MC']    # MC  - Maximum Capacity
dcr = data['DCR']  # DCR - Dispatched (and Accepted) Contingency Reserve

# Get interchange data
data = pd.read_html(ab_power_address, match='Saskatchewan', header=1)[1]
ict = data['ACTUAL FLOW']

# WRITE TO CSV ---------------------------------------------------------------

with open(csv_file, 'a') as f:
    str_list = [now]
    str_list += summary.tolist()
    str_list += tng.tolist()
    str_list += mc.tolist()
    str_list += dcr.tolist()
    str_list += ict.tolist()
    str_list = [str(x) for x in str_list]
    f.write(', '.join(str_list) + ' \n')
