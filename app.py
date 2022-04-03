from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'This is API for 2022 ntu magic night.'

import db_info
from generate_seats import generate_seats_data
#test to insert data to the data base
@app.route("/test")
def test():
    db_info.mydb.collection.insert_one({"name": "John"})
    return "Connected to the data base!"

@app.route("/insertSeats")
def insertSeats():
    seats_list = generate_seats_data()
    mycol = db_info.mydb.seats  #collections
    mycol.insert_many(seats_list)
    return "insert seats done"


import json
from bson import json_util
@app.route("/getSeats")
def getSeats():
    mycol = db_info.mydb.seats
    data = mycol.find()
    data = list(map(lambda x: json.loads(json_util.dumps(x)), data))
    return jsonify(data)

from flask import request
@app.route("/setSeats", methods=['POST'])
def setSeats():
    jsonData = request.get_json()

    mycol = db_info.mydb.seats

    for id in jsonData:
        sold = jsonData[id]['sold']
        row = jsonData[id]['row']
        col = jsonData[id]['col']
        query = {"row": row, "col": col}
        new_value = { "$set": { "sold": 1 } }
        mycol.update_one(query, new_value )

    return jsonify({'result':'success'})

@app.route("/postTest", methods=['POST'])
def postTest():
    jsonData = request.get_json()
    for id in jsonData:
        print(jsonData[id]['area'], jsonData[id]['row'], jsonData[id]['col'])
    return jsonify({'result':'success'})


@app.route("/clearAllSeats")
def clearAllSeats():
    mycol = db_info.mydb.seats
    mycol.delete_many({})
    return "刪除所有座位"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)