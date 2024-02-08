#!/bin/bash

HOST=${APP_HOST:="0.0.0.0"}
PORT=${APP_PORT:="8080"}

echo 'start elixir/group3'
exec uvicorn main:app --host $HOST --port $PORT
