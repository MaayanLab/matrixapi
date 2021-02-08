import json
import requests
import pandas as pd

url = "http://localhost:5001/matrixapi/colid"

# this function will return the colids
payload = {"id": "A1CF"}
response = requests.post(url, json=payload)
data = json.loads(response.text)
print(data)

url = "http://localhost:5001/matrixapi/col"

# this function will return the full column specified
payload = {"id": "A1CF"}
response = requests.post(url, json=payload)
data = json.loads(response.text)
print(data)



# extract sub matrix
payload = {"rowids": ["A1CF", "AAAS", "A2M"], "colids": ["ABHD1", "ABO", "doesnetexist"]}
response = requests.post("http://localhost:5001/matrixapi/slice", json=payload)
data = json.loads(response.text)
print(data)


url = "http://localhost:5001/matrixapi/coltop"

# this function will return the colids
payload = {"id": "A1CF", "count": 20}
response = requests.post(url, json=payload)
data = json.loads(response.text)


print(data)




url = "https://maayanlab.cloud/matrixapi/coltop"
data = ""
# this function will return the colids
payload = {"id": "SOX2", "count": 20}
response = requests.post(url, json=payload)
data = json.loads(response.text)

print(data)

