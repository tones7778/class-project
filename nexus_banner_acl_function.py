import requests
import json


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

if __name__ == '__main__':

    url='http://192.168.10.60/ins'
    switchuser='admin'
    switchpassword='Passw0rd1'

    createAcls()
    createBanner()