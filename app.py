
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

# Home page (student quiz interface placeholder)
@app.route("/")
def home():
    return "<h1>Hệ thống thi trắc nghiệm trực tuyến</h1><p>Trang thi được giữ nguyên từ notebook.</p>"

# Admin dashboard
@app.route("/admin")
def admin_dashboard():
    return render_template("admin/dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)
