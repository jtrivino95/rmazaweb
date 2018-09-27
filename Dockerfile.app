FROM python:3.7-slim

WORKDIR /rmazaweb
COPY . .

RUN pip install -r ./requirements/production.txt
RUN pip install gunicorn

EXPOSE 8000

CMD ["gunicorn", "rmazaweb.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
