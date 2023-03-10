from flask import Flask, request, render_template
from util import pipeline

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/query", methods=["POST"])
def query():
    src = request.json["src"]
    tgt = request.json["tgt"]
    return pipeline(src, tgt)

@app.after_request
def after_request(response):
    white_origin = ['http://localhost:3000']
    if request.headers['Origin'] in white_origin:
        response.headers['Access-Control-Allow-Origin'] = request.headers['Origin'] 
        response.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    return response

if __name__ == "__main__":
    app.run(debug=True, port=8000)