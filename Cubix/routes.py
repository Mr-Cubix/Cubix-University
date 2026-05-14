from flask import render_template, url_for
from Cubix import app


@app.route("/")
@app.route("/home")
def home():
    return render_template(
        "index.html",
        title="Home",
        stylesheet="css/index.css",
        script="js/index.js",
        active_page="home",
    )


@app.route("/about")
def about():
    return render_template(
        "about.html",
        title="About",
        stylesheet="css/about.css",
        active_page="about",
    )


@app.route("/program")
def program():
    return render_template(
        "program.html",
        title="Program",
        stylesheet="css/program.css",
        script="js/program.js",
        active_page="program",
    )


@app.route("/admission")
def admission():
    return render_template(
        "admission.html",
        title="Admission",
        stylesheet="css/admission.css",
        active_page="admission",
    )


@app.route("/contact")
def contact():
    return render_template(
        "contact.html",
        title="Contact Us",
        stylesheet="css/contact.css",
        script="js/contact.js",
        active_page="contact",
    )
