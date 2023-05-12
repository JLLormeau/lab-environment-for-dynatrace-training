#!/bin/bash
#design by JLLormeau Dynatrace
# version beta

. ../env.sh
DIR_MONACO="template-monaco-for-easytravel"
if [ $START_ENV -lt 1 ]
then
	END_ENV=$(($NBENV - 1))
else
	END_ENV=$(($NBENV-$START_ENV))
fi
response=no
cd ..


i=$START_ENV
while [ $i -le $END_ENV ]
do
        if [ $i -lt 5 ]
        then
                X='0' #from 00 to 04
                LOCATION=$LOCATION1
        fi
        if [ $i -ge 5 ] && [ $i -lt 10 ]
        then
                X='0' #from 05 to 09
                LOCATION=$LOCATION2
        fi
        if [ $i -ge 10 ] && [ $i -lt 15 ]
        then
                X='' #from 10 to 14
                LOCATION=$LOCATION3
        fi
        if [ $i -ge 15 ] && [ $i -lt 20 ]
        then
                X='' #from 10 to 20
                LOCATION=$LOCATION4
        fi
	
	echo ""
	echo "#######################"
	echo user=user$X$i
	echo DT_TENANT_URL=$DT_TENANT_URL
	echo DT_API_TOKEN=$DT_API_TOKEN
	export HostGroupName="lab_easytravel"$X$i
	echo HostGroupName=$HostGroupName
	export MZ=$HostGroupName
	export mz_name=$HostGroupName
	export slo_prefix=$HostGroupName
	export Hostname=$DOMAIN_NAME_DEFAULT$X$i"."$LOCATION".cloudapp.azure.com"
	export DomainName=$Hostname
	echo DomainName=$Hostname
	number_of_email=`echo $list_user | tr -cd '@' | wc -c`
        
	if [  $number_of_email -ge $(( $i + 1 )) ]; then
                export Email=`echo $list_user | cut -d" " -f$(( $i + 1 ))`
        else
                export Email="userdynatrace"$X$i"@gmail.com"
        fi
	echo Email=$Email
	echo EnableSynthetic=$EnableSynthetic
	read  -p "==> redeploy config for user$X$i (y|n):  " response
	
	if [ "$response" = "yes" ] || [ "$response" = "YES" ] || [ "$response" = "Y" ] || [ "$response" = "y" ]; then
	        cat monaco-easytravel/config.yml.ref > monaco-easytravel/config.yml
		sed -i "s/config-id/lab_easytravel$X$i/g" monaco-easytravel/config.yml
		sed -i "s/skip: true/skip: false/g" monaco-easytravel/config.yml
		./monaco deploy -c manifest.yaml -p monaco-easytravel
			
	else
			echo "user"$X$i" => response="$response
			echo
	fi
	i=$(($i + 1))

done
read  -p "==> redeploy simply smarter (y|n):  " response
if [ "$response" = "yes" ] || [ "$response" = "YES" ] || [ "$response" = "Y" ] || [ "$response" = "y" ]; then
	./monaco deploy manifest.yaml -p monaco-simply-smarter
fi
