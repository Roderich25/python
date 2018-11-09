from flask import Flask, render_template, request, redirect
import csv
import os
import smtplib

#configure application
app = Flask(__name__)

#resgistered persons
#persons = []

@app.route("/")
def index():
    name = request.args.get("name", "Flask")
    return render_template("index.html", name=name)

@app.route("/registered")
def registered():
    with open("registered.csv", "r") as file:
        reader = csv.reader(file)
        persons = list(reader)
    return render_template("success.html", persons=persons)

@app.route("/register", methods=["POST"])
def register():
    #init
    name = request.form.get("name")
    email = request.form.get("email")
    country = request.form.get("country")
    if not name or not email or not country:
        return render_template("failure.html")
    #persons.append(f"{name} from {country}")
    #email
    message = "Subject: Flask Register\n"+name + " from " + country + " you are now registered."
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("rodrigoavilasolis@gmail.com", os.getenv("PASSWORD"))
        server.sendmail("rodrigoavilasolis@gmail.com", email, message.encode("utf8"))
        print("Succesfully sent email")
    except smtplib.SMTPException:
        print("Error: unable to send email")
    #csv
    file = open("registered.csv", "a", newline='')
    writer = csv.writer(file)
    writer.writerow((name, email, country))
    file.close()
    return redirect("/registered")

if __name__ == '__main__':
    app.run(port=5000)
