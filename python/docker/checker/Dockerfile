FROM python:3.7-alpine

# install dependencies
COPY requirements.txt /requirements.txt

RUN apk add --no-cache gcc \
                       g++ \
                       binutils \
                       musl-dev && \
    pip install -r /requirements.txt && \
    apk del gcc \
            g++ \
            binutils \
            musl-dev && \
    apk add libstdc++ && \
    rm -rf ~/.cache && \
    rm /requirements.txt

# copy the checker app
COPY checker.py /checker.py

COPY protocol /protocol

COPY docker/checker/entrypoint.sh /entrypoint.sh

EXPOSE 9000

ENTRYPOINT ["/bin/sh", "/entrypoint.sh"]
