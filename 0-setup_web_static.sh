#!/usr/bin/env bash
# The script sets up my web servers for deployment

# Install Nginx if not already installed
if ! command -v nginx &> /dev/null; then
    sudo apt-get update
    sudo apt-get -y install nginx
fi

# Creates the  required directories
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

# Creates a fake HTML file
echo "<html><head></head><body>Holberton School</body></html>" | sudo tee /data/web_static/releases/test/index.html

# Creates or recreates the symbolic link
sudo rm -f /data/web_static/current
sudo ln -s /data/web_static/releases/test /data/web_static/current

# Gives ownership recursively to ubuntu
sudo chown -R ubuntu:ubuntu /data

# Updates Nginx configuration
NEW_STRING="\\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n"
if ! grep -q "location /hbnb_static/" /etc/nginx/sites-available/default; then
    sudo sed -i "/server {/a $NEW_STRING" /etc/nginx/sites-available/default
fi
# Restarst Nginx after changes
sudo service nginx restart
