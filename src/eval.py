from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import syllables

# evaluates: number of lines, syllabel count per line
def structural(response, data):
    lines = response.split('\n')
    if len(lines) == data[0]:
        for line in lines:
            if syllables.estimate(line) > data[1]:
                return False
        return True
    return False 

def lineanalysis(line):
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(line)
    return sentiment_dict['compound']

# evaluates feel / sentiment of text (postive, neutral, negative)
def thematic(response, feel):
    score = 0
    for line in response.split('\n'): 
        score += lineanalysis(line)

    if feel in ['abysmal', 'horrible', 'terrible', 'awful']:
        return True if score < -0.1 else False
    elif feel == 'neutral':
        return True if score >= -0.1 and score <= 0.1 else False
    else:
        return True if score > 0.1 else False

# main evaluation method, starts the process of evaluating 
# structural and thematic parts of the response provided by gpt
def evaluate(response, structdata):
    return True if structural(response, structdata[:2]) and thematic(response, structdata[-1]) else False