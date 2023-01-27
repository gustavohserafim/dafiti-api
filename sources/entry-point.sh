#!/bin/bash

flask db init
flask db migrate
flask db upgrade
flask --debug run --port 5000 --host=0.0.0.0