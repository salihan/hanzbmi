from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    # return "homepage"
    return render_template("index.html")

@views.route("/profile")
def profile():
    args = request.args
    username = args.get("username")
    return render_template("index.html", name=username)
# @views.route("/profile/<username>")
# def profile(username):
#     return render_template("index.html", name=username)

@views.route("/json")
def get_json():
    return jsonify({
        'name': 'salihan',
        'age': 45
    })

@views.route("/data")
def get_data():
    data = request.data
    return jsonify(data)

@views.route("/red_home")
def red_home():
    return redirect(url_for("views.home"))

@views.route("/bmi")
def bmi():
    flash("Please enter the required data.")
    return render_template("bmi.html")

@views.route("/bmiresult", methods=["POST", "GET"])
def bmiresult():
    weight = float(request.form['in_weight'])
    height = float(request.form['in_height'])
    cat = "Normal"
    bmi = weight / height ** 2
    if bmi < 18.5:
        cat = "UNderweiGHT"
    elif bmi > 25:
        cat = "ovERWEIGht"
    flash(cat+" BMI with BMI value: "+str(round(bmi,2)))
    return render_template("bmi.html")