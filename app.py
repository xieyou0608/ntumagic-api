from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'hello first api'

@app.route('/seat', methods=['POST'])
def post_seat():
    inputs = request.get_json()
    row = inputs['seat_row']
    num = inputs['seat_num']
    print(f'row: {row}\nseat: {num}')

    return jsonify({'return': 'ok!'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)