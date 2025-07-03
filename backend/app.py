# backend/app.py

import os
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/ping")
def ping():
    return jsonify({"message": "pong"})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # 🔥 关键：使用 Render 提供的 PORT
    app.run(host="0.0.0.0", port=port)
