# Ports and Adapters Pattern: Adapter
# Purpose: Adapter for the CSVParserInterface, this class is responsible for parsing a CSV file.
# Additional Information: This class is an implementation of the CSVParserInterface, it uses the csv module to parse the CSV file

import csv
from adapters.csv_parser.CSVParserInterface import CSVParserInterface

class CSVParser(CSVParserInterface):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def parse(self):
        with open(self.file_path, 'r') as file:
            reader = csv.reader(file)
            return list(reader)
        
# How to add requirements to requirements.txt using pip freeze
# pip freeze > requirements.txt
