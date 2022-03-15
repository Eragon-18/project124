from flask import Flask, jsonify, request

app = Flask(__name__)

task = [
    {"contact": 9987644456, "name": "Raju", "done": False, "id": 1},
    {"contact": 9876543222, "name": "Rahul", "done": False, "id": 2},]

@app.route("/add-data", methods=["POST"])

def add_data():
    if not request.json:
        return jsonify({"Status": "error", "message": "Please provide data"}, 400)
    
    task = {"id": task[-1]["id"] + 1, "contact": request.json["contact"], "name": request.get("name", ""), "done": False}
    task.append(task)
    return jsonify({"Status": "success", "message": "Data added successfully"})

@app.route("/get-data", methods=["GET"])

def get_data():
    return jsonify({"data": task})

if __name__ == '__main__':
    app.run(debug = True)


