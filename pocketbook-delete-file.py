#!/usr/bin/env python3
import requests
import sys

if len(sys.argv) <= 2:
    print("no hash??\n <bearer_token> <hash>")
    exit(-1)


hash = str(sys.argv[2])
BEARER_TOKEN=str(sys.argv[1])

url = "https://cloud.pocketbook.digital/api/v1.1/fileops/delete/?fast_hash=" + hash

payload = {}
headers = {
  'Authorization': 'Bearer ' + BEARER_TOKEN
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
