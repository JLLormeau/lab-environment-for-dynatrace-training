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
	echo MyTenant=$MyTenant
	echo MyToken=$MyToken
	export Appname="easytravel"$X$i
	echo Appname=$Appname
	export MZ=$Appname
	export mz_name=$Appname
	export slo_prefix=$Appname
	export Hostname=$DOMAIN_NAME_DEFAULT$X$i"."$LOCATION".cloudapp.azure.com"
	echo Hostname=$Hostname
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
			./monaco deploy -e=environments.yaml template-monaco-for-easytravel/Deploy
			./monaco deploy -e=environments.yaml template-monaco-for-easytravel/ITSM-integration
			./monaco deploy -e=environments.yaml template-monaco-for-easytravel/SLO-alerts
			
	else
			echo "user"$X$i" => response="$response
			echo
	fi
	i=$(($i + 1))

done
