from flask import Flask, jsonify
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Hello from Flask App by Adil",
        "version": os.getenv("APP_VERSION", "1.0.0"),
        "environment": os.getenv("NODE_ENV", "development")
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    # écouter sur 0.0.0.0 pour Kubernetes
    app.run(host='0.0.0.0', port=5000)
