from flask import Flask, Response, request, render_template, redirect, url_for
from store import storeInvoice
from extract import extract
from remove import removeInvoice


app = Flask(__name__)


@app.route("/", methods=["POST","GET"])
def flask_home():
    if request.method == "POST":
        if request.form["HomeButton"] == 'Store Invoice':
            return(redirect(url_for("flask_store")))
        elif request.form["HomeButton"] == 'Extract Invoice':
            return(redirect(url_for("flask_extract")))
        elif request.form["HomeButton"] == 'Delete Invoice':
            return(redirect(url_for("flask_remove")))
    else:
        return render_template("Home.html")

@app.route("/store", methods=["POST","GET"])
def flask_store():
    #Get User Input
    if request.method == "POST":
        fname = request.form["fnm"]
        xmlfile = request.form["xmll"]
    #Check if store function stores it properly
        try:
            storeInvoice(xmlfile,fname)
            return render_template("savedS.html")
        except Exception as e:
            return render_template("savedF.html")
            raise e

    else:
        return render_template("storeMain.html")

@app.route("/remove", methods=["POST","GET"])
def flask_remove():
    #Get User Input
    if request.method == "POST":
        fname = request.form["dfm"]
        print(fname)
    #Check if store function stores it properly
        try:
            removeInvoice(fname)
            return render_template("DeleteS.html")
        except Exception as e:
            print(e)
            return render_template("DeleteF.html")
            raise e

    else:
        return render_template("deleteMain.html")

@app.route("/extract", methods=["POST","GET"])
def flask_extract():
    #Get User Input
    if request.method == "POST":
        fname = request.form["efn"]
    #Check if store function stores it properly
        try:
            fname,xmlf = extract(fname)
            return render_template("extractS.html", xmll = xmlf)
        except Exception as e:
            return render_template("extractF.html")
            raise e

    else:
        return render_template("extractMain.html")
    
if __name__ == '__main__':
    app.debug = True
    app.run()