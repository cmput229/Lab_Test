#!/bin/sh
python3 src/main.py $(cat $1) | diff $2 -
