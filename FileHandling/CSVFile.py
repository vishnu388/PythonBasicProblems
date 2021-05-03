import csv
try:
    class CSV:
        def csv_write(self):
            fields = ['Name', 'Branch', 'Year', 'CGPA']
            Table = [['vishnu', 'Mech', '2018', '8.2'],
                    ['Chari', 'Mech', '2018', '9.1'],
                    ['Tarun', 'Mech', '2018', '8.5'],
                    ['sekhar', 'Bcom', '2018', '8.0'],
                    ['Kiran', 'PharmD', '2019', '9.5'],
                    ['Ashok', 'CA', '2016', '9.8']]

            filename = "university_records.csv"

            with open(filename, 'w') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(fields)
                csvwriter.writerows(Table)
    # creating object for the class and calling the method
    writecsv = CSV()
    writecsv.csv_write()
except Exception as e:
    print(e)