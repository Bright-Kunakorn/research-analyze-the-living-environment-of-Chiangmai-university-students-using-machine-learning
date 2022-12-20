from google.oauth2.credentials import Credentials

# Replace YOUR_API_KEY with your actual API key
creds = Credentials.from_api_key('YOUR_API_KEY')

# Import the Google Maps API client
from googleapiclient.discovery import build

# Build a service object to access the Google Maps API
service = build('maps', 'v1', credentials=creds)

# Make a request to the Google Maps API
response = service.geocode(address='1600 Amphitheatre Parkway, Mountain View, CA').execute()
print(response)
