'''
f = open('airlines.csv', 'rU')
data = f.read()
f.close()


import csv
with open('airlines.csv', 'rU') as f:
    data = [row for row in csv.reader(f)]


header = data[0]
data = data[1:]



import csv

with open("tab-separated-values") as tsv:
    for line in csv.reader(tsv, dialect="excel-tab"): 
        ... 

'''

import csv

with open('chipotle.tsv','rU') as tsv:
    data = [row for row in csv.reader(tsv, dialect="excel-tab")]
    print data
    


