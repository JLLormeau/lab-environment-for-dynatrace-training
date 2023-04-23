#Design by JLL - Dynatrace
#########################################################################################################
#import re
import json
import requests
import calendar
import os
import urllib3
import csv
import time
import datetime
import os
import re
import sys

##################################
### Environment
##################################
tenant=str(os.getenv('DT_TENANT_URL'))
token=str(os.getenv('DT_API_TOKEN'))
#print(tenant)
#print(token)


##################################
### variables
##################################
#disable the warning
urllib3.disable_warnings()

#API-ENV
DASHBOARDS = '/api/config/v1/dashboards'
API_MZ='/api/config/v1/managementZones'
API_MAINTENANCE='/api/config/v1/maintenanceWindows'
API_NZ='/api/v2/networkZones'
API_TAG='/api/config/v1/autoTags'
API_SLO='/api/v2/slo'
API_SYNT='/api/v1/synthetic/monitors'
API_TOKEN='/api/v1/tokens'
API_REQUESTNAMING='/api/config/v1/service/requestNaming'
API_REQUESTATTRIBUTE='/api/config/v1/service/requestAttributes'
API_CUSTOMALERT='/api/config/v1/anomalyDetection/metricEvents'
API_EXTENSION='/api/config/v1/extensions'
API_K8S_CREDENTIAL='/api/config/v1/kubernetes/credentials'
API_CALC_METRIC='/api/config/v1/calculatedMetrics/service'
API_SYNTH_LOCATION='/api/v1/synthetic/locations'
API_WEB_APP='/api/config/v1/applications/web'
API_ALERTING_PROFILE='/api/config/v1/alertingProfiles'
API_NOTIFICATIONS='/api/config/v1/notifications'

##################################
## GENERIC functions
##################################

def head_with_token(TOKEN):
    http_header = {
    'Accept': 'application/json',
    'Content-Type': 'application/json; charset=UTF-8'
    }
    return http_header
	
# generic function GET to call API with a given uri
def queryDynatraceAPI(uri,TOKEN):
    head=head_with_token(TOKEN)
    jsonContent = None
    #print(uri)
    try:
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
            status='failed'            
    except :
        status='failed'

    return jsonContent

# generic function POST to call API with a given uri
def postDynatraceAPI(uri, payload,TOKEN):
    head=head_with_token(TOKEN)
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
            status='failed'
    except :
         status='failed'
    #print(jsonContent,status)
    #For successful API call, response code will be 200 (OK)
    return (jsonContent,status)


# generic function PUT to call API with a given uri
def putDynatraceAPI(uri, payload,TOKEN):
    head=head_with_token(TOKEN)
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
            status='failed'
    except :
         status='failed'
    # For successful API call, response code will be 200 (OK)

    return (jsonContent,status)

# generic function del to call API with a given uri
def delDynatraceAPI(uri,TOKEN):
    head=head_with_token(TOKEN)
    jsonContent = None
    #print(uri)
    status='success'
    try:
        response = requests.delete(uri,headers=head,verify=False)
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
            status='failed'
    except :
         status='failed'
    # For successful API call, response code will be 200 (OK)

    return (jsonContent,status)

##################################
### functions###
##################################

# dashboard to clean
def dashboard_clean(TENANT,TOKEN):
    print('clean dashboard')
    uri=TENANT + DASHBOARDS + '?Api-Token=' +TOKEN
    #print(uri)
    datastore = queryDynatraceAPI(uri, TOKEN)
    #print(datastore)
    dashboards = datastore.get('dashboards')
    for dashboard in dashboards:
        id = dashboard.get('id')
        name = dashboard.get('name')
        owner = dashboard.get('owner')
        if owner != 'Dynatrace':
            uri = TENANT + DASHBOARDS + '/' + id + '?Api-Token=' + TOKEN
            delDynatraceAPI(uri, TOKEN)
            print('delete ' +name+ '    '+id)
    return ()

# management zones to clean
def mz_clean(TENANT,TOKEN):
    print('clean mz')
    uri=TENANT + API_MZ + '?Api-Token=' +TOKEN
    #print(uri)
    datastore = queryDynatraceAPI(uri, TOKEN)
    #print(datastore)
    if datastore != []:
        apilist = datastore['values']
        for entity in apilist:
            uri = TENANT + API_MZ + '/' + entity['id'] + '?Api-Token=' + TOKEN
            print('delete ' +entity['name']+ '    '+entity['id'])
            delDynatraceAPI(uri, TOKEN)
    return ()



# maintenance windows to clean
def mw_clean(TENANT,TOKEN):
    print('clean mw')
    uri=TENANT + API_MAINTENANCE + '?Api-Token=' +TOKEN
    #print(uri)
    datastore = queryDynatraceAPI(uri, TOKEN)
    #print(datastore)
    if datastore != []:
        apilist = datastore['values']
        for entity in apilist:
            uri = TENANT + API_MAINTENANCE + '/' + entity['id'] + '?Api-Token=' + TOKEN
            print('delete ' +entity['name']+ '    '+entity['id'])
            delDynatraceAPI(uri, TOKEN)
    return ()

# network zone to clean
def nz_clean(TENANT,TOKEN):
    print('clean nz')
    uri=TENANT + API_NZ + '?Api-Token=' +TOKEN
    #print(uri)
    datastore = queryDynatraceAPI(uri, TOKEN)
    #print(datastore)
    if datastore != []:
        apilist = datastore['networkZones']
        for entity in apilist:
            if entity['id'] != 'default':
                uri = TENANT + API_NZ + '/' + entity['id'] + '?Api-Token=' + TOKEN
                print('delete '+entity['id'])
                delDynatraceAPI(uri, TOKEN)
    return ()
    
# auto_tag to clean
def tag_clean(TENANT,TOKEN):
    print('clean autotag')
    uri=TENANT + API_TAG + '?Api-Token=' +TOKEN
    #print(uri)
    datastore = queryDynatraceAPI(uri, TOKEN)
    #print(datastore)
    if datastore != []:
        apilist = datastore['values']
        for entity in apilist:
            if entity['id'] != 'default':
                uri = TENANT + API_TAG + '/' + entity['id'] + '?Api-Token=' + TOKEN
                print('delete ' +entity['name']+'  '+entity['id'])
                delDynatraceAPI(uri, TOKEN)
    return ()

# slo to clean
def slo_clean(TENANT,TOKEN):
    print('clean slo')
    uri=TENANT + API_SLO + '?pageSize=500&Api-Token=' +TOKEN
    #print(uri)
    datastore = queryDynatraceAPI(uri, TOKEN)
    #print(datastore)
    if datastore != []:
        apilist = datastore['slo']
        for entity in apilist:
            if entity['id'] != 'default':
                uri = TENANT + API_SLO + '/' + entity['id'] + '?Api-Token=' + TOKEN
                print('delete ' +entity['name']+'  '+entity['id'])
                delDynatraceAPI(uri, TOKEN)
    return ()

# synthetic to clean
def synth_clean(TENANT,TOKEN):
    print('clean synthetic')
    uri=TENANT + API_SYNT + '?Api-Token=' +TOKEN
    #print(uri)
    datastore = queryDynatraceAPI(uri, TOKEN)
    #print(datastore)
    if datastore != []:
        apilist = datastore['monitors']
        for entity in apilist:
                uri = TENANT + API_SYNT + '/' + entity['entityId'] + '?Api-Token=' + TOKEN
                print('delete ' +entity['name']+'  '+entity['entityId'])
                delDynatraceAPI(uri, TOKEN)
    return ()

# token to clean
def token_clean(TENANT,TOKEN):
    print('clean token')
    uri=TENANT + API_TOKEN + '?Api-Token=' +TOKEN
    #print(uri)
    datastore = queryDynatraceAPI(uri, TOKEN)
    #print(datastore)
    if datastore != []:
        apilist = datastore['values']
        for entity in apilist:
            if not token.startswith(entity['id']) and not entity['name'].startswith('donotdelete'):
                #print(entity['id'], entity['name'])
                uri = TENANT + API_TOKEN + '/' + entity['id'] + '?Api-Token=' + TOKEN
                print('delete ' +entity['name']+'  '+entity['id'])
                delDynatraceAPI(uri, TOKEN)
    return ()

# request naming to clean
def requestnaming_clean(TENANT,TOKEN):
    print('clean request naming')
    uri=TENANT + API_REQUESTNAMING + '?Api-Token=' +TOKEN
    #print(uri)
    datastore = queryDynatraceAPI(uri, TOKEN)
    #print(datastore)
    if datastore != []:
        apilist = datastore['values']
        for entity in apilist:
                uri = TENANT + API_REQUESTNAMING + '/' + entity['id'] + '?Api-Token=' + TOKEN
                print('delete ' +entity['name']+'  '+entity['id'])
                delDynatraceAPI(uri, TOKEN)
    return ()



# request attribute to clean
def requestattribute_clean(TENANT,TOKEN):
    print('clean request attribute')
    uri=TENANT + API_REQUESTATTRIBUTE + '?Api-Token=' +TOKEN
    #print(uri)
    datastore = queryDynatraceAPI(uri, TOKEN)
    #print(datastore)
    if datastore != []:
        apilist = datastore['values']
        for entity in apilist:
                uri = TENANT + API_REQUESTATTRIBUTE + '/' + entity['id'] + '?Api-Token=' + TOKEN
                print('delete ' +entity['name']+'  '+entity['id'])
                delDynatraceAPI(uri, TOKEN)
    return ()


# custom alert to clean
def customevent_foralerting(TENANT,TOKEN):
    print('clean custom alert')
    uri=TENANT + API_CUSTOMALERT + '?Api-Token=' +TOKEN
    #print(uri)
    datastore = queryDynatraceAPI(uri, TOKEN)
    #print(datastore)
    if datastore != []:
        apilist = datastore['values']
        for entity in apilist:
            if len(entity['id'].split(".")) == 1 :
                    uri = TENANT + API_CUSTOMALERT + '/' + entity['id'] + '?Api-Token=' + TOKEN
                    print('delete ' +entity['name']+'  '+entity['id'])
                    delDynatraceAPI(uri, TOKEN)
           
    return ()


# custom extension to clean
def custom_extension(TENANT,TOKEN):
    print('clean custom extension')
    uri=TENANT + API_EXTENSION + '?Api-Token=' +TOKEN
    #print(uri)
    datastore = queryDynatraceAPI(uri, TOKEN)
    #print(datastore)
    if datastore != []:
        apilist = datastore['extensions']
        for entity in apilist:
            if entity['id'].startswith('custom') and entity['type'] == 'JMX':
                    uri = TENANT + API_EXTENSION + '/' + entity['id'] + '?Api-Token=' + TOKEN
                    print('delete ' +entity['name']+'  '+entity['id'])
                    delDynatraceAPI(uri, TOKEN)
           
    return ()


# custom k8s config to clean
def custom_k8sconfig(TENANT,TOKEN):
    print('clean k8s config')
    uri=TENANT + API_K8S_CREDENTIAL + '?Api-Token=' +TOKEN
    #print(uri)
    datastore = queryDynatraceAPI(uri, TOKEN)
    #print(datastore)
    if datastore != []:
        apilist = datastore['values']
        for entity in apilist:
                    uri = TENANT + API_K8S_CREDENTIAL + '/' + entity['id'] + '?Api-Token=' + TOKEN
                    print('delete ' +entity['name']+'  '+entity['id'])
                    delDynatraceAPI(uri, TOKEN)
           
    return ()


# custom calculated service metric to clean
def custom_calcmetric(TENANT,TOKEN):
    print('clean calculated service metric')
    uri=TENANT + API_CALC_METRIC + '?Api-Token=' +TOKEN
    #print(uri)
    datastore = queryDynatraceAPI(uri, TOKEN)
    #print(datastore)
    if datastore != []:
        apilist = datastore['values']
        for entity in apilist:
                    uri = TENANT + API_CALC_METRIC + '/' + entity['id'] + '?Api-Token=' + TOKEN
                    print('delete ' +entity['name']+'  '+entity['id'])
                    delDynatraceAPI(uri, TOKEN)


# request synthetic location  to clean
def synthloaction_clean(TENANT,TOKEN):
    print('clean synthetic location')
    uri=TENANT + API_SYNTH_LOCATION + '?Api-Token=' +TOKEN
    #print(uri)
    datastore = queryDynatraceAPI(uri, TOKEN)
    #print(datastore)
    if datastore != []:
        apilist = datastore['locations']
        for entity in apilist:
                if entity['type'] == "PRIVATE":
                    uri = TENANT + API_SYNTH_LOCATION + '/' + entity['entityId'] + '?Api-Token=' + TOKEN
                    print('delete ' +entity['name']+'  '+entity['entityId'])
                    delDynatraceAPI(uri, TOKEN)
    return ()

# request web app to clean
def webapp_clean(TENANT,TOKEN):
    print('clean web app')
    uri=TENANT + API_WEB_APP + '?Api-Token=' +TOKEN
    #print(uri)
    datastore = queryDynatraceAPI(uri, TOKEN)
    #print(datastore)
    if datastore != []:
        apilist = datastore['values']
        for entity in apilist:
                    uri = TENANT + API_WEB_APP + '/' + entity['id'] + '?Api-Token=' + TOKEN
                    print('delete ' +entity['name']+'  '+entity['id'])
                    delDynatraceAPI(uri, TOKEN)
    return ()

# request alertingprofile  to clean
def alertingprofile_clean(TENANT,TOKEN):
    print('clean alerteing  profile')
    uri=TENANT + API_ALERTING_PROFILE + '?Api-Token=' +TOKEN
    #print(uri)
    datastore = queryDynatraceAPI(uri, TOKEN)
    #print(datastore)
    if datastore != []:
        apilist = datastore['values']
        for entity in apilist:
                if entity['name'] != 'Default':
                    uri = TENANT + API_ALERTING_PROFILE + '/' + entity['id'] + '?Api-Token=' + TOKEN
                    print('delete ' +entity['name']+'  '+entity['id'])
                    delDynatraceAPI(uri, TOKEN)
    return ()

# request notification  to clean
def alertingprofile_clean(TENANT,TOKEN):
    print('clean alerting  profile')
    uri=TENANT + API_ALERTING_PROFILE + '?Api-Token=' +TOKEN
    #print(uri)
    datastore = queryDynatraceAPI(uri, TOKEN)
    #print(datastore)
    if datastore != []:
        apilist = datastore['values']
        for entity in apilist:
                if entity['name'] != 'Default':
                    uri = TENANT + API_ALERTING_PROFILE + '/' + entity['id'] + '?Api-Token=' + TOKEN
                    print('delete ' +entity['name']+'  '+entity['id'])
                    delDynatraceAPI(uri, TOKEN)
    return ()

# request notifications  to clean
def notifications_clean(TENANT,TOKEN):
    print('clean notifications')
    uri=TENANT + API_NOTIFICATIONS + '?Api-Token=' +TOKEN
    #print(uri)
    datastore = queryDynatraceAPI(uri, TOKEN)
    #print(datastore)
    if datastore != []:
        apilist = datastore['values']
        for entity in apilist:
                if entity['name'] != 'Default':
                    uri = TENANT + API_NOTIFICATIONS + '/' + entity['id'] + '?Api-Token=' + TOKEN
                    print('delete ' +entity['name']+'  '+entity['id'])
                    delDynatraceAPI(uri, TOKEN)
    return ()

#Clean
print(tenant)
print()

#Clean
print(tenant)
print()


dashboard_clean(tenant,token)
mz_clean(tenant,token)
mw_clean(tenant,token)
nz_clean(tenant,token)
tag_clean(tenant,token)
slo_clean(tenant,token)
synth_clean(tenant,token)
token_clean(tenant,token)
requestnaming_clean(tenant,token)
requestattribute_clean(tenant,token)
customevent_foralerting(tenant,token)
custom_extension(tenant,token)
custom_k8sconfig(tenant,token)
custom_calcmetric(tenant,token)
synthloaction_clean(tenant,token)
webapp_clean(tenant,token)
alertingprofile_clean(tenant,token)
notifications_clean(tenant,token)
    
#manque  mda, logs config, logs event, availability process for mongo
