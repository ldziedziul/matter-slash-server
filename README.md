# Matter slash server #
Simple server handling custom [Mattermost](https://www.mattermost.org) slash commands

## Requirements ##
 - Python
 - [virtualenv](https://virtualenv.readthedocs.io/en/latest)
 - [pip](https://packaging.python.org/install_requirements_linux/#installing-pip-setuptools-wheel-with-linux-package-managers)

## Setup ##
run `./setup-venv.sh`

It will create the virtual env and install all required dependencies (see `requirements.txt`)

## Run ##
Run `./matter-slash-server-run.sh` to start matter slash server in current terminal. If you want to start matter slash server in the background use `./matter-slash-server-start.sh`
  
run `./matter-slash-server-stop.sh` to stop matter slash server
