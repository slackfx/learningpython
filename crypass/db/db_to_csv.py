import csv

def write_csv(db, dbname):
    with open(dbname, 'w', newline='') as csv_file:
        csvwriter = csv.writer(csv_file, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for entry in db:
            csvwriter.writerow([entry.name, entry.url, entry.username, entry.password])
