import requests
import json

"""
Modify
"""
url='http://192.168.10.60/ins'
switchuser='admin'
switchpassword='Passw0rd1'

myheaders = {'Content-Type': 'application/json',}

payload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_conf",
    "chunk": "0",
    "sid": "1",
    "input": "conf t ;clock timezone EST -5 0",
    "output_format": "json"
  }
}
response = requests.post(url, data=json.dumps(payload), headers=myheaders, auth=(switchuser, switchpassword)).json()
