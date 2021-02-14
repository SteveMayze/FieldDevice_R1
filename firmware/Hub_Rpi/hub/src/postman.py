url = "https://b0o5r0vxkz5ekbo-db202011271753.adb.eu-frankfurt-1.oraclecloudapps.com/ords/leawood_dev/api/1.0/data_points"

payload="{\n    \"address\": \"0013A20041629BFB\",\n    \"label\": \"bus-voltage\",\n    \"value\": 13.46\n}"
headers = {
  'Authorization': 'Basic UkVTVF9VU0VSOjVidko5ZFUjJEdhZw==',
  'Content-Type': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
