from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", title="Trang chủ")

@app.route("/about")
def about():
    return "<h1>Trang giới thiệu</h1><p>Project test của Hoàng Tuấn Cương.</p>"