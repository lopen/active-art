import requests
import json

client_code="c693a4e4b58be7265fb4f6b6bec8c39e45737763"
client_secret="da51c4b2e8b5043a23f4a7420a8f28e0488eaded"
client_id="101992"

# Make Strava auth API call with your 
# client_code, client_secret and code
response = requests.post(
                    url = 'https://www.strava.com/oauth/token',
                    data = {
                            'client_id': client_id,
                            'client_secret': client_secret,
                            'code': client_code,
                            'grant_type': 'authorization_code'
                            }
                )#Save json response as a variable
strava_tokens = response.json()# Save tokens to file
with open('strava_tokens.json', 'w') as outfile:
    json.dump(strava_tokens, outfile)# Open JSON file and print the file contents 
# to check it's worked properly
with open('strava_tokens.json') as check:
  data = json.load(check)
print(data)