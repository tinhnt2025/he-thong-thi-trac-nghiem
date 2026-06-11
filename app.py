
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        return redirect(url_for("home"))
    return render_template("login.html")

@app.route("/admin")
def admin_dashboard():
    return render_template("admin/dashboard.html")

@app.route("/add_question", methods=["GET", "POST"])
def add_question():
    if request.method == "POST":
        subject = request.form.get("subject")
        question = request.form.get("question")
        answer = request.form.get("answer")
        return redirect(url_for("add_question"))
    return render_template("add_question.html")

@app.route("/import_excel", methods=["GET", "POST"])
def import_excel():
    if request.method == "POST":
        file = request.files.get("excel")
        return redirect(url_for("import_excel"))
    return render_template("import_excel.html")

@app.route("/results")
def results():
    return render_template("results.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
