import requests
import os

api_key = os.environ['API_KEY']
zone_id = os.environ['ZONE_ID']
url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records"
record = input("What type of record so you want to add?")

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}


def create_dns_record_typeA(headers):
    targetIP = input("'A' record Target\n")
    name = input(f"Name that will point at {targetIP}\n")
    owner_email = input(f"Email information of the Registrar of {name}\n")
    data = {
        "type": "A",
        "name": f"{name}",
        "content": f"{targetIP}",
        "ttl": 3600,
        "proxied": True,
        "comment": f"Email: {owner_email}"
    }
    global response
    response = requests.post(url, json=data, headers=headers)


if record == "A":
    create_dns_record_typeA(headers)
    print(response.json())
else:
    print("Invalid input, only A type records are available for now.")