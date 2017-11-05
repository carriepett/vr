import csv
with open('data.csv', newline='') as csvfile:
    attendancereader = csv.reader(csvfile, delimiter=',')
    for row in attendancereader:
        print(', '.join(row))
