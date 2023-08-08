import os
import subprocess
import sys

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_program', methods=['POST'])
def run_program():
    data = request.get_json()
    query = data['query']

    # Execute your Python program
    output = subprocess.check_output([sys.executable, 'chat.py', query])

    return jsonify({'output': output.decode()})

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
