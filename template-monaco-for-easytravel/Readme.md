# Monaco

You will import :  
- application-web 
- app-detection-rule 
- management-zone
- autotag
- alerting-profile 
- notification
- maintenance-window
- host-naming
- processgroup-naming
- sevice-naming
- dashboard
- synthetic
- calculated service metric
- slo

1) your variables  
	   
	   export NEW_CLI=1
	   export MyTenant=<YYYY>.live.dynatrace.com
	   export MyToken=<dt.1234567890>
	   export Appname=easytravel<XX>
	   export Hostname=dynatracelab<XX>.<AzureRegion>.cloudapp.azure.com
	   export Email=<your email of Dynatrace saas tenant connection>
	   export EnableSynthetic=true
  
2) validate the env variables 

       echo "NEW_CLI="$NEW_CLI;echo "MyTenant=https://"$MyTenant;echo "MyToken="$MyToken;echo "Appname="$Appname;echo "Hostname="$Hostname;echo "Email="$Email; echo "EnableSynthetic="$EnableSynthetic  

3) deploy the configuration 

       cd;cd lab-environment-for-dynatrace-training
       ./monaco deploy -e=environments.yaml template-monaco-for-easytravel/Deploy
       ./monaco deploy -e=environments.yaml template-monaco-for-easytravel/Slo
	 
4) you can delete the configuration here 

       cd;cd lab-environment-for-dynatrace-training
       sed -i 's/Appname/'$Appname'/g' Delete/delete.yaml;./monaco deploy -e=environments.yaml Delete;sed -i 's/'$Appname'/Appname/g' Delete/delete.yaml
