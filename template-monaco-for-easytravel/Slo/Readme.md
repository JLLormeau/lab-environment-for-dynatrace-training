# Deploy SLO for Management Zone

Export the variable:

	 export NEW_CLI=1
	 export MyTenant=<MyTenant>
	 export MyToken=<MyToken>
	 export MZ=<MZ-name>
		 

Deploy the configuration:

	cd;cd dynatrace-lab/lab-onboarding;
	./monaco deploy -e=environments.yaml 03-SLO/deploy-slo
