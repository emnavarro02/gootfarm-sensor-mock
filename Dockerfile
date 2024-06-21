FROM python:alpine AS sensor

RUN apk update && apk upgrade
ADD /sensor/ /srv/app/

WORKDIR /srv/app/
RUN pip install -r /srv/app/requirements.txt

ENTRYPOINT ["python", "/srv/app/main.py"]