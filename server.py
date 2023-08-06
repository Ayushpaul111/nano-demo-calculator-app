from flask import Flask, request
app = Flask(__name__)

@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    response_content = "Code:200\nContent:hello world!"
    return response_content, 200, {'Content-Type':'text/plain'}

@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.json
    first = data['first']
    second = data['second']
    result = first + second
    
    response_content = f"Status code:200\nContent:{{ result: {result} }}"
    return response_content, 200, {'Content-Type':'text/plain'}

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.json
    print("Received data:", data) 
    first = data['first']
    second = data['second']
    result = first - second
    
    response_content = f"Status code:200\nContent:{{ result: {result} }}"
    return response_content, 200, {'Content-Type':'text/plain'}


if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')