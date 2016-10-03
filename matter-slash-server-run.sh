#!/bin/bash
BASE_DIR=`dirname "$(readlink -f "$0")"`
cd "$BASE_DIR"

python ./matter-slash-server.py

cd "$OLDPWD"
