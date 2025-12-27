from flask import Flask, render_template, request
import yagmail
app=Flask(__name__)
app.secret_key = "secret123" #Any key
@app.after_request
def no_cache(response):
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

@app.route("/", methods=["GET", "POST"])
def login():
    return render_template("index.html")
@app.route("/submit",methods=[ "POST"])
def home():
    name=request.form.get('name')
    password=request.form.get('subject')
    title=request.form.get('title')
    mail=yagmail.SMTP("EMAIL_ID", "PASSWORD")
    mail.send(
    to=name,
    subject=title,
    contents=password
)
    return render_template("submit.html", name=name, subject=password, title=title)
    
app.run(debug=True)
