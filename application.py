import cs50
import csv
import os

from flask import Flask, jsonify, redirect, render_template, request

# Configure application
app = Flask(__name__)

# Reload templates when they are changed
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    """Disable caching"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET"])
def get_index():
    return redirect("/form")


@app.route("/form", methods=["GET"])
def get_form():
    return render_template("form.html")


@app.route("/form", methods=["POST"])
def post_form():
    # returning a different error message dependending from which fields are blank, starting from the top
    if not request.form.get("name"):
        return render_template("error.html", message="Please provide a name")
    elif not request.form.get("gender"):
        return render_template("error.html", message="Please choose a gender")
    elif not request.form.get("region"):
        return render_template("error.html", message="Please choose a region")
    elif not request.form.get("email"):
        return render_template("error.html", message="Please provide a valid e-mail address")
    elif not request.form.get("comment"):
        return render_template("error.html", message="Please leave a comment")

    # open csv file and append to next line what is inputed
    with open("survey.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow((request.form.get("name"), request.form.get("gender"), request.form.get(
            "region"), request.form.get("email"), request.form.get("comment")))
    # redirect to /sheet
    return redirect("/sheet")


@app.route("/sheet")
def get_sheet():
    # read the csv file to format sheet.htlm
    with open("survey.csv", "r") as file:
        reader = csv.reader(file)
        contacts = list(reader)
    return render_template("sheet.html", contacts=contacts)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
