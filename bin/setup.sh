#!/bin/sh

python -m virtualenv .ve
#source .ve/bin/activate
.ve/Scripts/activate.bat
pip install -r requirements.txt