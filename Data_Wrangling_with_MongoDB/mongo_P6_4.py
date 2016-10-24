#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
import pprint
import re
"""
Your task is to explore the data a bit more.
The first task is a fun one - find out how many unique users
have contributed to the map in this particular area!

The function process_map should return a set of unique user IDs ("uid")
"""

def get_user(element):
	uid = ""

	#if element.tag == "node":
	#	for tag in element.iter():
	uid = tag.get('uid')
    
    return uid


def process_map(filename):
    users = set()
    for _, element in ET.iterparse(filename):
        users.add(get_user(element))

    return users


def test():

    users = process_map('example.osm')
    pprint.pprint(users)
    assert len(users) == 6



if __name__ == "__main__":
    test()


'''

def key_type(element, keys):
    if element.tag == "tag":
        # YOUR CODE HERE
        for tag in element.iter():
            if re.search(problemchars, tag.get('k')):
                keys["problemchars"] += 1
            elif re.search(lower_colon, tag.get('k')):
                keys["lower_colon"] += 1
            elif re.search(lower, tag.get('k')):
                keys["lower"] += 1
            else:
                keys["other"] += 1
    
    print "keys is..", keys 

    return keys



def process_map(filename):
    keys = {"lower": 0, "lower_colon": 0, "problemchars": 0, "other": 0}
    for _, element in ET.iterparse(filename):
        keys = key_type(element, keys)

    return keys
