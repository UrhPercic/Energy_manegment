from flask import Flask, jsonify
from QRparser import parse_qr_codes

app = Flask(__name__)

@app.route('/api/attributes', methods=['GET'])
def get_active_attributes():
    active_attributes = parse_qr_codes()
    return jsonify(active_attributes)

if __name__ == '__main__':
    app.run(debug=True)
