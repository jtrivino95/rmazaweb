FROM alpine

# Initialize
RUN mkdir -p /code
WORKDIR /code
COPY requirements /code/requirements
COPY requirements.txt /code/

# Setup
RUN apk update
RUN apk upgrade
RUN apk add --update linux-headers python3 python3-dev postgresql-client postgresql-dev build-base gettext zlib libjpeg tiff-dev libwebp openjpeg musl-dev
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# Clean
RUN apk del -r python3-dev postgresql
