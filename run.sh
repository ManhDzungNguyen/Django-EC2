#!/bin/bash
while [ "true" ]
do
    # cd /hdd/dungnguyen/tonchimucdich/src/predicting && source /hdd/dungnguyen/tonchimucdich/venv/bin/activate && uvicorn service_test:app --host 0.0.0.0 --port 6868
    source venv/bin/activate && cd mycv && python manage.py runserver 0.0.0.0:8000
    sleep 5
done
#dungnguyen