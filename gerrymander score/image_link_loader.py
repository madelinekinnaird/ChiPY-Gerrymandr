import csv

image_links = []
base_link = 'https://github.com/madelinekinnaird/Gerrymandr/blob/master/images/'


with open('gerrymander_score_clean.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        image_links.append({'district_id': row['district_id'], 'image_link': base_link + row['district_id'] + '.PNG'})


with open('gerrymander_image_links.csv', "w") as csvfile:
        fieldnames = ('district_id', 'image_link')
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in image_links:
            writer.writerow(row)
