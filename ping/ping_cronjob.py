import argparse

import simplejson
from twilio.rest import Client

def send_reminder():
    config = simplejson.load(open(args.config))
    account_sid = config["sid"]
    auth_token = config["token"]
    client = Client(account_sid, auth_token)
    number = config["number"]
    sender = config["sender"]
    body = "Send automated message? Y/N"
    message = client.messages.create(body=body, from_=number, to=sender)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='.')
    parser.add_argument("--config", help="Config.", default="config.json")
    args = parser.parse_args()
    
    send_reminder()
