printf "\n*******************************************************"
printf "\nInstalling gunicorn ...\n"

sudo apt-get --yes --force-yes install gunicorn
gunicorn --version

printf "\nSetting up Gunicorn Configurationr\n"

sudo rm /etc/nginx/sites-enabled/default
sudo cp eztodo/app-server/conf/app_server_nginx.conf /etc/nginx/sites-available/
sudo ln -s /etc/nginx/sites-available/app_server_nginx.conf /etc/nginx/sites-enabled/app_server_nginx.conf

sudo service nginx restart

printf "\nMoving Repos Assets to www...\n"

sudo mkdir /home/www
sudo rm /home/www/app-server -r
sudo rm /home/www/api-server -r
sudo mv ~/eztodo/app-server/ /home/www/
sudo mv ~/eztodo/api-server/ /home/www/

printf "\nStarting Application Servers...\n"

cd /home/www/app-server/ && nohup gunicorn app:app -b localhost:8000 & disown
cd /home/www/api-server/ && nohup gunicorn flaskr:app -b localhost:5001 & disown

printf "\nGunicorn Processes...\n"
ps aux|grep gunicorn

printf "\nFINISHED!\n"

printf "\nTry hitting the public domain now!\n"

