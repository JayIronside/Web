# import Flask
from flask import Flask, render_template
# initialise app variable
app = Flask(__name__)
# decorate a python function with app.route. It associates a web url with a defined function.
@app.route("/")
def home():
    return "This is the home page attached to my URL"

@app.route("/hello")
def hello():
    return "Hello World from Python Flask Web Framework!"
# run the app notice here that we can specify host. 0.0.0.0 means that the app will be accessible from all the IP
# addresses on the system including 127.0.0.1 which is localhost. The default port for Flask is 5000. You can use
# something else.

@app.route("/hello/<string:name>/")
def hello_with_person_name (name):
    return "Hello {}, greetings from Flask FrameWork!".format(name)

@app.route("/hello2/<string:name>/")
def hello_with_template(name):
    return render_template('hello.html', person_name=name)

@app.route("/hello3/<string:name>/")
def hello_with_layout(name):
    return render_template('hello-extend-layout.html', person_name=name)

if __name__ == "__main__":
    #app.run()
    app.run(host="0.0.0.0", port=int("5000"), debug=True)