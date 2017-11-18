FROM tiangolo/uwsgi-nginx:python3.6

RUN mkdir /src
WORKDIR /src

COPY . .

RUN pip install -r requirements.txt
RUN ./manage.py collectstatic --noinput
RUN ./manage.py migrate
RUN ./manage.py loaddata initial_data.json

ENV UWSGI_INI /src/uwsgi.ini
