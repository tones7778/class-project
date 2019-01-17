import requests
import json

url='http://192.168.10.60/ins'
switchuser='admin'
switchpassword='Passw0rd1'
myheaders={'content-type':'application/json'}

def add_hostname():

    payload={
      "ins_api": {
        "version": "1.0",
        "type": "cli_conf",
        "chunk": "0",
        "sid": "1",
        "input": "conf t ;hostname NXOSv2",
        "output_format": "json"
      }
    }

    response = requests.post(url, data=json.dumps(payload), headers=myheaders, auth=(username,password)).json()
    print(response)

def add_admin_account():

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

def add_banner():

    payload={
      "ins_api": {
        "version": "1.0",
        "type": "cli_conf",
        "chunk": "0",
        "sid": "1",

        "input": "banner motd ^My lame banner in one line^",
        "output_format": "json"
      }
    }
    response = requests.post(url, data=json.dumps(payload), headers=myheaders, auth=(switchuser,switchpassword)).json()
    print(response)

def add_acls():

    payload={
      "ins_api": {
        "version": "1.0",
        "type": "cli_conf",
        "chunk": "0",
        "sid": "1",
        "input": "ip access-list 69 ;  10 permit ip 165.115.0.0/16 any  ;  20 permit ip 10.10.10.10/32 any ",
        "output_format": "json"
      }
    }
    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
    print(response)

def add_domain_name():

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
    print(response)

def modify_ip_and_mask():

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
    print(response)

def add_ntp():

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
    print(response)

def add_logging_servers():

    payload={
      "ins_api": {
        "version": "1.0",
        "type": "cli_conf",
        "chunk": "0",
        "sid": "1",
        "input": "conf t ;logging server 10.10.10.10",
        "output_format": "json"
      }
    }
    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
    print(response)

def add_dns():

    payload={
      "ins_api": {
        "version": "1.0",
        "type": "cli_conf",
        "chunk": "0",
        "sid": "1",
        "input": "conf t ;ip dns source-interface ethernet 1/5",
        "output_format": "json"
      }
    }
    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
    print(response)

def add_timezone():

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
    print(response)
