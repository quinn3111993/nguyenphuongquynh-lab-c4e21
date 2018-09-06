from pymongo import MongoClient
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot

uri = 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e'

client = MongoClient(uri)
db = client.get_default_database()
customers = db['customers']

ref_group = customers.aggregate([
    {'$group' : {'_id':'$ref', 'count': {'$sum': 1}}}
])
ref_list = list(ref_group)

ref_names = []
ref_count = []
for ref in ref_list:
    print(ref['_id'], ':', ref['count'])
    ref_names.append(ref['_id'])
    ref_count.append(ref['count'])

pyplot.pie(ref_count, labels=ref_names, autopct='%.1f%%', shadow=True)
pyplot.title('Pie chart: Reference Percentage')
pyplot.axis('equal')

print(ref_list)

pyplot.show()



