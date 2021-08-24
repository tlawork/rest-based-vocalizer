from flask import Flask
from flask import request
import json
import os
import speake3
import base64

app = Flask(__name__)
engine = speake3.Speake()
engine.say("startup series talk version 1.3")
engine.talkback()

@app.route("/")
def hello_world():
    print("aaaaa")  
    test = "Hello to you. The Home Vocalizer is functioning."
    engine.say(test)
    engine.talkback()  
    return "<p>hello</p>"

@app.route("/say", methods=['POST'])
def saythis():
    print("bbbbb")
    payload = request.get_json()
    print(payload)
    print(payload['say'])
    if 'say' in payload.keys():
        engine.say(payload['say'])
        engine.talkback()
    # print(request.get_json())
    return json.dumps({'ok': True}), 200, {'ContentType':'application/json'}

@app.route("/playby/<num>", methods=['GET'])
def playby(num=0):
    print("ccccc2222222")
    if int(num) > 0:
        os.system( f"omxplayer -o local audio/hubitat-0{num}.mp3" )
    return json.dumps({'ok': True}), 200, {'ContentType':'application/json'}
    
    
@app.route("/json", methods = ['GET'])
def returnjson():
    try:
        with open("audio.json", "r") as f:
            jsondata = json.load(f)
            return json.dumps(jsondata), 200, {'ContentType':'application/json'}
    except:
        return json.dumps({'ok': False}), 500, {'ContentType':'application/json'}


@app.route("/playsay", methods=['POST'])
def playandsaythis():
    print("ddddd")
    payload = request.get_json()
    print(payload)
    if 'mp3' in payload.keys():
        os.system(f"omxplayer -o local audio/{payload['mp3']}")
    if 'say' in payload.keys():
        engine.say(payload['say'])
        engine.talkback()
    return json.dumps({'ok': True}), 200, {'ContentType':'application/json'}


@app.route("/upload", methods=['POST'])
def uploadthis():
    try:
        print(request.headers)
        raw_data = request.get_data()
        with open('export.zip', 'wb') as theFile:
            theFile.write(raw_data) 
        return json.dumps({'ok': True}), 200, {'ContentType':'application/json'}
    except:
        return json.dumps({'ok': False}), 500, {'ContentType':'application/json'}

