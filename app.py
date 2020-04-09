import numpy
from flask import Flask, request, jsonify, render_template
import random
import json
#wait
app = Flask(__name__)
#preprocess and load functions
chain = json.load(open('chain.json', 'r'))

def predf(chain):
	w1 = random.choice(list(chain.keys()))
	s = w1.capitalize()
	for i in range(199):
		w2 = random.choice(chain[w1])
		w1 = w2
		s += ' ' + w2
	return s

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
	input = request.form["text"]
	res = predf(chain)
	return render_template("index.html",prediction_text = res)

if __name__ == "__main__":
	app.run(debug=True)
