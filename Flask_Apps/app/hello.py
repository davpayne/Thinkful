from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/template_test")
def template_test():
    rand_list = [0, 1, 2, 3, 4, 5]
    return render_template('layout.html', a_random_string="Heey, what's up!", a_random_list=rand_list)

if __name__ == "__main__":
    app.run()