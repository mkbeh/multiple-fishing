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

sudo cp /path/to/mysite/custom_nginx.conf /etc/nginx/sites-enabled/
sudo nginx -t
```
