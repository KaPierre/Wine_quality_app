import requests

# We have put the localhost URL as default, feel free to change it
url = "http://127.0.0.1:5000/predict"

# This a simple example of input
input_simple = {
    "input": [[7.0, 0.27, 0.36, 20.7, 0.045, 45.0, 170.0, 1.001, 3.0, 0.45, 8.8]]
}

res = requests.post(url, json=input_simple)
assert res.status_code == 200
print(res.json())