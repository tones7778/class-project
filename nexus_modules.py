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

    payload2={
      "ins_api": {
        "version": "1.0",
        "type": "cli_show",
        "chunk": "0",
        "sid": "1",
        "input": "show hostname",
        "output_format": "json"
      }
    }

    response2 = requests.post(url,data=json.dumps(payload2), headers=myheaders,auth=(username,password)).json()
    new_name = str(response2[u'ins_api'][u'outputs'][u'output'][u'body'][u'hostname'])
    print ("New hostname has been successfully pushed to the switch and is now " + new_name.upper())

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

def createBanner():

    #url='http://192.168.10.60/ins'
    #switchuser='admin'
    #switchpassword='Passw0rd1'

    myheaders={'content-type':'application/json'}
    payload={
      "ins_api": {
        "version": "1.0",
        "type": "cli_conf",
        "chunk": "0",
        "sid": "1",
        #"input": "banner motd ^ ;   _      _ ;  : `.--.' ;              _....,_ ;  .'      `.      _..--'\"'       `-._ ; :          :_.-'\"                  .`. ; :  6    6  :                     :  '.; ; :          :                      `..'; ; `: .----. :'                          ; ;   `._Y _.'               '           ; ;     'U'      .'          `.         ; ;        `:   ;`-..___       `.     .'`. ; hi     _:   :  :    ```\"''\"'``.    `.  `. ;      .'     ;..'            .'       `.'` ;     `.......'              `........-'` ;------------------------------------------------;^",
        "input": "banner motd ^My lame banner in one line^",
        #"input": "banner motd ^My lame \\\n banner in\\\n two line\\\n^\\\n",
        "output_format": "json"
      }
    }
    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()

def createAcls():

    #url='http://192.168.10.60/ins'
    #switchuser='admin'
    #switchpassword='Passw0rd1'

    myheaders={'content-type':'application/json'}
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

def loggingconf():

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
        "input": "conf t ;logging server 10.10.10.10",
        "output_format": "json"
      }
    }
    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()

def add_dns():
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
        "input": "conf t ;ip dns source-interface ethernet 1/5",
        "output_format": "json"
      }
    }
    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()


def add_timezone():
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
