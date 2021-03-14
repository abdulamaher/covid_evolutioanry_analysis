from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home_page():
	animals = ['bat', 'camel', 'cow', 'human', 'pig', 'rat', 'bird']
	return render_template('home_page.html', animals=animals)

@app.route('/results/<animal1>/<animal2>')
def result_page(animal1, animal2):
	return "Comparison of " + animal1 + " and " + animal2

if __name__ == '__main__':
	app.debug = True
	app.run(host = 'localhost', port = 5000)