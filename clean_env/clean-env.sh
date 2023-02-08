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

while [ "$response" !=  "$MyTenant"  ]
	do
		read  -p "clean ALL configurations for this tenant $MyTenant - enter the full name $MyTenant :  " response
	done

python clean-env.py
python ../mongo/process_mongo_availability.py disable

cd ..
i=$START_ENV
while [ $i -le $END_ENV ]
	do
		if [ $i -lt 10 ]; then 
			p=0
		else
			p=''	
		fi	
			echo easytravel$p$i
			echo `sed -i 's/Appname/easytravel'$p$i'/g' $DIR_MONACO/Delete/delete.yaml;./monaco deploy -e=environments.yaml -s=free_trial $DIR_MONACO/Delete;sed -i 's/easytravel'$p$i'/Appname/g' $DIR_MONACO/Delete/delete.yaml`
	i=$(($i + 1))
done

