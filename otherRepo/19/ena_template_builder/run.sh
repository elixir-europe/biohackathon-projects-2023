#!/usr/bin/env bash

WDIR=/app

# Can remove stdout/err redirect for debugging, otherwise shows Flask/Vue logs
cd $WDIR
honcho start -f Procfile-docker #> /dev/null 2>&1 &

while [[ ! -f "$ENA_OUTPUT_STUDY" ]]; do
    sleep 0.25
done

sleep 0.25

exit 0
