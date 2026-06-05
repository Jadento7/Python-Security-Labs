# Python Security Labs

## Overview

This repository contains beginner-friendly cybersecurity labs built with Python. Each project focuses on a specific security concept, such as port scanning, vulnerable API behavior, sensitive data exposure, and basic API access control.

The purpose of this repository is to practice Python programming while building hands-on cybersecurity projects in a safe, controlled localhost environment.

## Projects Included

| # | Project | Description | Key Concepts |
|---:|---|---|---|
| 01 | Python Port Scanner | A basic TCP port scanner that checks common ports on localhost and reports whether they are open or closed. | Sockets, TCP connections, ports, services, localhost scanning |
| 02 | Vulnerable API Lab | A Flask API that intentionally exposes fake sensitive data without authentication. | Sensitive data exposure, broken access control, JSON APIs |
| 03 | API Key Protected API Lab | An improved Flask API that requires an API key before returning protected fake data. | API keys, request headers, access control, 401 responses |

## Skills Practiced

Through these labs, I practiced:

- Writing Python scripts
- Using the Python `socket` module
- Building basic Flask APIs
- Returning JSON responses
- Reading HTTP request headers
- Testing APIs with PowerShell and `curl.exe`
- Understanding common network ports and services
- Identifying insecure API behavior
- Applying basic access control concepts
- Documenting security projects clearly and professionally

## Repository Structure

```text
python-security-labs/
├── 01-port-scanner/
│   ├── README.md
│   ├── src/
│   │   └── port_scanner.py
│   └── screenshots/
│       ├── 01-port-scanner-output.png
│       └── 02-port-scanner-code.png
│
├── 02-vulnerable-api/
│   ├── README.md
│   ├── requirements.txt
│   ├── src/
│   │   └── vulnerable_api.py
│   └── screenshots/
│       ├── 01-sensitive-data-exposed.png
│       ├── 02-flask-server-running.png
│       └── 03-vulnerable-api-code.png
│
├── 03-api-key-protected-api/
│   ├── README.md
│   ├── requirements.txt
│   ├── src/
│   │   └── secure_api_key.py
│   └── screenshots/
│       ├── 01-api-key-access-test.png
│       ├── 02-api-key-protected-code.png
│       └── 03-flask-server-running.png
│
└── README.md
```

## Project Summaries

### 01 - Python Port Scanner

This lab uses Python's built-in `socket` module to attempt TCP connections to common ports on `127.0.0.1`. The script checks whether each port is open or closed and displays the service commonly associated with that port.

This project helped reinforce how port scanning works at a basic level and why open ports matter in cybersecurity.

### 02 - Vulnerable API Lab

This lab uses Python and Flask to create a deliberately vulnerable API. The `/data` endpoint returns fake sensitive information without requiring authentication or authorization.

This project demonstrates how sensitive data exposure and broken access control can happen when an API does not verify who is requesting protected information.

### 03 - API Key Protected API Lab

This lab improves the vulnerable API by requiring an API key in the request header before returning fake sensitive data. If the API key is missing or incorrect, the application returns a `401 Unauthorized` response.

This project demonstrates how even a basic access control check can prevent unauthenticated users from accessing protected API data.

## How to Run the Labs

Each project folder contains its own README with specific setup and run instructions.

In general, the labs can be run by navigating into the project folder and running the Python script.

Example:

```bash
cd 01-port-scanner
python src/port_scanner.py
```

For Flask-based projects, install dependencies first:

```bash
pip install -r requirements.txt
```

Then run the application:

```bash
python src/vulnerable_api.py
```

or:

```bash
python src/secure_api_key.py
```

## Tools Used

- Python
- Flask
- Visual Studio Code
- PowerShell
- `curl.exe`
- Web browser
- Localhost testing environment

## What I Learned

These projects helped me build a stronger foundation in both Python and cybersecurity. I learned how network ports are checked, how basic APIs return data, how insecure API behavior can expose sensitive information, and how access control can be added to protect an endpoint.

I also practiced documenting projects in a way that explains the goal, tools used, technical process, screenshots, lessons learned, and ethical boundaries.

## Future Improvements

Possible future improvements for this repository include:

- Adding command-line arguments to the port scanner
- Allowing custom target IP addresses and port ranges
- Saving scan results to a file
- Moving hardcoded API keys into environment variables
- Adding logging and rate limiting to the API labs
- Creating a login-based authentication lab
- Adding more OWASP Top 10 focused labs
- Adding a main setup guide for the entire repository

## Security and Ethics Notice

These projects are for educational purposes only. They are designed to run in a local lab environment using `127.0.0.1`, also known as localhost.

Do not scan, test, or attack systems that you do not own or do not have explicit permission to assess. Do not deploy intentionally vulnerable applications publicly. All sensitive-looking data used in these labs is fake and should never be replaced with real credentials, personal information, API keys, tokens, or secrets.
