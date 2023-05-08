import pandas as pd
import requests
import json
import time

client_code=""
client_secret=""
client_id="101992"

def getStravaTokens():
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

    return True

def getStravaData(num):
    ## Get the tokens from file to connect to Strava
    with open('strava_tokens.json') as json_file:
        strava_tokens = json.load(json_file)
        
    ## If access_token has expired then use the refresh_token to get the new access_token
    if strava_tokens['expires_at'] < time.time(): #Make Strava auth API call with current refresh token
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
                "average_speed",
                "max_speed",
                "average_cadence",
                "average_heartrate",
                "max_heartrate",
                "end_latlng",
        ]
    )

    while True:
        
        # get page of activities from Strava
        r = requests.get(url + '?access_token=' + access_token + '&per_page=100' + '&page=' + str(page))
        r = r.json()
        
        # if no results then exit loop
        if (not r):
            return False
        # otherwise add new data to dataframe
        for x in range(len(r)):
            if num <= 0:
                return True
            # checks to see if we have a run and nessecary data
            if (r[x]['type'] == 'Run') & r[x]['has_heartrate']:
                activities.loc[x + page-1,'id'] = r[x]['id']
                activities.loc[x + page-1,'name'] = r[x]['name']
                activities.loc[x + page-1,'start_date_local'] = r[x]['start_date_local']
                activities.loc[x + page-1,'type'] = r[x]['type']
                activities.loc[x + page-1,'distance'] = r[x]['distance']
                activities.loc[x + page-1,'moving_time'] = r[x]['moving_time']
                activities.loc[x + page-1,"average_speed"] = r[x]["average_speed"]
                activities.loc[x + page-1,"max_speed"] = r[x]["max_speed"]
                activities.loc[x + page-1,"average_cadence"] = r[x]["average_cadence"]
                activities.loc[x + page-1,"average_heartrate"] = r[x]["average_heartrate"]
                activities.loc[x + page-1,"max_heartrate"] = r[x]["max_heartrate"] 
                activities.loc[x + page-1,'end_latlng'] = r[x]['end_latlng']
                activities.to_csv('strava_activities.csv')
                num -= 1
                
        return True

def getData(lookupWord, index):
    data = pd.read_csv('strava_activities.csv')
    return data[lookupWord].iloc[index]