FROM python:3.13.7-slim-trixie

RUN pip install --no-cache-dir waitress flask requests

WORKDIR /app
COPY . .

USER nobody

CMD waitress-serve --listen "127.0.0.1:5001" internal_app:app & \
    waitress-serve --listen "0.0.0.0:1337" --trusted-proxy '*' --trusted-proxy-headers 'x-forwarded-for x-forwarded-proto x-forwarded-port' --log-untrusted-proxy-headers --clear-untrusted-proxy-headers --threads 4 main:app
