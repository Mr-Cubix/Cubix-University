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


@app.route("/dashboard")
def dashboard():
    return render_template(
        "student_portal/dashboard.html",
        title="Dashboard",
        stylesheet="css/student_portal_css/dashboard.css",
        script="js/dashboard.js",
        active_page="dashboard",
    )


@app.route("/myprofile")
def myprofile():
    return render_template(
        "student_portal/myprofile.html",
        title="My Profile",
        stylesheet="css/student_portal_css/myprofile.css",
        script="js/myprofile.js",
        active_page="myprofile",
    )


@app.route("/academics")
def academics():
    return render_template(
        "student_portal/academics.html",
        title="Academics",
        stylesheet="css/student_portal_css/academics.css",
        script="js/academics.js",
        active_page="academics",
    )


@app.route("/mycourses")
def mycourses():
    return render_template(
        "student_portal/mycourses.html",
        title="My Courses",
        stylesheet="css/student_portal_css/mycourses.css",
        script="js/mycourses.js",
        active_page="mycourses",
    )


@app.route("/attendance")
def attendance():
    return render_template(
        "student_portal/attendance.html",
        title="Attendance",
        stylesheet="css/student_portal_css/attendance.css",
        script="js/attendance.js",
        active_page="attendance",
    )


@app.route("/result")
def result():
    return render_template(
        "student_portal/result.html",
        title="Result",
        stylesheet="css/student_portal_css/result.css",
        script="js/result.js",
        active_page="result",
    )


@app.route("/timetable")
def timetable():
    return render_template(
        "student_portal/timetable.html",
        title="Timetable",
        stylesheet="css/student_portal_css/timetable.css",
        script="js/timetable.js",
        active_page="timetable",
    )


@app.route("/schoolfees")
def schoolfees():
    return render_template(
        "student_portal/schoolfees.html",
        title="School Fees",
        stylesheet="css/student_portal_css/schoolfees.css",
        script="js/schoolfees.js",
        active_page="schoolfees",
    )


@app.route("/notices")
def notices():
    return render_template(
        "student_portal/notices.html",
        title="Notices",
        stylesheet="css/student_portal_css/notices.css",
        script="js/notices.js",
        active_page="notices",
    )


@app.route("/downloads")
def downloads():
    return render_template(
        "student_portal/downloads.html",
        title="Downloads",
        stylesheet="css/student_portal_css/downloads.css",
        script="js/downloads.js",
        active_page="downloads",
    )


@app.route("/settings")
def settings():
    return render_template(
        "student_portal/settings.html",
        title="settings",
        stylesheet="css/student_portal_css/settings.css",
        script="js/settings.js",
        active_page="settings",
    )


@app.route("/logout")
def logout():
    return render_template(
        "student_portal/logout.html",
        title="Logout",
        stylesheet="css/student_portal_css/logout.css",
        script="js/logout.js",
        active_page="logout",
    )
