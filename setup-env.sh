#!/bin/bash

python3 -m venv env
source env/bin/activate
pip  install setuptools-rust
pip install --upgrade pip
pip install -r requirements.txt
