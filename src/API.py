from flask import Flask, jsonify
from QRparser import generate_active_attributes

app = Flask(__name__)

@app.route('/api/attributes', methods=['GET'])
def get_active_attributes():
    attributes_generator = generate_active_attributes()
    active_attributes = next(attributes_generator)
    return jsonify(active_attributes)

if __name__ == '__main__':
    app.run(debug=True)
