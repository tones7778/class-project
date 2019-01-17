import requests
import json


def modify_ip_and_mask():

    url='http://192.168.10.60/ins'
    switchuser='sysadmin'
    switchpassword='Passw0rd1'

    myheaders={'content-type':'application/json'}
    payload={
      "ins_api": {
        "version": "1.0",
        "type": "cli_conf",
        "chunk": "0",
        "sid": "1",
        "input": "interface mgmt0 ; ip address 192.168.10.60/24 ;vrf context management ; ip route 0/0 192.168.10.10",
        "output_format": "json"
      }
    }
    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()


if __name__ == "__main__":

    modify_ip_and_mask()
