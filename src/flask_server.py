from flask import Flask, request, render_template, redirect, url_for
from src.store import store
from src.extract import extract
from src.remove import remove
from src.search import search
from flask_cors import CORS
# from src.error import InputError, ConnectionError

from src.error import InputError
from json import dumps

app = Flask(__name__)
CORS(app)

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
        password = request.form["Password"]
        fname = request.form["FileName"]
        xmlfile = request.form["XML"]
    # Check if store function stores it properly
        try:
            store(xmlfile, fname, password)
            return 'success'
        except Exception:
            raise InputError(description="Wrong xml input type or Password")
    else:
        return render_template("storeMain.html")

# remove route


@app.route("/remove", methods=["POST", "GET"])
def flask_remove():
    # Get User Input
    if request.method == "POST":
        fname = request.form["FileName"]
        password = request.form["Password"]
    # Check if store function stores it properly
        try:
            response = remove(fname, password)
            if response == 200:
                return '200'
            else:
                return InputError(description="failed to remove file: incorrect file name or password")
        except Exception as e:
            return e
            # raise e
    else:
        return render_template("deleteMain.html")

# extract route


@app.route("/extract", methods=["POST", "GET"])
def flask_extract():
    # Get User Input
    if request.method == "POST":
        password = request.form["Password"]
        fname = request.form["FileName"]
    # Check if store function stores it properly
        try:
            xml = extract(fname, password)
            if xml == None:
                raise InputError(
                    description="file not found with given filename and password")
            else:
                return xml[0]
        except Exception as e:
            return e

        # try:
        #     xmlf = extract(fname, password)
        #     return xmlf
        # except Exception as e:
        #     return e

    else:
        return render_template("extractMain.html")


@app.route("/search", methods=["POST", "GET"])
def flask_search():
    # Get User Input
    sender_name = []
    issue_date = []
    if request.method == "POST":
        password = request.form.get("Password")
        sender_name.append(request.form.get("sender_name"))
        issue_date.append(request.form.get("issue_date"))
        try:
            ret_l = search(issue_date, sender_name, password)
            return dumps({"file_names": ret_l})
        except Exception:
            raise InputError(description="Incorrect search key(s) or Password")
    else:
        return render_template("searchMain.html")


if __name__ == '__main__':
    app.debug = True
    app.run()
