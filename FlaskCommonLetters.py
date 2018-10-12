from flask import Flask, jsonify, request, json
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route('/findcommonletters', methods=['POST'])
def findcommonletters():

    # Retrieve the json that ws sent in the request
    some_json = request.get_json()

    # Access the values in sentence and letters and put them into a string
    s1 = some_json.get('sentence')
    s2 = some_json.get('letters')

    # Convert the strings into sets and find common letters between the sets using the '&' operator and store them in a list
    a = list(set(s1) & set(s2))

    # Return the list of common letters in JSON format
    return jsonify({'letters': a}), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
