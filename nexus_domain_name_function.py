import requests
import json

def domain_name():


    url='http://192.168.10.60/ins'
    switchuser='admin'
    switchpassword='Passw0rd1'

    myheaders={'content-type':'application/json'}
    payload={
        "ins_api": {
        "version": "1.0",
        "type": "cli_conf",
        "chunk": "0",
        "sid": "1",
        "input": "conf t ;vrf context management ; ip domain-name tony-montana.ca ;ip name-server 10.1.1.1 ;ip name-server 10.2.1.1",
        "output_format": "json"
    }
    }
    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()


