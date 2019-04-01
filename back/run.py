from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/greeting")
def hello():
    return jsonify({'name': 'buddies', 'feel': 'good'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')