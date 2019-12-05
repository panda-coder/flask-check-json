#!/usr/bin/env python3

import sys
sys.path.append("..") # Adds higher directory to python modules path.

from flask_check_json import validator

schema = {
  "type": "object",
  "properties": {
    "number":      { "type": "number" },
    "street_name": { "type": "string" },
    "street_type": { "type": "string",
                     "enum": ["Street", "Avenue", "Boulevard"]
                   }
  }
}

try:
    test1 = {"number": 1600, "street_name": "Pennsylvania", "street_type": "Avenue"}
    validator.validate_schema(schema, data=test1)
    print("Teste1 passed")
except Exception:
    print("Teste1 failed")


try:
    test2 = {"number": "1600", "street_name": "Pennsylvania", "street_type": "Avenue"}
    validator.validate_schema(schema, data=test2)
    print("Teste2 failed")
except Exception:
    print("Teste2 passed")