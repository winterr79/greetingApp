from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "vshdbvzj_xfmdjxcs"

@app.route("/hello")
def index():
    flash("What's your name?")
    return render_template("index.html")

@app.route("/greet", methods=["POST"])
def greet():
    name = request.form["name_input"]
    flash("Hi " + name + ", great to see you!")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)