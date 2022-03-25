from flask import Flask, request, render_template, redirect, url_for
from src.store import store
from src.extract import extract
from src.remove import remove
from src.search import search
# from src.error import InputError, ConnectionError


app = Flask(__name__)

# home route


@app.route("/", methods=["POST", "GET"])
def flask_home():
    if request.method == "POST":
        if request.form["HomeButton"] == 'Store Invoice':
            return(redirect(url_for("flask_store")))
        elif request.form["HomeButton"] == 'Extract Invoice':
            return(redirect(url_for("flask_extract")))
        elif request.form["HomeButton"] == 'Delete Invoice':
            return(redirect(url_for("flask_remove")))
        elif request.form["HomeButton"] == 'Search Invoice':
            return(redirect(url_for("flask_search")))
    else:
        return render_template("Home.html")

# store route


@app.route("/store", methods=["POST", "GET"])
def flask_store():
    # Get User Input
    if request.method == "POST":
        fname = request.form["FileName"]
        xmlfile = request.form["XML"]
    # Check if store function stores it properly
        try:
            store(xmlfile, fname)
            return 'success'
        except Exception as e:
            return 'failure'     
    else:
        return render_template("storeMain.html")

# remove route
@app.route("/remove", methods=["POST", "GET"])
def flask_remove():
    # Get User Input
    if request.method == "POST":
        fname = request.form["FileName"]
        print(fname)
    # Check if store function stores it properly
        try:
            remove(fname)
            return 'success'
        except Exception as e:
            return 'failure'
            # raise e
    else:
        return render_template("deleteMain.html")

# extract route
@app.route("/extract", methods=["POST", "GET"])
def flask_extract():
    # Get User Input
    if request.method == "POST":
        fname = request.form["FileName"]
    # Check if store function stores it properly
        try:
            xmlf = extract(fname)
            print(type(xmlf[1]))

            return xmlf[1]
        except Exception as e:
            return e

    else:
        return render_template("extractMain.html")


@app.route("/search", methods=["POST", "GET"])
def flask_search():
    # Get User Input
    sender_name = []
    issue_date = []
    if request.method == "POST":
        sender_name.append(request.form["senderName"])
        issue_date.append(request.form["senderDate"])
    # Check if store function stores it properly
        try:
            ret_l = search(issue_date, sender_name)
            # print(ret_l)
            return ret_l

        except Exception as e:
            # print (e)
            return "failure"
    else:
        return render_template("searchMain.html")


if __name__ == '__main__':
    app.debug = True
    app.run()
