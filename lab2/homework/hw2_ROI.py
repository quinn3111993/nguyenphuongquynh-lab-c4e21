from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict

url = 'http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn'
conn = urlopen(url)

raw_data = conn.read()
html_page = raw_data.decode('utf-8')

soup = BeautifulSoup(html_page, 'html.parser')

# Extract key 
keys = []
div = soup.find('div',id='divTableHeader')
row = div.table.tr
cols = row.find_all('td')[:-1]
keys = [ele.text.strip() for ele in cols]

# Extract value
values = []
div_val = soup.find('div',style='overflow:hidden;width:100%;border-bottom:solid 1px #cecece;')
rows = div_val.table.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    values.append([ele for ele in cols if ele])
values = [ele for ele in values if ele]

# Create data file
my_table = []
for i, row in enumerate(values):
    dic = OrderedDict({})
    for j, col in enumerate(row):
        dic[keys[j]] = col
    my_table.append(dic)

print(my_table)

import pyexcel
pyexcel.save_as(records=my_table, dest_file_name='ROI_table.xlsx')






