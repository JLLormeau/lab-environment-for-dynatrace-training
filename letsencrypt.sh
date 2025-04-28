#!/bin/sh

#domain=`ls /var/lib/shellinabox | grep cloudapp | cut -d'-' -f2- | sed 's/.pem//'`
#user=`whoami`
domain=$1
user=$2
echo $domain
echo $user
#sudo /home/dynatracelab_easytraveld/start-stop-easytravel.sh stop
#sudo apt update
#sudo snap install --classic certbot
#sleep 2
#sudo certbot certonly --standalone -d $domain --key-type rsa --quiet --agree-tos
#sleep 2
sudo cat /etc/letsencrypt/live/$domain/privkey.pem > /home/$user/cert.pem
sudo cat /etc/letsencrypt/live/$domain/fullchain.pem >> /home/$user/cert.pem
sudo rm /var/lib/shellinabox/*.pem
sudo mv /home/$user/cert.pem /var/lib/shellinabox/certificate-$domain.pem
sudo chown shellinabox:shellinabox /var/lib/shellinabox/certificate-$domain.pem
sudo chmod 600 /var/lib/shellinabox/certificate-$domain.pem
                                                                                                                                                                        
#sudo service shellinabox restart
#sudo service shellinabox status
