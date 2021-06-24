#!/usr/bin/env python
# #-*- coding: utf-8 -*-

import json

data_dir = "../data/"
# file_name = data_dir + "country.json"
# file_name = data_dir + "color.json"
# file_name = data_dir + "colors.json"
# file_name = data_dir + "porsche.json"
file_name = data_dir + "cars.json"

class DataObject:

    def __init__(self, file):
        self.file_name = file
        self.file = open(self.file_name)
        self.dataobject = json.load(self.file)
        
        # Testing string variable
        self.count = 0              # items counter
        self.index = []
        self.print = []             # test string
        self.dash = "- "
        self.tab = "\t"
        self.tabdash = "\t- "
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
        if n in self.index:
            self.print.append(self.tabdash+ n +" < found in data set.")
        else:
            self.print.append(self.tabdash+ n + " < not found in data set.")

    def sort(self, n):
        self.print.append("sort")
        if n == True : # true: sort ascending
            self.print.append(self.tabdash+"sort ascending")
        else: # false: sort descending
            self.print.append(self.tabdash+"sort descending")

    def validate(self, data):
        t = None
        if isinstance(data, dict):
            t = "dict"
            self.print.append(self.tab + ' >> validate = object is a ' + t)
        if isinstance(data, list):
            t = "list"
            self.print.append(self.tab + ' >> validate = object is a ' + t)
        if isinstance(data, str):
            t = "str"
            self.print.append(self.tab + ' >> validate = object is a ' + t)
        return t

    def iterate(self, data):

        if isinstance(data, list):
            for i in range(len(data)):
                if isinstance(data[i] ,str) or isinstance(data[i] , int):
                    self.print.append(self.tabdash + "VALUE LIST: " + str(data[i]))
                    self.index.append(str(data[i]))
                    self.count += 1
                else:
                    self.iterate(data[i])
        elif isinstance(data, dict):
            i = len(data.keys())
            for (k, v) in data.items():
                self.print.append(self.tabdash + "KEY DICT: " + str(k)) 
                if isinstance(v, str):
                    self.print.append(self.tabdash + "VALUE DICT: " + str(v)) 
                    self.index.append(str(v))
                    self.count += 1
                else:
                    self.iterate(v)
 
    def count_items(self):
        data = self.dataobject

        if isinstance(data, dict) or isinstance(data, list):
            self.iterate(data)
        else: 
             self.print.append(self.tab + 'object is NOT a dictionary')     
        return self.count

    def count_branch_level(self):
        # list number of sub levels within dictionary
        self.print.append("count_branch_level")

    def printasstr(self):
        for attribute, value in self.dataobject.items():		
            self.print.append(attribute + str(value))
       #     print(attribute, str(value))

    def printobject(self, n):
        self.print.append("printobject")
        if n == True: # true print list
            print(str(self.print))
        else:
            for n in self.print:
                print(n)
        self.print = []

dao = DataObject(file_name)
print(dao.count_items())

# dao.printasstr()
dao.find("Rover")

dao.printobject(False)
# dao.printobject(True)


