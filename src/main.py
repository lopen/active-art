from promptgen import genPrompt
from gpt import queryGPT
import strava
from eval import evaluate
import sys

# active-art main

def main():
    # grab strava tokens to pull data from strava
    #if not strava.getStravaTokens():
    #    print("Failed to get strava tokens.")
    #    print("Stopping program")
    #    return
    # grab strava data
    num = int(sys.argv[1])
    if not strava.getStravaData(num):
        print("Failed to get strava data")
        print("Stopping program")
        return

    for index in range(0,num,1):
        # generate prompt
        promptdata = genPrompt(index)
        prompt = promptdata[0]
        # system primer
        system = "You are a runner and poet, that enjoys writing poems about runs you have done. You also enjoy wordplay and clever rhyme schemes."
        # setup messages for initial query to GPT
        messages=[
            {"role": "system", "content": system},
            {"role": "assistant", "content": prompt}
        ] 
        score = 0
        response = ""
        # send prompt to gpt, evaluate response and repeat if needed
        while score < 1:
            response = queryGPT("gpt-3.5-turbo", messages)
            score = evaluate(response, promptdata[1:])
        
        print("Response found to fit evaluation, here is result:")
        f = open("results.txt", "a")
        f.write("""\n###################################################################################################################\n
        Prime:\n """ + system + """\n
        Prompt:\n """ + prompt + """\n
        Response:\n """ + response + """
        """)
        f.close()
        print(response)
    
main()

