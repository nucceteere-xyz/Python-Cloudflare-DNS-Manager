from dotenv import load_dotenv
load_dotenv() 
import os

print(os.environ.get('API_KEY'))
print(os.environ.get('ZONE_ID'))