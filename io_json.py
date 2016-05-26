# -*- coding: utf-8 -*-
"""
Created on Thu May 26 08:06:23 2016

@author: Jorge
"""

import json

json_data = """
{
  "address":{
    "streetAddress": "21 2nd Street",
    "city":"New York",
    "houseNumber":12
  },
  "phoneNumber":
    [
    {
      "type":"home",
      "number":"212 555-1234"
    }
  ]
}
"""

loaded_data = json.loads(json_data)

print(loaded_data['address'])
print(loaded_data['address']['city'])