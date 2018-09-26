import csv

results = []

with open('gerrymander_score_unclean.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		results.append(row)
		for item in results:
			item.lower()
	print(results)





#filtered_dict = {k:v for (k,v) in data.items() if filter_string in k}

"""	data = (list(reader))"""

"""
for row in gs_dictionary:
	print(row['district_code'], row['gerrymander_score'])

print(list(gs_dictionary)
"""
	#print(row['district_code'], row['gerrymander_score'])
