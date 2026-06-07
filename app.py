from flask import Flask, render_template,request,send_file
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template("index.html")



@app.route('/contacts', methods = ["GET","POST"])
def contacts():
    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("messages.txt", "a", encoding="utf-8") as f:
            f.write("------New Message-------\n")
            f.write(f"Date: {now}\n")
            f.write(f"Name: {name}\n")
            f.write(f"Email: {email}\n")
            f.write(f"Message: {message}\n")
            f.write("--------------------------\n")

        return "پیام دریافت شد"
    return render_template("contacts.html")

@app.route("/resume")
def resume():
    return send_file(
        "static/resume.pdf",
        mimetype="application/pdf"
    )

if __name__ == "__main__":
    app.run()
