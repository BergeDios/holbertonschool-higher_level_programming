#!/usr/bin/python3
from sys import argv

"""
Module 9-add_item

"""

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    existing_content = load_from_json_file(filename)
except FileNotFoundError:
    existing_content = []

save_to_json_file(existing_content + argv[1:], filename)
