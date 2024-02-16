#!/bin/bash

gunicorn --bind 0:8500 main:app --worker-class uvicorn.workers.UvicornWorker --reload