Alberta Energy Sources
======================

- Get data from AESO website (http://ets.aeso.ca/ets_web/ip/Market/Reports/CSDReportServlet)
- Save to CSV

To scrape every 5 minutes:
```bash
crontab -e
```
```bash
*/5 * * * * PATH=$PATH:/usr/sbin /Volumes/Data/garrett/applications/anaconda2/bin/python /Volumes/Data/garrett/GoogleDrive/Projects/AlbertaEnergy/get_data.py
```