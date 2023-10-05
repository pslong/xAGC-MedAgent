#!/bin/bash

# url=https://www.physionet.org/challenge/2017/
url=https://www.physionet.org/files/challenge-2017/1.0.0/

mkdir data && cd data
# cd data

curl -O $url/training2017.zip
unzip training2017.zip
curl -O $url/sample2017.zip
unzip sample2017.zip
curl -O $url/REFERENCE-v3.csv

cd ..

python build_datasets.py
