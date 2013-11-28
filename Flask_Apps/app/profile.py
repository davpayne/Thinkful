from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/portfolio')
def portfolio():
	return render_template("portfolio.html")

@app.route('/map')
def map():
	return render_template("map.html")

@app.route('/quotes')
def quotes():
    return render_template("quotes.html")

if __name__ == "__main__":
	app.run(debug=True)
