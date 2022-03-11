from flask import Flask, Response, request, render_template
from store import storeInvoice


app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
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
    
    

if __name__ == '__main__':
    app.debug = True
    app.run()