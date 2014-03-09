from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/results', methods=['POST'])
def results():
    meal_cost = float(request.form['meal_cost'])
    tip_percentage = float(request.form['tip_percentage'])
    result = meal_cost*(tip_percentage/100)
    return render_template('results.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)