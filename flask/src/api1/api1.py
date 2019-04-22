import requests
import os
from aws_xray_sdk.core import xray_recorder

from flask import Flask, jsonify, Response
app = Flask(__name__)

X_RAY_HEADER_PARENT = "_x_ray_parent_id"
X_RAY_HEADER_TRACE = "_x_ray_trace_id"

@app.route('/')
def dynamodb():
    
    xray_recorder.begin_segment(name='API1', sampling=1)
    current_segment = xray_recorder.current_segment()
    headers  = { X_RAY_HEADER_TRACE: current_segment.trace_id, X_RAY_HEADER_PARENT: current_segment.id}
    url = "http://" + os.environ['API2_HOST'] + ":5000"
    
    r = requests.get(url, headers=headers)
    
    data = r.json()

    response = jsonify({'api1': 'ok', 'api2': data['api2'], 'api3': data['api3']})
    response.status_code = 200

    xray_recorder.end_segment()
    
    return response


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')