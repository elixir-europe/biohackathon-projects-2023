#!/usr/bin/env bash

WDIR=/app
export FLASK_OUTPUT_FILE="/app/output.csv"

# Can remove stdout/err redirect for debugging, otherwise shows Flask/Vue logs
cd $WDIR
honcho start -f Procfile-docker #> /dev/null 2>&1 &

while [[ ! -f "$FLASK_OUTPUT_FILE" ]]; do
    sleep 1
done

cp $FLASK_OUTPUT_FILE '$ENA_OUTPUT_FILE'

exit 0
