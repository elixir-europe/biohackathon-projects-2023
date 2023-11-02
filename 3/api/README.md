# Virtual Reference Collection API
Small API for demonstration purposes.

Developed with `python 3.10`

## Running Locally
Install dependencies
```
pip install --upgrade pip
pip install -r requirements.txt
```

Run application
```
uvicorn main:app
```

## Building and Running Image
Build image
```
docker build -t elixir/group3 .
```

Run image
```
docker run -p 8080:8080 elixir/group3
```

## Usage
- get all available ids http://localhost:8080/vrc
- get specific VRC by id http://localhost:8080/vrc/{id}

Deployed to https://elixir-biohackathon-2023.rahtiapp.fi/ for the duration of the biohackathon.
