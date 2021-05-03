import csv
try:
    class CSV:
        def csv_read(self):
            with open('university_records.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)
    # creating object for the class and calling the method
    readcsv = CSV()
    readcsv.csv_read()
except Exception as e:
    print(e)

#import pandas as pd
#obj = pd.read_csv('university_records.csv')