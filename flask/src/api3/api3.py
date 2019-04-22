import requests
import os
from aws_xray_sdk.core import xray_recorder

from flask import Flask, request, jsonify, Response
app = Flask(__name__)

X_RAY_HEADER_PARENT = "_x_ray_parent_id"
X_RAY_HEADER_TRACE = "_x_ray_trace_id"

@app.route('/')
def put_item():
    trace_id = request.headers.get(X_RAY_HEADER_TRACE)
    parent_id = request.headers.get(X_RAY_HEADER_PARENT)
    xray_recorder.begin_segment(name='API3', parent_id=parent_id ,traceid=trace_id, sampling=1)

    response = jsonify({'api3': "ok"} )
    response.status_code = 200
    response.mimetype = "application/json"
    
    xray_recorder.end_segment()

    return response


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')