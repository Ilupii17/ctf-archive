from flask import Flask, request, Response, abort, render_template
import time
import socket
import requests
from urllib.parse import urlparse

app = Flask(__name__)

# Resolve NASA's IP at startup
NASA_HOST = "images-api.nasa.gov"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api")
def api():
    NASA_IPS = set(socket.gethostbyname_ex(NASA_HOST)[2])

    target_url = request.args.get("url")
    if not target_url:
        abort(400, "Missing url parameter")

    # Parse the target URL
    parsed = urlparse(target_url)
    if not parsed.scheme:
        target_url = "https://" + target_url  # assume https if missing
        parsed = urlparse(target_url)

    hostname = parsed.hostname
    if not hostname:
        abort(400, "Invalid URL")

    # Prevent users brute forcing our api
    time.sleep(1)
    try:
        resolved_ip = socket.gethostbyname(hostname)
    except socket.gaierror as e:
        abort(400, "Unable to resolve hostname")

    # Verify that the url provided resolve's to NASA's IP address
    if resolved_ip not in NASA_IPS:
        abort(403, "URL does not resolve to NASA")

    # Fetch and stream the content
    try:
        r = requests.get(target_url, stream=True, timeout=5)
        r.raise_for_status()
    except requests.RequestException as e:
        print("failed to fetch", target_url, e)
        abort(502, "Failed to fetch data")

    return Response(
        r.iter_content(chunk_size=8192),
        content_type=r.headers.get("Content-Type", "application/octet-stream"),
    )
