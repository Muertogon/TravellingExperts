from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/<name>')
def home(name):
    return render_template("index.html", content=name, radiation=999, gang=["joe", "mama", "kek"])

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.run()
