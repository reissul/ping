import argparse

from flask import Flask, request
import simplejson
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

def send_automated():
    config = simplejson.load(open(args.config))
    account_sid = config["sid"]
    auth_token = config["token"]
    client = Client(account_sid, auth_token)
    body = config["body"]
    number = config["number"]
    recipient = config["recipient"]
    message = client.messages.create(body=body, from_=number, to=recipient)


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    body = request.form['Body']
    if body.lower() in ["y", "ye", "yes"]:
        send_automated()
        response_body = "sent"
    else:
        response_body = "not sent"
    print(response_body)
    response = MessagingResponse()
    response.message(response_body)
    return str(response)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='.')
    parser.add_argument("--config", help="Config.", default="config.json")
    args = parser.parse_args()
    
    app.run(debug=True)
