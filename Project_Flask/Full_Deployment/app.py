from flask import Flask, jsonify, request
from prometheus_client import Counter, generate_latest
from app.controllers.book_controller import book_bp

app = Flask(__name__)

# Register Blueprints (routes)
app.register_blueprint(book_bp)

# Create a Prometheus Counter to count requests
REQUEST_COUNTER = Counter('flask_app_requests_total', 'Total requests to Flask app')

@app.route('/hello', methods=['GET'])
def hello_world():
    REQUEST_COUNTER.inc()  # Increment the counter
    return jsonify(message="Hello, World!")

# Prometheus metrics route
@app.route('/metrics', methods=['GET'])
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain; version=0.0.4'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


