#!/usr/bin/env sh
gunicorn --chdir app website:app --workers 2 --threads 2 --bind 0.0.0.0:8080