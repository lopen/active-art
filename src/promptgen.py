import random, math
from weather import getWeather
from strava import getData
# heartrate zones (0 - 4 index in list heartrateWords) and their associated words, 2 words per zone
# threshold for zones are from this site https://www.polar.com/blog/running-heart-rate-zones-basics/
#
#   Zone - Intensity - Percentage of HRMax
#   1      very light  50 - 60 %
#   2      light       60 - 70 % 
#   3      moderate    70 - 80 %
#   4      hard        80 - 90 %
#   5      maximum     90 - 100 %
#
synonym_list = [['minimal', 'scant', 'slight', 'negligible', 'faint', 'inconsiderable', 'minute', 'trifling', 'wee', 'petty'], 
                ['mild', 'soft', 'gentle', 'temperate', 'leisurely', 'docile', 'placid', 'tame', 'easy', 'calm'], 
                ['average', 'ordinary', 'moderate', 'middle-of-the-road', 'standard', 'tolerable', 'so-so', 'regular', 'conventional', 'median'], 
                ['strenuous', 'arduous', 'vigorous', 'robust', 'strenuous', 'stiff', 'grueling', 'strenuous', 'severe', 'tough'], 
                ['intense', 'extreme', 'rigorous', 'strong', 'ardent', 'feverish', 'vigorous', 'heightened', 'acute', 'maximal']]

def pickHRwords(avgHR, maxHR):
    return [synonym_list[pickZone(avgHR)][random.randint(0,9)], synonym_list[pickZone(maxHR)][random.randint(0,9)]]

# to find the zones I will use my own max etc - as it can vary from person to person
# max heartrate can be estimated by doing 220 - your age (24 in my case) for a max of 196
def pickZone(HR):
    maxHR = 210
    if maxHR * 0.9 <= HR:
        return 4
    elif maxHR * 0.8 <= HR:
        return 3
    elif maxHR * 0.7 <= HR:
        return 2
    elif maxHR * 0.6 <= HR:
        return 1
    else:
        return 0

def pickNumLines(distance, moving_time):
    lines = math.ceil((moving_time / 60) / (distance / 1000)) # <-- calcualtes pace
    # lines = math.ceil((moving_time / distance) * 10)
    return lines if lines < 10 else 10

def pickTone(latlng, time):
    # time does not get used, as the weather provides day only due to limitations.
    return getWeather(latlng)

def pickMaxSyl(cadence):
    return math.ceil(cadence / 10)

def pickFeel(avgspeed, maxspeed):
    words = ['abysmal', 'horrible', 'terrible', 'awful', 'neutral', 'pleasant', 'good', 'great', 'wonderful', 'fantastic']
    for i in range(9,0,-1):
        if maxspeed * (i / 10) <= avgspeed:
            return words[i]

# prompt generation
def genPrompt(index):
    avgHR = getData("average_heartrate", index)
    maxHR = getData("max_heartrate", index)
    latlng = getData("end_latlng", index)
    time = getData("start_date_local", index)
    avgspeed = getData("average_speed", index)
    maxspeed = getData("max_speed", index)
    distance = getData("distance", index)
    moving_time = getData("moving_time", index)
    cadence = getData("average_cadence", index)
    runname = getData("name", index)

    # theme, feel
    intensity = pickHRwords(avgHR, maxHR)
    tone = pickTone(latlng, time)
    feel = pickFeel(avgspeed, maxspeed)

    # structure
    lines = pickNumLines(distance, moving_time)
    syllables = pickMaxSyl(cadence)

    prompt = """
                Write a poem about a """ + runname.lower() + """ you have just completed.
                The poem must be """ + str(lines) + """ lines long, where the maximum number of syllables per line is """ + str(syllables) + """. 
                The poem must express feelings of """ + intensity[0] + """ and at times """ + intensity[1] + """ activity. 
                The poem must convey tones of a """ + tone + """ and must convey a feeling of a """ + feel + """ time.
            """
    return [prompt, lines, syllables, intensity, tone, feel]

