#!/usr/bin/env bash
# first setup webserver

apt-get update
apt-get install -y nginx

# make directories if not already exits
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
# write a content into the fake html
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
  </html>" | sudo tee /data/web_static/releases/test/index.html
#create a symbolic link to
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current
# grant permission to the users
sudo chown -R ubuntu:ubuntu /data/
sudo chgrp -R ubuntu:ubuntu /data/
#setup the folder
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

#restart the service to save changes
sudo service nginx restart
