# visualization_service.py
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/visualize', methods=['POST'])
def visualize():
    data = request.json
    sorted_data = sorted(data, key=lambda x: x['model_response'])  # Assume 'model_response' field from the model API
    # You can use any visualization library here like matplotlib, bokeh, etc.
    return jsonify(sorted_data)

if __name__ == '__main__':
    app.run(port=5002)
