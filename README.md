# multiple-fishing


## Installation

### Build dependencies

```
adduser django
usermod -aG sudo django
su django
cd

sudo apt update

sudo apt install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl \
git libpq-dev supervisor nginx
```


### Python installation

```
# pyenv installation.
curl https://pyenv.run | bash

# Load pyenv automatically by adding
# the following to ~/.bashrc:
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

. ~/.bashrc

# Installing Python specific version.
pyenv install --list | grep " 3\.[678]"
pyenv install -v 3.7.7
pyenv versions
pyenv global 3.7.7

# Check current Python version.
pyenv versions
```


### -- preparation

```
python3.7 -m venv venv
source venv/bin/activate
python3.7 -m pip install django
```

### Creating DB for Django application
```
# - Migrations -
python3.7 manage.py makemigrations yandex
python3.7 manage.py migrate

# - Deploying static files - 
python3.6 manage.py collectstatic --link

# - Creating superuser -
python3.7 manage.py createsuperuser
```


### NGINX

```
deactivate
sudo systemctl enable nginx
sudo vi /etc/sysctl.conf

# - Add next line in the end of the file -
fs.file-max = 40000

sudo sysctl -p
sudo cp multiple_fishing/server_configs/nginx.conf /etc/nginx/

# - Fill in the nginx.conf -
# - return 301 $sheme://<domain.com>; Change domain on yours in this line -  
sudo vi /etc/nginx/nginx.conf

# - Fill in the config file custom_nginx.conf - 
vi multiple_fishing/server_configs/custom_nginx.conf

sudo nginx -t
```


### Adding SSL

```
# NOTE: check latest certbot instruction on official site
# https://certbot.eff.org/lets-encrypt/ubuntufocal-nginx ,
# there maybe some changes

sudo apt-get update
sudo apt-get install software-properties-common
sudo add-apt-repository universe
sudo apt-get update
sudo apt-get install certbot python3-certbot-nginx

sudo certbot --nginx -d <domain.com> certonly
sudo rm /etc/letsencrypt/options-ssl-nginx.conf

crontab -e
# - Add next line for auto updating cert -
@daily certbot renew

# - Uncomment ssl supporting in custom_nginx.conf
```


### UWSGI

```
sudo python3.7 -m pip install uwsgi

# - Fill in the config file custom_uwsgi.ini -
vi /path/to/custom_uwsgi.ini

# - Copy configs to /etc/...
sudo mkdir -p /etc/uwsgi/vassals
sudo cp /path/to/server_configs/emperor.ini /etc/uwsgi/
sudo ln -s /abs/path/to/server_configs/custom_uwsgi.ini /etc/uwsgi/vassals

sudo systemctl restart nginx.service

# - Running the Django application with uwsgi and nginx -
# - Need for debug , another use systemd -
uwsgi --emperor /etc/uwsgi/emperor.ini

# - UWSGI production -
sudo cp /path/to/server_configs/emperor.uwsgi.service /etc/systemd/system/

sudo systemctl daemon-reload
sudo systemctl start emperor.uwsgi.service
sudo systemctl enable emperor.uwsgi.service
```