from flask import Flask, request, jsonify

app = Flask(__name__)

db = {
    "9998887779": {
        "name": "Radhe Gupta",
        "city": "Mithapur",
        "sim": "Jio"
    }
}

@app.route('/')
def home():
    return "API Running ✅"

@app.route('/number')
def number():
    num = request.args.get('num')

    if num in db:
        return jsonify({
            "status": "success",
            "result": db[num]
        })
    else:
        return jsonify({
            "status": "not found"
        })

handler = app
