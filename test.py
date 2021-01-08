import json
import requests
import pandas as pd

url = "http://localhost:5001/matrixapi/col"

payload = {"rowids": ["A1CF", "AAAS", "A2M"], "colids": ["ABHD1", "ABO", "doesnetexist"]}
response = requests.post(url, json=payload)
data = json.loads(response.text)
print(data)

response = requests.post("http://localhost:5001/matrixapi/slice", json=payload)