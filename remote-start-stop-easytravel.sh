#!/bin/bash
#design by JLLormeau Dynatrace
# version beta

. ./env.sh
response=$1
END_ENV=$(($START_ENV + $NBENV))


while [[ $response != "stress" ]] && [[ $response != "restart" ]] && [[ $response != "restartmongo" ]] && [[ $response != "stopmongo" ]] && [[ $response != "issue" ]] && [[ $response != "status" ]] && [[ $response != "start" ]] && [[ $response != "stop" ]]
	do
		read  -p "start | stop | restart | restartmongo | stopmongo | issue | stress | status = " response
	done

if [ $response = "stress" ]
then
	response='run stress '$2' '$3' '$4' '$5' '$6' '$7' '$8' '$9' '$11' '$12
	echo $response
fi

i=$START_ENV
while [[ $i -lt $END_ENV ]]
do
	echo $i
	if [ $i -lt 5 ]
	then
		X='0' #from 00 to 04
		LOCATION=$LOCATION1      
	
		echo 'run ssh user'$X$i'@'$DOMAIN_NAME$X$i'.'$LOCATION'.cloudapp.azure.com' $response
		ssh -tt -oStrictHostKeyChecking=no 'user'$X$i'@'$DOMAIN_NAME$X$i'.'$LOCATION'.cloudapp.azure.com' '/home/dynatracelab_easytraveld/start-stop-easytravel.sh' $response &

	fi
	if [ $i -ge 5 ] && [ $i -lt 10 ] 
	then
		X='0' #from 05 to 09
		LOCATION=$LOCATION2
		
		echo 'run ssh user'$X$i'@'$DOMAIN_NAME$X$i'.'$LOCATION'.cloudapp.azure.com' $response
		ssh -tt -oStrictHostKeyChecking=no 'user'$X$i'@'$DOMAIN_NAME$X$i'.'$LOCATION'.cloudapp.azure.com' '/home/dynatracelab_easytraveld/start-stop-easytravel.sh' $response &


	fi
	if [ $i -ge 10 ] && [ $i -lt 15 ] 
	then
		X='' #from 10 to 14
		LOCATION=$LOCATION3

		echo 'run ssh user'$i'@'$DOMAIN_NAME$i'.'$LOCATION'.cloudapp.azure.com' $response
		ssh -tt -oStrictHostKeyChecking=no 'user'$i'@'$DOMAIN_NAME$i'.'$LOCATION'.cloudapp.azure.com' '/home/dynatracelab_easytraveld/start-stop-easytravel.sh' $response &

	fi
	if [ $i -ge 15 ] && [ $i -lt 20 ] 
	then
		X='' #from 10 to 20
		LOCATION=$LOCATION4
		
		echo 'run ssh user'$i'@'$DOMAIN_NAME$i'.'$LOCATION'.cloudapp.azure.com' $response
		ssh -tt -oStrictHostKeyChecking=no 'user'$i'@'$DOMAIN_NAME$i'.'$LOCATION'.cloudapp.azure.com' '/home/dynatracelab_easytraveld/start-stop-easytravel.sh' $response &

	fi     
	i=$(($i + 1))
done
