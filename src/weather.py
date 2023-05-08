import datapoint, json, os

datapoint_key = os.getenv("DATAPOINT_API_KEY")

def getWeather(latlng):
    l = json.loads(latlng)
    conn = datapoint.connection(api_key=datapoint_key)
    #site = conn.get_nearest_observation_site(l[0], l[1]) #UNABLE TO DO THIS DUE TO CLOSEST SITE BEING MORE THAN 30KM AWAY
    #observation = conn.get_observations_for_site(site.id, "daily")
    
    # Have to do the current weather of when the request is made.
    site = conn.get_nearest_forecast_site(l[0], l[1])
    forecast = conn.get_forecast_for_site(site.id, "daily")
    current_timestep = forecast.now()
    weather = current_timestep.weather.text.lower()
    return weather if "day" in weather else weather + " day"