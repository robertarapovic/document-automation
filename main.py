from cred import username
from cred import psw
from create_document import CreateDocument
from extract_data import ExtractData
import os
from os import listdir

# Main program to execute. Calling and executing all classes, create document and remove file with data

file = listdir('C:/Users/robert.arapovic/kod/therefore/erp_files')
file_full_path = f"C:/Users/robert.arapovic/kod/therefore/erp_files/{file[0]}"
data = ExtractData(file_full_path)
employees = data.extract()

try:
    for one in employees:
        name = one['ime']
        surname = one['prezime']
        number = one['index']
        body = {
            "CategoryNo": 14,
            "IndexDataItems": [
                {
                    "StringIndexData": {
                        "FieldNo": 113,
                        "DataValue": name
                    }
                },
                {
                    "StringIndexData": {
                        "FieldNo": 114,
                        "DataValue": surname
                    }
                },
                {
                    "IntIndexData": {
                        "FieldNo": 115,
                        "DataValue": number
                    }
                }
            ],
            "DoFillDependentFields": True,
            "ConversionOptions": {
                "ConvertTo": 0
            }
        }
        new_document = CreateDocument(body, username, psw)
        doc_no = new_document.create_document()
        print(doc_no)
except:
    print('Please check your excel!')

os.remove(file_full_path)