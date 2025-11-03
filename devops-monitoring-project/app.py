from flask import Flask
from prometheus_client import start_http_server, Counter, generate_latest

# Create a Flask app
app = Flask(__name__)

# Create a counter metric for Prometheus
# This will count the number of page visits
VISITS_COUNTER = Counter('page_visits_total', 'Total number of visits to the main page')

# Define the main route for the web app
@app.route('/')
def index():
    # Increment the counter every time the page is visited
    VISITS_COUNTER.inc()
    # Get the current value of the counter to display it
    # Note: This is a simplified way to get the count. In a real app, you'd access the metric's value.
    # For this demo, we'll just display a welcome message.
    return "<h1>Welcome to the DevOps Exam Project!</h1><p>Visit the /metrics endpoint to see the visitor count.</p>"

# Define the /metrics endpoint that Prometheus will scrape
@app.route('/metrics')
def metrics():
    return generate_latest()

if __name__ == '__main__':
    # Start the Prometheus metrics server on port 8000
    start_http_server(8000)
    # Run the Flask web app on port 5000
    app.run(host='0.0.0.0', port=5000)