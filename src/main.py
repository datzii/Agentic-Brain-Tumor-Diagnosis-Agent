
import os
import time

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import config.config as config
from services.agents import make_agent_query


app = Flask(__name__)
CORS(app,
     allow_origins=["*"],
     allow_headers=["Content-Type, Authorization, X-Auth-Token"],
     allow_methods=["GET, POST, PUT, DELETE, OPTIONS"],
     supports_credentials=True)


@app.route("/v1/status/", methods=['GET', 'OPTIONS'])
@cross_origin()
def status():
    start = time.time()

    took_ms = round((time.time() - start) * 1000) + 1

    return jsonify(
        kudos="up",
        took_ms=took_ms
    ), 200


@app.route("/agent/make_query", methods = ['POST'])
@cross_origin()
def make_query():
    data = request.json
    input = data.get('input')
    print(input)
    response = make_agent_query(input)
    return response


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', "Content-Type, Authorization, X-Auth-Token")
    response.headers.add('Access-Control-Allow-Methods', "GET, POST, PUT, DELETE, OPTIONS")
    return response


if __name__ == "__main__":

    port = config.PORT

    if os.getenv('PORT') is not None and os.getenv('PORT') != '':
        port = int(os.getenv('PORT'))

    app.run(host="0.0.0.0", port=port, debug=False)
