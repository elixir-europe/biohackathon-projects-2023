#!/usr/bin/env bash

docker build -t neoformit/ena-upload:v0.1 . && docker push neoformit/ena-upload:v0.1
