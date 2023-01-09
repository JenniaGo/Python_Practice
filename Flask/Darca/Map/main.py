from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://mongodb:27017/")
db = client["ticket-system"]

@app.route("/classrooms")
def classrooms():
    classrooms = db.classrooms.find()
    results = []
    for classroom in classrooms:
        results.append({
            "name": classroom["name"],
            "computers": [
                {
                    "number": computer["number"],
                    "status": computer["status"],
                }
                for computer in classroom["computers"]
            ],
        })
    return jsonify(results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
