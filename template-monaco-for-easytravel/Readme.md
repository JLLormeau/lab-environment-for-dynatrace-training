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

1) your variables  
	   
	#Export variables Env
	export DT_TENANT_URL=https://abcd.live.dynatrace.com
	export DT_API_TOKEN=XXXX

	#Export variables appli
	export Appname=easytravelxx
	export Hostname=zzzz.yyyy.cloudapp.azure.com
	export Email=myemail@email.com
  
2) validate env variables 

       echo "DT_TENANT_URL="$DT_TENANT_URL;echo "DT_API_TOKEN="$DT_API_TOKEN;echo "Appname="$Appname;echo "Hostname="$Hostname;echo "Email="$Email;
       
3) deploy configuration 

       cd;cd lab-environment-for-dynatrace-training
       ./monaco deploy manifest.yaml

