import requests
import json
import time
import io





while 1:
    file = open('logtest.txt','a')
    response = requests.get('https://api.nrfcloud.com/v1/messages',headers={'Accept':'application/json','Authorization':'Bearer 6165fe3b2081b2938525929c7da617daa453400d'},params={'inclusiveStart':'2019-09-27T00:00:00Z','exclusiveEnd':'2019-12-30T00:00:00Z','pageLimit':'1'})
    jsonobject = json.loads(response.text)
    print(jsonobject['items'][0]['receivedAt'])
    file.write(jsonobject['items'][0]['receivedAt']+" - ")

    response = requests.get('https://api.nrfcloud.com/v1/devices/nrf-352656100750325',headers={'Accept':'application/json','Authorization':'Bearer 6165fe3b2081b2938525929c7da617daa453400d'})

    #print(response.text)
    jsonobject = json.loads(response.text)
    print(jsonobject['state']['reported']['sessionIdentifier'])
    #print(jsonobject['state']['reported']['DEVICE']['networkInfo'])
    #print(jsonobject['state']['reported']['DEVICE']['deviceInfo'])
    bob = jsonobject['state']['reported']['device']['deviceInfo']
    #print(bob[54:58])
    print(bob['batteryVoltage'])
    file.write(' %s -- '%jsonobject['id'])
    file.write('Battery Voltage:%s\r\n'%bob['batteryVoltage'])
    file.close()
    time.sleep(30)