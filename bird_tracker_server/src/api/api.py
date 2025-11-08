from flask import Flask, jsonify, request
from flask_cors import CORS


class API:
    def __init__(self, database):
        self.app = Flask(__name__)
        CORS(self.app)
        self.database = database

    def setup_route(self):
        @self.app.route("/", methods=["POST"])
        def post_data():
            data = request.get_json()

            graph_data = self.database.get_calls(data.get("startDate"), data.get("endDate"), data.get("location"), data.get("bird"))

            return jsonify(graph_data)

    def run(self):
        self.setup_route()
        self.app.run(host="0.0.0.0", port=3000, debug=True)