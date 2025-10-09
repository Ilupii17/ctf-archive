from flask import Flask, request, Response, abort

app = Flask(__name__)

@app.route("/")
def root():
    return "the flag will go here"