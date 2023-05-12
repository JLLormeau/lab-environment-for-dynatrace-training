export NEW_CLI=1 
export DT_TENANT_URL=https://xxxx.live.dynatrace.com
export DT_API_TOKEN=dt0c01.abcdefghij.abcdefghijklmn
export MyTenant=`echo $DT_TENANT_URL| cut -d '/' -f 3`
export MyToken=$DT_API_TOKEN
export PaasToken=$MyToken
export list_user="user00@demo.com user01@demo.com"
export EnableSynthetic=false
export TIME=`date +%Y%m%d%H%M%S`
export DOMAIN_NAME_DEFAULT=demodomaine$TIME
export DOMAIN_NAME=$DOMAIN_NAME_DEFAULT
export PASSWORD=DummyP@ssword00
export SIZE_LINUX=Standard_B2ms #2 CPU 8 GB
#export SIZE_LINUX=Standard_B4ms #4CPU 16 GB
export SIZE_WINDOWS=Standard_B2ms   #2 CPU 8 GB
export LOCATION4=francecentral
export LOCATION1=westeurope
export LOCATION2=northeurope
export LOCATION3=uksouth
export LOCATION5=eastus #Reserved for the kubernetes lab
export LOCATION6=eastus2 #Reserved for the kubernetes lab
export START_ENV=0
export NBENV=2
#Monaco Integration
export HostGroupName="lab_easytravelxx"
export DomainName="yyy.zzz.dynatrace.com"
export Email="myemail@email.com"
#synthetic location (for live.dynatrace.com)
export PublicSyntheticLocation1="GEOLOCATION-E266126A762728A2" #Paris_AWS
export PublicSyntheticLocation2="GEOLOCATION-8A751DADED5D705A" #Marseille_Azure
#SLO &ITSM Integration
#default application-performance configuration
export application_performance_target=85 #for apdex = 0.85,minimum value of a good apdex
export application_performance_warning=90
export application_performance_burnrate="3.5"
export application_performance_period="-1w"
#default frontendservice_availability configuration
export frontendservice_availability_target=95
export frontendservice_availability_warning=98
export frontendservice_availability_burnrate="3.5"
export frontendservice_availability_period="-1w"
#default metric events
export application_performance_fastburnalert_enable="false" #check the padex is >0,85 befaore enabling the event
export frontendservice_availability_fastburnalert_enable="true"
#alerting profile
export delay_for_real_time_alert=0 #minutes
export delay_for_persitent_problem=60 #minutes
