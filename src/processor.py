#!/usr/bin/env python
# #-*- coding: utf-8 -*-

import json

file_name = "country.json"
file_name = "colors.json"
file_object = open(file_name)
json_object = json.load(file_object)

class DataObject:

    def __init__(self, data):
        self.dataobject = data
        self.print = []
        self.dash = "- "
        self.tab = "\t"
        self.tabdash = "\t- "
        self.print.append(str(data))
        self.print.append("DataObject")

    def convert_to_json(self, n):
        self.print.append("convert_to_json")
        if n.lower() == "xml":
            self.print.append(self.tabdash+"XML file type")
        elif n.lower() == "json":
            self.print.append(self.tabdash+"JSON file type")
        elif n.lower() == "yml" or n.lower() == "yaml":
            self.print.append(self.tabdash+"YAML file type")
        else:
            self.print.append(self.tabdash+"not suporrted file type")

    def find(self, n):
        self.print.append("find")
        if n in self.dataobject:
            self.print.append(self.tabdash+"found string")
        else:
            self.print.append(self.tabdash+"sting not found")

    def sort(self, n):
        self.print.append("sort")
        if n == True : # true: sort ascending
            self.print.append(self.tabdash+"sort ascending")
        else: # false: sort descending
            self.print.append(self.tabdash+"sort descending")

    def count_items(self):
        # list total number of data items
        self.print.append("count_items")

    def count_branch_level(self):
        # list number of sub levels within dictionary
        self.print.append("count_branch_level")

    def printobject(self, n):
        self.print.append("printobject")
        if n == True: # true print list
            print(str(self.print))
        else:
            for n in self.print:
                print(n)
        self.print = []

dao = DataObject(file_name)
dao.sort("yml")

# dao.printobject(False)
dao.printobject(True)