#!/usr/bin/env bash
source venv/bin/activate
dev_appserver.py --skip_sdk_update_check --host=0.0.0.0 --enable_host_checking=false .
