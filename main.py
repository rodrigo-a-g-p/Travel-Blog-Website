from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/egypt')
def show_egypt():
    return render_template('egypt.html')


@app.route('/india')
def show_india():
    return render_template('india.html')


@app.route('/mexico')
def show_mexico():
    return render_template('mexico.html')


@app.route('/about')
def show_about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)
