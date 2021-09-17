import pandas as pd

# Class for export data from .xlsx file, that is exported from ERP system


class ExtractData:

    def __init__(self, file):
        self.file = file

    def extract(self):

        xl = pd.ExcelFile(self.file)
        wb = xl.parse("Sheet1")
        employees = []

        for row in wb.values:
            employee = {}
            employee['ime'] = row[0]
            employee['prezime'] = row[1]
            employee['index'] = row[2]
            employees.append(employee)

        return employees




