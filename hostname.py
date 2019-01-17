#!/usr/bin/env python
import requests
import json

def hostname():
    username = 'admin'
    password = 'Passw0rd1'
    mgmt_ip = '192.168.10.60'
    url=str('http://'+ mgmt_ip + '/ins')
    #url='http://192.168.10.60/ins'
    #print (url)
    hostname_var = raw_input('Please enter the hostname of the switch followed by the "Enter" button\n')
    hostname_var_str = str(hostname_var)
    print("You've entered " + hostname_var_str)
    #type(hostname_var_str)
    #print(hostname_var)
    print "Starting to push hostname value to the switch. Please wait..."
    #json_hostname = '"' + 'conf t ;hostname ' + hostname_var_str + '"'
    json_hostname_str = str('conf t ;hostname ' + hostname_var_str)

    myheaders={'content-type':'application/json'}
    payload={
      "ins_api": {
        "version": "1.0",
        "type": "cli_conf",
        "chunk": "0",
        "sid": "1",
        "input": json_hostname_str,
        #"input": "conf t ;hostname NXOSv2",
        "output_format": "json"
      }
    }

    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(username,password)).json()
    print "New hostname has been successfully pushed to the switch"

if __name__=="__main__":
    hostname()



