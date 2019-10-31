#!/bin/bash
# A startup script
echo "Starting application...";
uwsgi app.ini;
while ! nc -z postgres 5432;
    do
        echo sleeping;
        sleep 1;
    done;
        echo Connected!;
      
flask db init;
flask db migrate;
flask db upgrade;
