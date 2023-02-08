#Designed by Dynatrace
#########################################################################################################
import json
import requests
import calendar
import os
import urllib3
import csv
import time
import os
import sys


##################################
### Environment
##################################
tenant='https://'+str(os.getenv('MyTenant'))
token=str(os.getenv('MyToken'))

##################################
### variables
##################################
##File variable to be changed if script is run on Windows or Linux. '\\' for Windows, '/' for Linux
#DIRECTORY='./'#Linux

#disable the warning
urllib3.disable_warnings()

#API-ENV
API_ENTITY='/api/v2/entities?entitySelector=type("PROCESS_GROUP")'
API_ANOMALYDETECTION='/api/config/v1/anomalyDetection/processGroups/'

dict_pg=dict()

##################################
## GENERIC functions
##################################

head = {
    'Accept': 'application/json',
    'Content-Type': 'application/json; charset=UTF-8'
    }
	
# generic function GET to call API with a given uri
def queryDynatraceAPI(uri):
    jsonContent = None
    #print(uri)
    response = requests.get(uri,headers=head,verify=False)
    # For successful API call, response code will be 200 (OK)
    if(response.ok):
        if(len(response.text) > 0):
            jsonContent = json.loads(response.text)
    else:
        jsonContent = json.loads(response.text)
        print(jsonContent)
        errorMessage = ''
        if(jsonContent['error']):
            errorMessage = jsonContent['error']['message']
            print('Dynatrace API returned an error: ' + errorMessage)
        jsonContent = None
        raise Exception('Error', 'Dynatrace API returned an error: ' + errorMessage)

    return jsonContent

# generic function POST to call API with a given uri
def postDynatraceAPI(uri, payload):
    jsonContent = None
    status='success'
    #print(uri)
    try:
        response = requests.post(uri,headers=head,verify=False, json=payload)
        if(response.ok):
            if(len(response.text) > 0):
                jsonContent = json.loads(response.text)
        else:
            jsonContent = json.loads(response.text)
            print(jsonContent)
            errorMessage = ''
            if (jsonContent['error']):
                errorMessage = jsonContent['error']['message']
                print('Dynatrace API returned an error: ' + errorMessage)
            jsonContent = None
            raise Exception('Error', 'Dynatrace API returned an error: ' + errorMessage)

    except :
         status='failed'
    #print(jsonContent,status)
    #For successful API call, response code will be 200 (OK)
    return (jsonContent,status)


# generic function PUT to call API with a given uri
def putDynatraceAPI(uri, payload):
    jsonContent = None
    #print(uri)
    status='success'
    try:
        response = requests.put(uri,headers=head,verify=False, json=payload)
        if(response.ok):
            if(len(response.text) > 0):
                jsonContent = json.loads(response.text)
        else:
            jsonContent = json.loads(response.text)
            print(jsonContent)
            errorMessage = ''
            if (jsonContent['error']):
                errorMessage = jsonContent['error']['message']
                print('Dynatrace API returned an error: ' + errorMessage)
            jsonContent = None
            raise Exception('Error', 'Dynatrace API returned an error: ' + errorMessage)

    except :
         status='failed'
    # For successful API call, response code will be 200 (OK)

    return (jsonContent,status)

##################################
### INFO functions###
##################################

def list_pgavailability(tenant,token,action):

    uri = tenant + API_ENTITY + ',entityName("Mongodb")'+ '&Api-Token=' + token


    print(uri)
    datastore = queryDynatraceAPI(uri)
    if int(datastore['totalCount']) > 0:
        entityidlist = datastore['entities']
        for pg in entityidlist:
            print(pg.get('displayName') )

            if action == 'enable':
                print('Enable Process Group availability for MongoDB')
                enable_pgavailability(tenant,token,pg.get('entityId'))
            elif action == 'disable':
                print('Disable Process Group availability for MongoDB')
                disable_pgavailability(tenant,token,pg.get('entityId'))
            
    return()

def enable_pgavailability(tenant,token,pg_id):
    uri = tenant + API_ANOMALYDETECTION + pg_id + '?Api-Token=' + token
    #print(uri)
    payload ={
          "availabilityMonitoring": {
            "method": "PROCESS_IMPACT"
          }
        }
    result=putDynatraceAPI(uri, payload)
    #print(uri, payload)
    print(result[1])   
    return()


def disable_pgavailability(tenant,token,pg_id):
    uri = tenant + API_ANOMALYDETECTION + pg_id + '?Api-Token=' + token
    #print(uri)
    payload ={
          "availabilityMonitoring": {
            "method": "OFF"
          }
        }
    result=putDynatraceAPI(uri, payload)
    #print(uri, payload)
    print(result[1])   
    return()


#############
#Main Program
#############
arg=''

if len(sys.argv) > 1:
    arg=sys.argv[1]
    #print(' => argument'+ arg)
                

##For each tenant
if arg not in ['enable', 'disable'] :
    print(' bad argument: must be \'enable\' or \'disable\'')

else : 
    
    list_pgavailability(tenant,token,str(arg))


 
#if os.name == 'nt':
#    os.system("pause")
    
