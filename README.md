# Python Security Labs

## Overview

This repository contains a collection of beginner‑friendly Python security labs created for my ePortfolio. Each lab demonstrates a different security concept in a controlled, local‑only environment.

The labs progress from basic network scanning to API security and finally to an educational keylogger with strong ethical safeguards. All code is intentionally simplified for learning and runs exclusively on `localhost` (`127.0.0.1`).

## Lab Index

| # | Lab Name | Focus Area |
|---|----------|-------------|
| 01 | [Port Scanner](#01---port-scanner) | Network scanning, socket programming |
| 02 | [Vulnerable API](#02---vulnerable-api) | Sensitive data exposure, broken access control |
| 03 | [API Key Protected API](#03---api-key-protected-api) | Authentication, API security |
| 04 | [Educational Keylogger](#04---educational-keylogger) | Keyboard event handling, ethical safeguards |

---

## 01 - Port Scanner

### Overview
A simple TCP port scanner that checks common ports on `127.0.0.1` and reports whether each port is open or closed.

### Key Features
- Scans a predefined list of common ports (20, 21, 22, 23, 25, 53, 80, 110, 443, 445, 3389)
- Identifies the service associated with each port
- Uses Python's `socket` module for TCP connections
- Runs only on localhost to prevent unauthorised scanning

### How to Run
```bash
```
cd 01-port-scanner
python src/port_scanner.py
Learn More
See the full README for screenshots, example output, and detailed explanations.

02 - Vulnerable API
Overview
A deliberately insecure Flask API that exposes fake sensitive data on the /data endpoint without any authentication.

Key Features
Two routes: / (info) and /data (vulnerable endpoint)

Returns fake credentials (username, password, address, SSN)

Demonstrates sensitive data exposure and broken access control

Runs on http://127.0.0.1:3000

How to Run
bash
cd 02-vulnerable-api
pip install -r requirements.txt
python src/vulnerable_api.py
Learn More
See the full README for screenshots, vulnerability analysis, and improvement suggestions.

03 - API Key Protected API
Overview
An improved version of the vulnerable API that adds API key authentication to protect the /data endpoint.

Key Features
Requires a valid X-API-Key header (lab-api-key-123)

Returns 401 Unauthorized for missing or invalid keys

Same fake data structure as Lab 02

Demonstrates basic access control

How to Run
bash
cd 03-api-key-protected-api
pip install -r requirements.txt
python src/secure_api_key.py
Testing
Without key: curl http://127.0.0.1:3000/data

With key: curl.exe -H "X-API-Key: lab-api-key-123" http://127.0.0.1:3000/data

Learn More
See the full README for PowerShell testing examples and limitations discussion.

04 - Educational Keylogger
Overview
A safe, educational keylogger that logs keystrokes to a local file with timestamps and human‑readable special key tags. Requires explicit user consent (I AGREE) before logging.

Key Features
Captures all key presses using the pynput library

Converts special keys (space, enter, backspace, etc.) to readable tags like [SPACE]

Adds timestamps (HH:MM:SS) to every keystroke

Stops when ESC is pressed

Includes a mandatory consent prompt and prominent ethical disclaimers

No network transmission – logs saved only to keylog.txt

How to Run
bash
cd 04-educational-keylogger-lab
pip install pynput
python keylogger_lab.py
Important Ethics Notice
This tool is for educational use only on your own computer.
Unauthorised keylogging is illegal. The script will not run unless you type "I AGREE".

Learn More
See the full README for screenshots, example log output, and detailed safety features.

Tools Used Across All Labs
Python 3

Flask

pynput

Visual Studio Code

Localhost (127.0.0.1)

PowerShell / curl.exe (for testing APIs)

Repository Structure
text
Python-Security-Labs/
├── README.md                     (this file)
├── 01-port-scanner/
│   ├── README.md
│   ├── src/
│   │   └── port_scanner.py
│   └── screenshots/
├── 02-vulnerable-api/
│   ├── README.md
│   ├── requirements.txt
│   ├── src/
│   │   └── vulnerable_api.py
│   └── screenshots/
├── 03-api-key-protected-api/
│   ├── README.md
│   ├── requirements.txt
│   ├── src/
│   │   └── secure_api_key.py
│   └── screenshots/
└── 04-educational-keylogger-lab/
    ├── README.md
    ├── keylogger_lab.py
    └── screenshots/
What I Learned Building This Suite
Through these four labs, I learned:

Low‑level networking – TCP socket connections, port scanning, and timeouts.

Web API fundamentals – Flask routes, JSON responses, and request headers.

Access control concepts – Why authentication matters and how even a simple API key can block unauthorised access.

Ethical considerations – How to build sensitive tools (like a keylogger) responsibly with consent prompts, kill switches, and clear disclaimers.

Documentation – Writing clear, structured READMEs that explain both the what and the why for each project.

Future Improvements
Add input validation – Allow users to specify target IPs or port ranges (with warnings).

Environment variables – Store API keys outside source code.

Logging – Add persistent logs for API access attempts.

Encryption – Encrypt keylogger output files.

More labs – e.g., password strength checker, file integrity monitor, basic encryption tool.

Security and Ethics Notice
All labs are for educational purposes only.
Every script is designed to run on 127.0.0.1 (localhost) or on the user's own machine. None of the labs transmit data over a network (unless explicitly testing a local API).

Port Scanner – Only scans 127.0.0.1 by default. Never scan systems you do not own.

Vulnerable API – Uses fake data. Do not deploy publicly.

API Key Protected API – Hardcoded key for learning. Real applications should use environment variables.

Keylogger – Requires typed consent "I AGREE" and stops immediately on ESC. Use only on your own computer.

By using or cloning this repository, you agree to use these labs responsibly and only in controlled, authorised environments.

License
Educational / portfolio use only. No warranty.

---

Copy everything from the first line (`# Python Security Labs`) to the last line (`No warranty.`). Then paste it into your GitHub repository’s main `README.md` editor and commit.
