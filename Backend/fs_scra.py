# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 00:11:49 2019

@author: PI
"""

import requests
from bs4 import BeautifulSoup
# import csv


pageUrl = 'https://ngn.fxexchangerate.com/'
# pageUrl = input("Enter Url==>")
request = requests.get(pageUrl)
soup=BeautifulSoup(request.text, 'lxml')
# readable = soup.prettify()
# print(readable)

# Target data table
data_table = soup.find('table',{'class':'fx-table-none'})

# Extract and write data as text
with open('fx_exchange.txt', mode='w') as fx_data_op:
    fx_data_op.write('Country\tCode\tRate\n') # Write needed headers
    for row in data_table.find_all('tr'): # loop through target element
        tds = row.find_all('td')
    #    print(tds)
        try:
            fx_data_op.write(str(tds[0].text)+"\t"+str(tds[1].text)+"\t"+str(tds[2].text+"\n"))
        # Empty lists might occur initially
        except IndexError:
            pass
    