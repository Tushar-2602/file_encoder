from flask import Flask,request,jsonify

app=Flask(__name__)


@app.route('/',methods=["POST"])
def sample():
    print(request.get_json())
    return jsonify({"aa":11})


if(__name__=="__main__"):
    app.run(debug=True,port=4000)