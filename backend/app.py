from flask import Flask, request, jsonify
from flask_cors import CORS

from evaluator import evaluate_essay


app = Flask(__name__)

CORS(app)


@app.route("/")
def home():

    return jsonify({
        "message": "EssayLens AI API is running",
        "status": "success"
    })


@app.route("/analyze", methods=["POST"])
def analyze():

    try:

        data = request.get_json()

        topic = data.get("topic", "").strip()
        essay = data.get("essay", "").strip()

        if not topic:

            return jsonify({
                "error": "Topic is required"
            }), 400

        if not essay:

            return jsonify({
                "error": "Essay is required"
            }), 400

        result = evaluate_essay(
            essay,
            topic
        )

        return jsonify(result)

    except Exception as error:

        return jsonify({
            "error": str(error)
        }), 500


if __name__ == "__main__":

    print("\n===================================")
    print("        ESSAYLENS AI SERVER")
    print("===================================")
    print("Server: http://127.0.0.1:5000")
    print("===================================\n")

    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )