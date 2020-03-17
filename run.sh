#!/bin/bash

# init virtual env
if [[ -d venv ]]
then
  echo "Deleting old virtualenv"
  rm venv/ -rf
fi

virtualenv venv -p python3 && venv/bin/python3 -m pip install -r requirements.txt && echo "venv was created"