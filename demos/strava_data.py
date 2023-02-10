import pandas as pd
import requests
import json
import time

client_id="101992"
client_secret="da51c4b2e8b5043a23f4a7420a8f28e0488eaded"

## Get the tokens from file to connect to Strava
with open('strava_tokens.json') as json_file:
    strava_tokens = json.load(json_file)
    
## If access_token has expired then use the refresh_token to get the new access_token
if strava_tokens['expires_at'] < time.time():#Make Strava auth API call with current refresh token
    response = requests.post(
                        url = 'https://www.strava.com/oauth/token',
                        data = {
                                'client_id': client_id,
                                'client_secret': client_secret,
                                'grant_type': 'refresh_token',
                                'refresh_token': strava_tokens['refresh_token']
                                }
                    )
    
    #Save response as json in new variable
    new_strava_tokens = response.json()
    
    # Save new tokens to file
    with open('strava_tokens.json', 'w') as outfile:
        json.dump(new_strava_tokens, outfile)
    
    #Use new Strava tokens from now
    strava_tokens = new_strava_tokens
    
#Loop through all activities
page = 1
url = "https://www.strava.com/api/v3/athlete/activities"
access_token = strava_tokens['access_token']## Create the dataframe ready for the API call to store your activity data
activities = pd.DataFrame(
    columns = [
            "id",
            "name",
            "start_date_local",
            "type",
            "distance",
            "moving_time",
            "elapsed_time",
            "total_elevation_gain",
            "end_latlng",
            "external_id"
    ]
)

while True:
    
    # get page of activities from Strava
    r = requests.get(url + '?access_token=' + access_token + '&per_page=1' + '&page=' + str(page))
    r = r.json()
    
    # if no results then exit loop
    if (not r):
        break
    
    # otherwise add new data to dataframe
    for x in range(len(r)):
        activities.loc[x + page-1,'id'] = r[x]['id']
        activities.loc[x + page-1,'name'] = r[x]['name']
        activities.loc[x + page-1,'start_date_local'] = r[x]['start_date_local']
        activities.loc[x + page-1,'type'] = r[x]['type']
        activities.loc[x + page-1,'distance'] = r[x]['distance']
        activities.loc[x + page-1,'moving_time'] = r[x]['moving_time']
        activities.loc[x + page-1,'elapsed_time'] = r[x]['elapsed_time']
        activities.loc[x + page-1,'total_elevation_gain'] = r[x]['total_elevation_gain']
        activities.loc[x + page-1,'end_latlng'] = r[x]['end_latlng']
        activities.loc[x + page-1,'external_id'] = r[x]['external_id']# increment page
    
    page += activities.to_csv('strava_activities.csv')