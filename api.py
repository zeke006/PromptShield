# api.py
from flask import Flask, request, jsonify
from detect import detect_injection
from sanitize import sanitize_input
from utils import log_input

app = Flask(__name__)

@app.route('/scan', methods=['POST'])
def scan_input():
    """
    POST endpoint to scan and sanitize inputs.
    Expected JSON format: {"text": "user input"}
    Returns JSON with detection result, matched trigger, and sanitized text.
    """
    data = request.json
    text = data.get("text", "")
    
    flagged, trigger = detect_injection(text)
    sanitized = sanitize_input(text) if flagged else text

    log_input(text, flagged)

    return jsonify({
        "flagged": flagged,
        "trigger": trigger,
        "output": sanitized
    })

if __name__ == '__main__':
    app.run(debug=True)
