from flask import Flask, jsonify, json
from pyroute2 import IPDB


class SetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        elif obj is None:
            return None
        return json.JSONEncoder.default(self, obj)


def remove_null(obj):
    return {key:value for key, value in obj.items() if value is not None}

app = Flask(__name__)
app.json_encoder = SetEncoder

@app.route('/interfaces')
def get_interfaces():
    with IPDB() as ip:
        j = {k:v for k, v in ip.interfaces.items() if isinstance(k, str)}
        return jsonify(j)


@app.route('/interfaces/<interface>')
def get_interface(interface):
    with IPDB() as ip:
        j = ip.interfaces[interface]
        return jsonify(j)
