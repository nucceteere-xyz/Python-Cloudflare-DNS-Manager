import requests
import sys
from dotenv import load_dotenv
load_dotenv() 
import os

api_key = os.environ['API_KEY']
zone_id = os.environ['ZONE_ID']
url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records"
record = input("What type of record so you want to add?\n")

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}


def create_dns_record_type_generic(headers):
    targetIP = input("'A' record Target\n")
    name = input(f"Name that will point at {targetIP}\n")
    owner_email = input(f"Email information of the Registrar of {name}\n")
    askproxy = input("Enable CloudFlare proxy? (y/n)\n")
    if record == "NS" or record == "MX":
        proxy = False
    elif askproxy == "y":
        proxy = True
    else:
        proxy = False
    print(proxy)
    data = {
        "type": f"{record}",
        "name": f"{name}",
        "content": f"{targetIP}",
        "ttl": 3600,
        "proxied": proxy,
        "comment": f"Email: {owner_email}",
        "priority": 0
    }
    global response
    response = requests.post(url, json=data, headers=headers)


if record == "A" or record == "MX" or record == "AAAA" or record == "NS":
    create_dns_record_type_generic(headers)
    print(response.json())
else:
    print("Invalid input, only A, AAAA, MX, NS type records are available for now.")
