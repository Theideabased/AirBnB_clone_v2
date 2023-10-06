#!/usr/bin/env bash
# This will set uo the web server so we can deploy our Airbnb clone project
sudo apt-get update
sudo apt-get install nginx

# creaye a foldee /data/ if not exists
mkdir -p /data

# create a folder /data/web_static if not exist
mkdir -p /data/web_static

# create a folder /data/web_static/releases/ if not exist
mkdir -p /data/web_static/releases

# create a folder /data/web_static/shared/ if not exists
mkdir -p /data/web_static/shared

# create a folder /data/web_static/releases/test/ if not exist
mkdir -p /data/web_static/releases/test

# create a fake html fike
echo "<html>\n <head>\n </head>\n <body>\n Holberton School\n \
	</body>\n </html>">> /data/web_static/releases/test/index.html

# creating a symbolic link 
ln -sF /data/web_static/releases/test/ /data/web_static/current

# give ownership of the /data/ to ubuntu
sudo chown -R ubuntu :ubuntu /data

# update the nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;
    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }
    location /redirect_me {
        return 301 http://cuberule.com/;
    }
    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" > /etc/nginx/sites-available/default

service nginx restart
