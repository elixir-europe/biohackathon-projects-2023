"""ELIXIR Biohackathon 2023 Group 3 Mock VRC API."""

import os
import sys
import json
import logging

from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from fastapi.responses import PlainTextResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware

# the web app
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

# logging
formatting = "[%(asctime)s][%(name)s][%(process)d %(processName)s][%(levelname)-8s] (L:%(lineno)s) %(module)s | %(funcName)s: %(message)s"
logging.basicConfig(level=logging.INFO, format=formatting)
LOG = logging.getLogger("elixir/group3")

# configuration
data_file = os.environ.get("VRC_DATA", "data.json")
DATA = {}
try:
    with open(data_file, "r") as f:
        LOG.info(f"loading data file {data_file}")
        DATA = json.loads(f.read())
        LOG.info(f"data loaded: {DATA}")
except Exception as e:
    LOG.error(f"failed to load data file {data_file}, {e}")
    sys.exit(e)


@app.get("/")
async def index_endpoint():
    """Index can be used as a health check endpoint."""
    LOG.info("request to index")
    return PlainTextResponse("ELIXIR Biohackathon 2023")


@app.get("/vrc")
async def vrc_ids_endpoints():
    """List all VRC IDs available."""
    LOG.info("request to vrc id list")

    return JSONResponse(DATA["ids"])


@app.get("/vrc/{vrc_id}")
async def vrc_data_endpoint(vrc_id: str):
    """Get specific VRC by ID."""
    LOG.info("request to virtual reference collection")

    json_response = {}
    try:
        json_response = DATA["data"][vrc_id]
    except KeyError as e:
        LOG.info(f"no virtual reference collections found with id={vrc_id}, reason={e}")
        raise HTTPException(404, f"no virtual reference collections found with id: {vrc_id}")
    except Exception as e:
        LOG.error(e)
        raise HTTPException(500, "unexpected error")

    return JSONResponse(json_response)
