printf "\n*******************************************************"
printf "\nInstalling gunicorn ...\n"
sudo apt-get --yes --force-yes install gunicorn

printf "\n*******************************************************"
printf "\nInstalling git and pulling Public Repo ...\n"
sudo apt-get --yes --force-yes install git
sudo rm eztodo -r
git clone https://github.com/fyeung86/eztodo.git

printf "\nSetting up Application Server?\n"
# sudo cp eztodo/api-server/conf/api_server_nginx.conf /etc/nginx/conf.d/                                               
sudo cp eztodo/app-server/conf/app_server_nginx.conf /etc/nginx/sites-available/
sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /etc/nginx/sites-available/app_server_nginx.conf /etc/nginx/sites-enabled/app_server_nginx.conf
sudo service nginx restart
sudo mkdir /home/www
sudo rm /home/www/app-server -r
sudo rm /home/www/api-server -r
sudo mv ~/eztodo/app-server/ /home/www/
sudo mv ~/eztodo/api-server/ /home/www/
cd /home/www/app-server/ && nohup gunicorn app:app -b localhost:8001 & disown
cd /home/www/api-server/ && nohup gunicorn flaskr:app -b localhost:5000 & disown


printf "\nFINISHED!\n"

