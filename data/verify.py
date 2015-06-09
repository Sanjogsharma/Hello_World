import csv
with open('airlines.csv', 'rU') as f:
    data = [row for row in csv.reader(f)]


header = data[0]
data = data[1:]


#code for problem #1


list_incidents = [(float(row[2])+float(row[5]))/30 for row in data]


# create empty ist 

#determine the last character
# if* append the string 

#[x+1 if x >= 45 else x+5 for x in l]

airline_name =[row[0] if row[0][-1] != '*' else row[0][0:-1] for row in data]


star_indicator =[0 if row[0][-1] != '*' else 1 for row in data]




'''number 3

> if * add 1, else add 0
'''

#d = {key: value for (key, value) in iterable}

dummy_dict = {row[0]if row[0][-1] != '*' else row[0][0:-1]: (float(row[2])+float(row[5]))/30 for row in data}




