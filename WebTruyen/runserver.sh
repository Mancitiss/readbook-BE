#!/bin/bash

exec py manage.py runsslserver --certificate C:/Certbot/archive/mancitiss.duckdns.org/fullchain1.pem --key C:/Certbot/archive/mancitiss.duckdns.org/privkey1.pem 0.0.0.0:8000