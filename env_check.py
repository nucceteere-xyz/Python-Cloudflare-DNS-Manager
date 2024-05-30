from dotenv import load_dotenv
load_dotenv() 
import os

print(f"API Key: {os.environ.get('API_KEY')}")
print(f"Zone ID: {os.environ.get('ZONE_ID')}")
