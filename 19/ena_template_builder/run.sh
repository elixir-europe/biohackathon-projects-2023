#!/usr/bin/env bash

export FLASK_OUTPUT_FILE="/app/app/output.csv"

# Can remove stdout/err redirect for debugging, otherwise shows Flask logs
python /app/app/app.py > /dev/null 2>&1 &

while [[ ! -f "$FLASK_OUTPUT_FILE" ]]; do
    sleep 1
done

cp "$FLASK_OUTPUT_FILE" "$ENA_OUTPUT_FILE"
exit 0
