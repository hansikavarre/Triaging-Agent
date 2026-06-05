from flask import Flask, request, jsonify
from flask_cors import CORS   # ADD THIS
from triage import classify_bug

app = Flask(__name__)
CORS(app)   

@app.route('/triage', methods=['POST'])
def triage():
    data = request.json
    bug_description = data.get("bug", "")

    result = classify_bug(bug_description)

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)