#!/usr/bin/env python
# #-*- coding: utf-8 -*-

import json

file_name = "country.json"
file_name = "colors.json"
file_object = open(file_name)
json_object = json.load(file_object)

def jsonkey(j_object):
    print("\n jsonkey")
    for (k, v) in j_object.items():
        print("Key: " + k)
        print("Value: " + str(v))
        # iterate and return dictionary

def jsonid(dict_var):
    print("\n jsonid")
    for k, v in dict_var.items():
        if isinstance(k, str):
            yield v
        elif isinstance(v, dict):
            for id_val in jsonid(v):
                yield id_val

#clean iteration
def jsonobj(j_object):	
    print("\n jsonobj")	
    for attribute, value in j_object.items():		
        print(attribute, str(value)) 		

def jstr(j_object):	
    print("\n printstr")	
    for k, v in j_object.items():		
        if isinstance(v, str):			
            # process value string			
            print(k + " = " + v)
        else:				
            print(str(k))				
            dictstr(v)

def dictstr(dic):	
    for k in dic:		
        if isinstance(dic[k], str):			
            # process value string			
            print(k + " = " + dic[k])
        else:
            print(str(k))				
            print(str(dic[k]))	

jsonkey(json_object)

for i in jsonid(json_object):	
    print(i)

jsonobj(json_object)

print("String")

dictstr(json_object)

print("End")
