from flask import Flask 
from flask_cors import CORS
from Database import collections
from flask_mail import Mail,Message
import os
from dotenv import load_dotenv


app = Flask(__name__)

CORS(app)
load_dotenv()

app.config.update(
    MAIL_SERVER="smtp.gmail.com",
    MAIL_PORT="465",
    MAIL_USE_SSL=True,
    MAIL_USERNAME=os.environ.get("MAIL_USERNAME"),
    MAIL_PASSWORD=os.environ.get("MAIL_PASSWORD"),
)
mail = Mail(app)


@app.route("/insert")
def syayaya():
    collections.insert_one({"name":"ashraf"})
    return "inserted"

@app.route("/")
def syaya():
    collections.insert_one({"name":"ahaenene"})
    return "inserted"

@app.route("/mail")
def mailll():
    msg = Message(
        "backend testing mail",
        sender=os.environ.get("MAIL_USERNAME"),
        recipients=['2023bca113@axiscolleges.in'],
        body="your testing is succesfull",
        
    )
    mail.send(msg)
    return "sended succesfully"





app.run(host='0.0.0.0', port=3000)