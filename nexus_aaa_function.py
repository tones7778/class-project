import requests
import json

# changes to the NXOSv
def add_admin_account():
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
        "input": "conf t ;username sysadmin password 0 Passw0rd1 role network-admin",
        "output_format": "json"
      }
    }
    response = requests.post(url, data=json.dumps(payload), headers=myheaders, auth=(switchuser,switchpassword)).json()
    print(response)


if __name__ == "__main__":
    add_admin_account()
