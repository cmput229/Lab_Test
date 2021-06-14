#!/bin/sh
# You'll only have to run this script once after cloning the repo for the first time
if git submodule status | grep \( > /dev/null
then 
    git submodule update --init
fi
