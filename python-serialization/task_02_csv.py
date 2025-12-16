#!/usr/bin/python3
import csv
import json
def convert_csv_to_json(csv_file):
    try:
        with open(csv_file, mode='r', newline='', encoding='utf-8') as f:
            data = list(csv.DictReader(f))

        with open('data.json', mode='w', encoding='utf-8') as f:
            json.dump(data, f)
            return True
    except:
        return False
