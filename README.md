# Lab environment for dynatrace training
This script permits to deploy quickly several Ubuntu VM with Docker Engine on an Azure subscription. It's usefull for a workshop and Dynatrace Training. Several options are available to deploy and start automatically easytravel with OneAgent installation and configuration deploy with Monaco. 

Open your azure subscription, https://portal.azure.com/ 
Open your azure cli like described here :  
![cli-azure](cli-azure.png)

  
# Deploy training environment : 
Go to your Azure Cli and apply these commands
   
    cd;if [ -d "./lab-environment-for-dynatrace-training" ];then rm -rf ./lab-environment-for-dynatrace-training;fi
    git clone https://github.com/JLLormeau/lab-environment-for-dynatrace-training.git
    cd lab-environment-for-dynatrace-training;chmod +x ./azure-cli-deploy-vm-windows-and-linux-for-training-dynatrace.sh
    curl -L https://github.com/Dynatrace/dynatrace-configuration-as-code/releases/latest/download/monaco-linux-amd64 -o monaco
    chmod +x monaco
    ./azure-cli-deploy-vm-windows-and-linux-for-training-dynatrace.sh
      

## Step 1 - Max 20 environments
CONFIGURATION :  

0) config env : training name                          =demodomaine
1) config env : password                               =DummyP@ssword00
2) config env : value fisrt env                        =01
3) config env : nbr total env                          =3
4) add env : windows VM to env                         =N
5) add env : easytravel installed                      =Y
6) add env : cron to stop Mongo at 11 H GMT            =Y
7) stop Mongo : hour (GMT) of Mongo shutdown           =11
8) full configuration : OneAgent + run Monaco          =Y
9) start env : VM started after installation           =N  

A) apply and deploy the VM - (Ctrl/c to quit) A

## Get the list of environment you will create : 
ENVIRONMENT : Linux
user01;mydemoenvironment01.francecentral.cloudapp.azure.com
user02;mydemoenvironment02.francecentral.cloudapp.azure.com
user03;mydemoenvironment03.francecentral.cloudapp.azure.com

## Step 2 - Deploy configuration with Monaco on Dynatrace env  
if option 8_full configuration with OneAgent installed + Monaco = Y
PARAMETER :  

0) Tenant                               =xxxx.live.dynatrace.com  
1) API Token                            =dt0c01.abcdefghij.abcdefghijklmn   
3) List of emails                       =user1@user1.com user2@user2.com (optional)  
A) apply and deploy the VM - (Ctrl/c to quit)  

Selet A for starting the installation (env 5 minutes / VM): 
![image](https://user-images.githubusercontent.com/40337213/149200827-f44df686-ce63-427f-bfa6-aa7e227c1e66.png)

## Access - example for the user01 with the training name = mydemoenvironment  : 

Shell-in-the-box (putty) => https://mydemoenvironment01.francecentral.cloudapp.azure.com/  
easytravel classic  => http://mydemoenvironment01.francecentral.cloudapp.azure.com/  
easytravel angular  => http://mydemoenvironment01.francecentral.cloudapp.azure.com:9079/  (no VPN !! - only with a direct access)  


## Last step - Delete the ResourceGroups on your Azure subscription
At the end, use the script delete_resourcegroup to clean your Azure environement. 
![image](https://user-images.githubusercontent.com/40337213/149200383-cca7dd1a-d18e-43d5-b64b-9559d6f07b04.png)

   

