#!/usr/bin/env python3
"""Module for converting CSV data to JSON format."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Converts a CSV file to a JSON file named data.json."""
    try:
        with open(csv_filename, "r", encoding="utf-8") as csv_f:
            reader = csv.DictReader(csv_f)
            data_list = [row for row in reader]

        with open("data.json", "w", encoding="utf-8") as json_f:
            json.dump(data_list, json_f)

        return True
    except Exception:
        return False
