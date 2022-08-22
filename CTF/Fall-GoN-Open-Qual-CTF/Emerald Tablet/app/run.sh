#!/bin/sh

# Randomize flag inscription key for all instances
python manage.py migrate tablet 0002

# Run server (--insecure just for static file serving, no intended bugs)
exec python manage.py runserver --insecure 0.0.0.0:59909
