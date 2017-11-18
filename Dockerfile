FROM tiangolo/uwsgi-nginx:python3.6

ENV UWSGI_INI /src/uwsgi.ini
ENV DJANGO_SETTINGS_MODULE rmazaweb.settings.production

RUN mkdir /src
WORKDIR /src

COPY . .

RUN pip install -r requirements.txt
RUN ./manage.py collectstatic --noinput

