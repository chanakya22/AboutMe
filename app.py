from flask import Flask
from datetime import datetime
import re
from flask import render_template

# TODO

app = Flask(__name__)

@app.route("/")
def landingpage():
    # return "Hello, Flask!"
    return render_template("home.html")

@app.route("/about/")
def about():
    # return "Hello, Flask!"
    return render_template("about.html")


@app.route("/portfolio/")
def portfolio():
    # return "Hello, Flask!"
    return render_template("portfolio.html")

@app.route("/home/")
def home():
    # return "Hello, Flask!"
    return render_template("home.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")



@app.route("/<name>")
def hello(name = None):
    # now = datetime.now()
    # formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # # Filter the name argument to letters only using regular expressions. URL arguments
    # # can contain arbitrary text, so we restrict to safe characters only.
    # match_object = re.match("[a-zA-Z]+", name)

    # if match_object:
    #     clean_name = match_object.group(0)
    # else:
    #     clean_name = "Friend"

    # content = "Hello there, " + clean_name + "! It's " + formatted_now
    # return content

    return render_template("landingpage.html",name=name,date=datetime.now())

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")

@app.after_request
def add_header(response):
    response.cache_control.no_store = True
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')



# TODO:
# SPA - for profile/experiences/contact/projects/            Home/Blog/Portfolio-Work/Skill/Contact