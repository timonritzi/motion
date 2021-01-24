#!/bin/bash

python -c "import time; time.sleep(3)"
python manage.py migrate
python manage.py collectstatic --noinput
rm -rf /frontend/build/* && cp -r /frontend_tmp/* /frontend
gunicorn -w 4 -b 0.0.0.0 motion_backend.wsgi:application

