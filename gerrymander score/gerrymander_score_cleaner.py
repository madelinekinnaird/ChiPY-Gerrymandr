import csv



with open('gerrymander_score_unclean.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		for value in row['district_code']:
			x = value.split('-')
		reader.update({'newkey':x})


print(row['newkey'])
		#results.append(row)





"""RANDOM ATTEMPTS

filtered_dict = {k:v for (k,v) in data.items() if filter_string in k}

for row in gs_dictionary:
	print(row['district_code'], row['gerrymander_score'])

print(list(gs_dictionary)

print(row['district_code'], row['gerrymander_score'])
"""
