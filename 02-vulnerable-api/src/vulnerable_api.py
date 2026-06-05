# FOR LOCALHOST / LAB USE ONLY
# This Flask app is intentionally vulnerable for educational purposes.
# Do not deploy this app publicly or use real sensitive information inside it.

from flask import Flask, jsonify  # Imports Flask to create the web app and jsonify to return JSON responses

app = Flask(__name__)  # Creates the Flask application instance

# Fake sensitive information used only for this lab.
# This data is intentionally exposed later to demonstrate sensitive data exposure.
SENSITIVE_INFO = {
    "username": "admin",  # Fake admin username used as sample exposed data
    "password": "fake_admin_password_123",  # Fake password used to demonstrate unsafe data exposure
    "address": "777 Example Road",  # Fake address used as sample personal information
    "ssn": "123-45-6789"  # Fake SSN-style value used to demonstrate sensitive personal data exposure
}


@app.get("/")  # Creates a GET route for the homepage of the API
def home():
    # Returns a safe explanation of what the lab is and where the vulnerable endpoint is located
    return jsonify({
        "message": "Vulnerable API Lab",  # Basic title/message for the API
        "warning": "This app intentionally exposes fake sensitive data for localhost testing only.",  # Explains the lab purpose
        "endpoint": "/data"  # Shows the endpoint that demonstrates the vulnerability
    })


@app.get("/data")  # Creates a GET route that exposes the vulnerable data endpoint
def data():
    # Vulnerability: No authentication or authorization is required.
    # Anyone who visits /data can view the fake sensitive information.
    # This demonstrates sensitive data exposure and broken access control.
    return jsonify(SENSITIVE_INFO)  # Converts the fake sensitive dictionary into a JSON response


if __name__ == "__main__":  # Runs this block only when the file is executed directly
    # Starts the Flask development server on localhost only.
    # host="127.0.0.1" keeps the app limited to the local machine.
    # port=3000 makes the app available at http://127.0.0.1:3000
    # debug=True is useful for learning, but should not be used in production.
    app.run(host="127.0.0.1", port=3000, debug=True)
    
