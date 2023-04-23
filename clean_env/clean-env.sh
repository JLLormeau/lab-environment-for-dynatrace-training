#!/bin/bash
#design by JLLormeau Dynatrace
# version beta

. ../env.sh
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
./monaco delete


