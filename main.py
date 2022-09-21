from openpyxl import Workbook
import csv
filename = "sample.csv"
name_sheet = "phone book"
exel_file = Workbook()
exel_sheet = exel_file.create_sheet(name_sheet)
with open(filename) as data:
    for line in csv.reader(data):
        if line:
            exel_sheet.append(line)

exel_file.save(filename="qwer.xlsx")