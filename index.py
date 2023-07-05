from flask import Flask, render_template, request, redirect, url_for
from gevent.pywsgi import WSGIServer
from gevent_ws import WebSocketHandler
from datetime import datetime
import json
import random
import urllib.parse

app = Flask(__name__)

# --reading data from .json file
with open('config.json','r') as c:
    params = json.load(c)["params"]


# --direct to a main template('/')
@app.route("/")
def Home():
    occasion = ['Friendship Day', 'Teacher\'s Day', 'New Year', 'Festivals', 'Special Occasions', 'Birthday', 'Valentines Day']
    tag = random.choice(occasion)
    return render_template('home.html', tag=tag)

# --direct to share template
@app.route("/<type>/<name>", methods=['GET','POST'])
def shared(name, type):
    if request.method == "POST":
        # name = request.form.get('name')
        return redirect(url_for('sharemore', type=type))
    else:
        return render_template('show_card.html', name=name, events=params[type], type=type, date=datetime.now())

# --direct to show card template
@app.route("/<type>", methods=['GET','POST'])
def sharemore(type):
    if request.method == "POST":
        name = request.form.get('name')
        url = request.url
        return render_template('share.html', name=name, encodedname=urllib.parse.quote(name), events=params[type], url=url, date=datetime.now())
    else:
        name = "{Your Name}"
        return render_template('show_card.html', name=name, events=params[type], type=type, date=datetime.now())


# --url for Privacy Policy Template
@app.route("/privacy_policy")
def Privacy():
    return render_template('privacy.html')

# --url for Terms & Conditions Template
@app.route("/terms_and_conditions")
def Terms():
    return render_template('terms.html')


if __name__=='__main__':
    # Debug/Development
    # app.run(debug=False, port=8000)
    # Production
    server = WSGIServer(('', 8000), app, handler_class=WebSocketHandler)
    server.serve_forever()