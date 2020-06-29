# multiple-fishing


## Installation

### Build dependencies

```
sudo apt update

sudo apt install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl \
git libpq-dev supervisor
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


```
python3.7 manage.py makemigrations yandex
python3.7 manage.py migrate
python3.7 manage.py createsuperuser
```

