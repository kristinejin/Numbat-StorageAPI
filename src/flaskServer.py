from flask import Flask, Response, request, render_template


app = Flask(__name__)

@app.route("/")
def flask_store():
    return render_template("store_html.html")
    
    

if __name__ == '__main__':
    app.debug = True
    app.run()