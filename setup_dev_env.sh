#!/bin/bash
#-*- coding: utf-8 -*-

set -e
VENV=./venv

python3 -m virtualenv ${VENV}
. ${VENV}/bin/activate
pip install -U pip setuptools
pip install -r requirements.txt

echo ""
echo "* Created a virtualenv in ${VENV}, and"
echo "* installed dependencies into the virtualenv."
echo "* You can now activate the virtualenv by \". ${VENV}/bin/activate\""
