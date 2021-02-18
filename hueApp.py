import json
from flask import Flask, request, redirect, render_template
import requests
from tokens import Tokens



app = Flask(__name__)

url = 'http://'+Tokens['bridge-IP']+'/api/' + Tokens['bridge-username'] 

@app.route('/')
def home():

    return render_template('index.html')

@app.route('/lights')
def lightsOn():

    r = request

    requests.put(url + '/lights/3/state', data = json.dumps({'on':True})).json()

    return redirect('/')

@app.route('/lightsOff')
def lightsOff():
    
    r = request

    requests.put(url + '/lights/3/state', data = json.dumps({'on':False})).json()

    return redirect('/')

if __name__=='__main__':

    app.run(debug=True, host='0.0.0.0')