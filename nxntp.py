import requests
import json

def add_ntp():
    url = 'http://192.168.10.60/ins'
    switchuser = 'admin'
    switchpassword = 'Passw0rd1'

    myheaders={'content-type':'application/json'}
    payload={
      "ins_api": {
        "version": "1.0",
        "type": "cli_conf",
        "chunk": "0",
        "sid": "1",
        "input": "config t  ;ntp server 165.115.38.100",
        "output_format": "json"
      }
    }
    response = requests.post(url,data=json.dumps(payload),headers=myheaders,auth=(switchuser,switchpassword)).json()

if __name__ == "__main__":

    add_ntp()
