from flask import Flask, render_template
from data import *

app = Flask(__name__)

destinations = [
    {
        "name": "India",
        "flag": "india-images/india-flag.png",
        "url_function": "show_india",
    },
    {
        "name": "Egypt",
        "flag": "egypt-images/egypt-flag.png",
        "url_function": "show_egypt",
    },
    {
        "name": "Mexico",
        "flag": "mexico-images/mexico-flag.png",
        "url_function": "show_mexico",
    },
]


@app.route("/")
def homepage():
    return render_template(
        "index.html", destinations=destinations, bg_image="index-image.jpg"
    )


@app.route("/egypt")
def show_egypt():
    return render_template(
        "post.html",
        destinations=destinations,
        bg_image=egypt_data["image"],
        data=egypt_data,
    )


@app.route("/india")
def show_india():
    return render_template(
        "post.html",
        destinations=destinations,
        bg_image=india_data["image"],
        data=india_data,
    )


@app.route("/mexico")
def show_mexico():
    return render_template(
        "post.html",
        destinations=destinations,
        bg_image=mexico_data["image"],
        data=mexico_data,
    )


@app.route("/about")
def show_about():
    return render_template(
        "about.html", destinations=destinations, bg_image="about-image.jpg"
    )


if __name__ == "__main__":
    app.run(debug=True)
