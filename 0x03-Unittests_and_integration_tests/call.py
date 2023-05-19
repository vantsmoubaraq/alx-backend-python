#!/usr/bin/env python3

import requests
import json

response = requests.get("http://example.com")

try:
    data = json.loads(response.text)
    # JSON is valid, proceed with further processing
except json.JSONDecodeError as e:
    print("Invalid JSON:", e)
