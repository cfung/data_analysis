#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
import pprint
import re
import codecs
import json
import sys
"""
Your task is to wrangle the data and transform the shape of the data
into the model we mentioned earlier. The output should be a list of dictionaries
that look like this:

{
"id": "2406124091",
"type: "node",
"visible":"true",
"created": {
          "version":"2",
          "changeset":"17206049",
          "timestamp":"2013-08-03T16:43:42Z",
          "user":"linuxUser16",
          "uid":"1219059"
        },
"pos": [41.9757030, -87.6921867],
"address": {
          "housenumber": "5157",
          "postcode": "60625",
          "street": "North Lincoln Ave"
        },
"amenity": "restaurant",
"cuisine": "mexican",
"name": "La Cabana De Don Luis",
"phone": "1 (773)-271-5176"
}

You have to complete the function 'shape_element'.
We have provided a function that will parse the map file, and call the function with the element
as an argument. You should return a dictionary, containing the shaped data for that element.
We have also provided a way to save the data in a file, so that you could use
mongoimport later on to import the shaped data into MongoDB. 

Note that in this exercise we do not use the 'update street name' procedures
you worked on in the previous exercise. If you are using this code in your final
project, you are strongly encouraged to use the code from previous exercise to 
update the street names before you save them to JSON. 

In particular the following things should be done:
- 1. you should process only 2 types of top level tags: "node" and "way"
- 2. all attributes of "node" and "way" should be turned into regular key/value pairs, except:
    - attributes in the CREATED array should be added under a key "created"
    - attributes for latitude and longitude should be added to a "pos" array,
      for use in geospacial indexing. Make sure the values inside "pos" array are floats
      and not strings. 
- 3. if second level tag "k" value contains problematic characters, it should be ignored
- 4. if second level tag "k" value starts with "addr:", it should be added to a dictionary "address"
- 5. if second level tag "k" value does not start with "addr:", but contains ":", you can process it
  same as any other tag.
- 6. if there is a second ":" that separates the type/direction of a street,
  the tag should be ignored, for example:

<tag k="addr:housenumber" v="5158"/>
<tag k="addr:street" v="North Lincoln Avenue"/>
<tag k="addr:street:name" v="Lincoln"/>
<tag k="addr:street:prefix" v="North"/>
<tag k="addr:street:type" v="Avenue"/>
<tag k="amenity" v="pharmacy"/>

  should be turned into:

{...
"address": {
    "housenumber": 5158,
    "street": "North Lincoln Avenue"
}
"amenity": "pharmacy",
...
}

- for "way" specifically:

  <nd ref="305896090"/>
  <nd ref="1719825889"/>

should be turned into
"node_refs": ["305896090", "1719825889"]
"""


lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

CREATED = [ "version", "changeset", "timestamp", "user", "uid"]


def shape_element(element):
    node = {}
    node["created"] = {}
    node["address"] = {}
    node["node_refs"] = []
    node["pos"] = []
    counter = 0

    #print " $$$$$$$$$$$$$$$$$$$$$$$$$$$$$  node number.." + str(counter) 

    if element.tag == "node" or element.tag == "way" :
        # YOUR CODE HERE
        for tag in element.iter():

            
            #sys.stdout.write(element.tag)
            #print tag.items()
            print "what is tag items....", tag.items()
            if tag.keys()[0] == "k":
              print "found k", tag.items()
              #node["address"] = {}

              for i in range(len(tag.items())):
                # if it's house #
                print "what is i item....?????", tag.items()[i][0]
                print "item 0 is...", item[0]
                print "item 1 is...", item[1][:4]
                #print "index..", index
                #node["address"][item[0]] = item[1]
                print "end..."

                if tag.items()[i][1][:16] == "addr:housenumber":
                  print "******************  FOUND ADDR house number !!! *****************" 
                  node["address"]["housenumber"] = tag.items()[i+1][1]
                  print "what is housenumber?", node["address"]["housenumber"]


                if tag.items()[i][1][:11] == "addr:street" and len(tag.items()[i][1])==11 :
                  print "******************  FOUND street!!! *****************" 
                  node["address"]["street"] = tag.items()[i+1][1]
                  print "what is street name?", node["address"]["street"]


                if tag.items()[i][1][:13] == "addr:postcode":
                  print "******************  FOUND post code number !!! *****************" 
                  node["address"]["postcode"] = tag.items()[i+1][1]
                  print "what is postcode?", node["address"]["postcode"]

                #if item[0] == 'v'
                # if it's street
                #  node["address"][]
                #print "node is.."
                #pprint.pprint(node)


            elif tag.keys()[0] == "changeset":
              print "found changeset"
              for item in tag.items():

                if item[0] == 'changeset':
                  node["created"]["changeset"] = item[1]

                elif item[0] == 'lon' or item[0] == 'lat':
                  print "found pos...", item[1]
                  node['pos'].append(float(item[1]))
                  print node['pos']
                  #print type(node['pos'])

                elif item[0] == 'timestamp':
                  node['created'][item[0]] = item[1]

                elif item[0] == 'uid':
                  node['created'][item[0]] = item[1]

                elif item[0] == 'id':
                  node[item[0]] = item[1]

                elif item[0] == 'version':
                  node['created'][item[0]] = item[1]

                elif item[0] == 'user':
                  node['created'][item[0]] = item[1]

                elif item[0] == 'visible':
                  node[item[0]] = item[1]

                

                #elif item[0] == 'type':
                #  print "found type !!!"
                node['type'] = element.tag

                print "item in changeset....", item
              print "node is...", node


            elif tag.keys()[0] == "ref":
              #node["node_refs"] = []
              print "found ref"
              for item in tag.items():

                node["node_refs"].append(item[1])
                print "type of item..", type(item)
                print "node in ref is....", node

        counter += 1


        print "**************** final check before retuning ******"
        index_to_delete = []
        for element in node:
          print "dict keys value..", element
          if not node[element]:
            print "empty !!!!", node[element]
            index_to_delete.append(element)
            #node.pop(element)

        print "what is index_to_delete list..", index_to_delete

        for item_delete in index_to_delete:
          #node.pop(item_delete)
          print "what is item_delete...", item_delete
          node.pop(item_delete)

        print "**************** final check before retuning ******"

        return node
    else:
        return None


def process_map(file_in, pretty = False):
    # You do not need to change this file
    counter = 0
    file_out = "{0}.json".format(file_in)
    data = []
    with codecs.open(file_out, "w") as fo:
        for _, element in ET.iterparse(file_in):
            print "$$$$$$$$$$$$$$$$$ counter..", counter

            el = shape_element(element)
            if el:
                data.append(el)
                if pretty:
                    fo.write(json.dumps(el, indent=2)+"\n")
                else:
                    fo.write(json.dumps(el) + "\n")
            counter += 1
            print "$$$$$$$$$$ data at counter...", data#pprint.pprint(data)
    return data

def test():
    # NOTE: if you are running this code on your computer, with a larger dataset, 
    # call the process_map procedure with pretty=False. The pretty=True option adds 
    # additional spaces to the output, making it significantly larger.
    data = process_map('example.osm', True)
    #pprint.pprint(data)
    
    correct_first_elem = {
        "id": "261114295", 
        "visible": "true", 
        "type": "node", 
        "pos": [-87.6866303, 41.9730791], 
        "created": {
            "changeset": "11129782", 
            "user": "bbmiller", 
            "version": "7", 
            "uid": "451048", 
            "timestamp": "2012-03-28T18:31:23Z"
        }
    }

    #[('changeset', '11129782'), ('uid', '451048'), ('timestamp', '2012-03-28T18:31:23Z'), 
    #('lon', '-87.6866303'), ('visible', 'true'), ('version', '7'), ('user', 'bbmiller'), 
    #('lat', '41.9730791'), ('id', '261114295')]

    '''
    {'created': {'changeset': '11129782',
             'timestamp': '2012-03-28T18:31:23Z',
             'uid': '451048',
             'user': 'bbmiller',
             'version': '7'},
      'id': '261114295',
      'pos': [-87.6866303, 41.9730791],
      'type': 'node',
      'visible': 'true'}


    '''

    pprint.pprint(data[0])
    print "what is data -1?"
    pprint.pprint(data[-1])
    assert data[0] == correct_first_elem
    assert data[-1]["address"] == {
                                    "street": "West Lexington St.", 
                                    "housenumber": "1412"
                                      }
    assert data[-1]["node_refs"] == [ "2199822281", "2199822390",  "2199822392", "2199822369", 
                                    "2199822370", "2199822284", "2199822281"]

if __name__ == "__main__":
    test()