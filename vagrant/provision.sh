#!/bin/bash

PROJECT_NAME=rmazaweb
PROJECT_DIR=/vagrant
USER=ubuntu
VIRTUALENV_DIR=/home/$USER/.virtualenvs/$PROJECT_NAME
PYTHON=$VIRTUALENV_DIR/bin/python
PIP=$VIRTUALENV_DIR/bin/pip

# Virtualenv setup for project
sudo apt-get update

sudo apt-get install -y virtualenv gcc python3 python3-dev

su - $USER -c "virtualenv --python=python3 $VIRTUALENV_DIR"

su - $USER -c "echo $PROJECT_DIR > $VIRTUALENV_DIR/.project"

su - $USER -c "$PIP install --upgrade pip"

su - $USER -c "$PIP install -r $PROJECT_DIR/requirements.txt"


# Set execute permissions on manage.py as they get lost if we build from a zip file
chmod a+x $PROJECT_DIR/manage.py

# Add .env file for django-dotenv environment variable definitions
echo DJANGO_SETTINGS_MODULE=$PROJECT_NAME.settings.production > $PROJECT_DIR/.env

# Run syncdb/migrate/load_initial_data/update_index
su - $USER -c "$PYTHON $PROJECT_DIR/manage.py migrate --noinput && \
                   $PYTHON $PROJECT_DIR/manage.py loaddata $PROJECT_DIR/initial_data.json && \
                   $PYTHON $PROJECT_DIR/manage.py update_index"


# Add a couple of aliases to manage.py into .bashrc
cat << EOF >> /home/$USER/.bashrc
export PYTHONPATH=$PROJECT_DIR

alias dj="./manage.py"
alias djrun="dj runserver 0.0.0.0:8000"

source $VIRTUALENV_DIR/bin/activate
cd $PROJECT_DIR
EOF
