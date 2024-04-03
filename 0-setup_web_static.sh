#!/usr/bin/env bash
#sets up server for deployment of web_static
#install nginx if it is not installed
function install() {
	if ! command -v "$1"; then
		echo -e "\t Installing nginx...\n"
		apt update -y -qq && apt install -y -qq "$1"
		echo -e "\nSuccessfully installed nginx\n"
		echo -e "\nSetting up Nginx..."
		ufw allow 'Nginx HTTP'
		echo -e "Nginx is set up successfully!...\n"
	else
		echo -e "\nNginx is already installed.\n"
	fi
}
install nginx

web_static_dir="/data/web_static/"
shared="/shared/"
releases="/releases/test/"

if [ ! -d "$web_static_dir" ]; then
	mkdir -p "$web_static_dir"

	if [ ! -d "$web_static_dir""$shared" ]; then
		mkdir "$web_static_dir""$shared"
	fi
	if [ ! -d "$web_static_dir""$releases" ]; then
		mkdir -p "$web_static_dir""$releases" 
	fi
fi

fake_html="\
<html>
	<head>
		<title>Fake Content</title>
	</head>
	<body>
		<h1>This is a fake html page</h1>
	</body>
</html>
"
echo "$fake_html" > /data/web_static/releases/test/index.html

sym_link="/data/web_static/current/"

if [ -L "$sym_link" ]; then
	rm -r "$sym_link"
	ln -s "$sym_link" "$web_static_dir""$releases"
else
	ln -s "$sym_link" "$web_static_dir""$releases"
fi

chown -R ubuntu:ubuntu /data/

new_block="\
location /hbnb_static {
	alias /data/web_static/current/;
}
"
nginx_config="/etc/nginx/sites-available/default"

if [ -f "$nginx_config" ]; then
	if grep -q "location /hbnb_static" "$nginx_config"; then
		echo "Configuration block for hbnb_static exists in $nginx_config"
	else
		sudo sed -i "/server {/a\t$new_block" "$nginx_config"
		echo "Added configuration block for hbnb_static"
	fi
else
	echo "NGINX not properly configured as $nginx_config does not exist"
fi
