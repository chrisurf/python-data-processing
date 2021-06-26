#!/usr/bin/env python
# #-*- coding: utf-8 -*-

import json
import yaml
from xml.dom import IndexSizeErr, minidom


data_dir = "../data/"
file_name = data_dir + "country.json"
# file_name = data_dir + "color.json"
file_name = data_dir + "colors.json"
# file_name = data_dir + "porsche.json"
# file_name = data_dir + "cars.json"
# file_name = data_dir + "user.yaml"
# file_name = data_dir + "sample.xml"

class DataObject:

    def __init__(self, file, type = None):
        # Testing string variable
        self.count = 0              # items counter
        self.count_keys = 0         # keys counter
        self.count_values = 0       # values counter
        self.index = []
        self.print = []             # test string
        self.print.append("DataObject")
        self.file_name = file
        self.dataobject = None

        if 0 < self.file_name.lower().find("json"):
            type = "json"
        elif 0 < self.file_name.lower().find("yaml") or 0 < self.file_name.find("yml"):
            type = "yaml"
        elif 0 < self.file_name.lower().find("xml"):
            type = "xml"

        self.data = open(self.file_name)
        self.convert_to_json(type)

    def t(self, t, n = None):
        tab = ""
        if isinstance(t, int):
            for i in range(0, t):
              tab = tab + "\t"
        else:
            print("Not an integer")
            
        if isinstance(n, str):
            tab = tab + n + " "

        return tab


    def convert_to_json(self, n):
        if n.lower() == "json":
            self.dataobject = json.load(self.data)
        elif n.lower() == "yml" or n.lower() == "yaml":
            self.dataobject = yaml.load(self.data)
        elif n.lower() == "xml":
            self.print.append(self.t(1)+"XML file type")
            mydoc = minidom.parse(self.data)
            self.dataobject = mydoc.getElementsByTagName('Category')
            print(self.dataobject)
        else:
            self.print.append(self.t(1)+"not suporrted file type")

    def find(self, n):
        self.print.append("find")
        # currently index only holds values.
        # TODO: improve index with separated list of keys
        if n in self.index:
            self.print.append(self.t(1)+ n +" < found in data set.")
        else:
            self.print.append(self.t(1)+ n + " < not found in data set.")

    def sort(self, n):
        self.print.append("sort")
        if n == True : # true: sort ascending
            self.print.append(self.t(1)+"sort ascending")
        else: # false: sort descending
            self.print.append(self.t(1)+"sort descending")

    def validate(self, data):
        t = None
        if isinstance(data, dict):
            t = "dict"
            self.print.append(self.t(1) + ' >> validate = object is a ' + t)
        if isinstance(data, list):
            t = "list"
            self.print.append(self.t(1) + ' >> validate = object is a ' + t)
        if isinstance(data, str):
            t = "str"
            self.print.append(self.t(1) + ' >> validate = object is a ' + t)
        return t

    def iterate(self, data):

        if isinstance(data, list):
            for v in range(len(data)):
                self.get_value(data[v])

        elif isinstance(data, dict):
            i = len(data.keys())
            for (k, v) in data.items():
                self.count_keys += 1
                self.get_key(k)
                self.get_value(v)

    def get_key(self, k):
        self.count_keys += 1
        self.print.append(self.t(1, "KEY: ") + str(k))

    def get_value(self, v):
        if isinstance(v ,str) or isinstance(v , int):
            self.count_values += 1
            self.print.append(self.t(1, "-") + "VALUE: " + str(v))
            self.index.append(str(v))
            self.count += 1   
        else:
            self.iterate(v)    

    def count_items(self):
        data = self.dataobject

        if isinstance(data, dict) or isinstance(data, list):
            self.iterate(data)
        else: 
             self.print.append(self.t(1) + 'object is NOT a dictionary')     
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
dao.find("black")

dao.printobject(False)
# dao.printobject(True)