from flask import Flask, render_template, request
app = Flask(__name__)

to_do_list = []


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST" and request.form["newItem"] != '':
        to_do_list.append(request.form["newItem"])
    return render_template("index.html", listOfITems=to_do_list)


if __name__ == "__main__":
    app.run(debug=True)