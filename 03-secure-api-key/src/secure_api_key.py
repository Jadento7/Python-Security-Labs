# FOR LOCALHOST / LAB USE ONLY
# Secure API Key Lab:
# This version improves the intentionally vulnerable API by requiring an API key.
# Do not deploy this app publicly or use real sensitive information inside it.

from flask import Flask, jsonify, request
# Flask creates the web application.
# jsonify converts Python dictionaries into JSON responses.
# request lets the app read data sent by the client, such as headers.

app = Flask(__name__)
# Creates the Flask application instance.
# __name__ tells Flask where the application is being run from.


# Fake sensitive information used only for this lab.
# This data represents information that should normally be protected.
SENSITIVE_INFO = {
    "username": "admin",  # Fake username used as sample protected data
    "password": "fake_admin_password_123",  # Fake password used to demonstrate sensitive data handling
    "address": "777 Example Road",  # Fake address used as sample personal information
    "ssn": "123-45-6789"  # Fake SSN-style value used to represent highly sensitive personal data
}


# Fake API key for localhost testing only.
# This key is used to check whether the client is allowed to access /data.
# In a real application, API keys should not be hardcoded directly in the source code.
API_KEY = "lab-api-key-123"


@app.get("/")
# Creates a GET route for the homepage.
# This route is safe because it does not expose the fake sensitive data.
def home():
    return jsonify({
        "message": "API Key Protected Lab",  # Describes the purpose of the app
        "warning": "This app uses a simple API key check for localhost testing only.",  # Explains this is a lab
        "protected_endpoint": "/data",  # Shows which endpoint requires an API key
        "required_header": "X-API-Key"  # Tells the user which HTTP header must be provided
    })


@app.get("/data")
# Creates a GET route for the protected data endpoint.
# This endpoint should only return data if the correct API key is provided.
def data():
    # Reads the API key from the request headers.
    # The client must send a header named X-API-Key with the correct value.
    provided_key = request.headers.get("X-API-Key")

    # Checks whether the provided API key matches the expected API key.
    # If the key is missing or incorrect, access is denied.
    if provided_key != API_KEY:
        return jsonify({
            "error": "Unauthorized",  # Tells the client the request was not allowed
            "message": "Missing or invalid API key"  # Explains why access was denied
        }), 401  # 401 means the request is unauthorized

    # If the API key is correct, the fake sensitive data is returned.
    # This demonstrates how access control protects the endpoint.
    return jsonify(SENSITIVE_INFO)


if __name__ == "__main__":
    # Runs the Flask app only when this file is executed directly.
    # host="127.0.0.1" keeps the app limited to the local machine.
    # port=3000 makes the app available at http://127.0.0.1:3000
    # debug=True helps during development, but should not be used in production.
    app.run(host="127.0.0.1", port=3000, debug=True)
