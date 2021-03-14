from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home_page():
	animals = ['bat', 'camel', 'cow', 'human', 'pig', 'rat', 'bird']
	variants = ['SARS CoV', 'SARS CoV 2', 'MERS CoV']
	# icons = [i + "-" + j for i in animals for j in variants]
	icons = animals
	return render_template('home_page.html', animals=icons, variants=variants)

@app.route('/results/<animal1>/<animal2>')
def result_page(animal1, animal2):
	return render_template("results.html")

if __name__ == '__main__':
	app.debug = True
	app.run(host = 'localhost', port = 5000)