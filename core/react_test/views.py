from flask import render_template, Blueprint
import requests
import json
from flask import Flask
from flask import jsonify

app = Flask(__name__)

react_blueprint = Blueprint('hello',__name__)



@react_blueprint.route("/")
def hello():
  return "Hello World!"

payload = {'X-API-Key': 'RNsY79C0pFXWa1vFWwmmV2XMMKxPCXuey9y7uOAl'}
r = requests.get('https://api.propublica.org/congress/v1/115/senate/members.json', headers=payload)
#print(r.text)

@react_blueprint.route("/data")

def data():
	members = json.loads(r.text) 	#['results'][0]['members']
	print(members)
	return render_template("base.html", members = members)
