# Active-Art 
Active-Art is a computational creativity system, written as part of a coursework assignement at the University of Kent.

-----
### Requirements
Active-Art is a python3 project and therefore requires a few libraries to be installed.

Install the following packages before attempting to run:
- vaderSentiment
- syllables
- pandas
- datapoint
- openai
-----
### How to run
Navigate to the `src/` dir and run the following command
```
python3 main.py 1
```
main.py takes one argument and it is the number of runs to retrieve from Strava, this will also then determine the number of poems generated.

-----
### Project breakdown
`main.py` : takes care of running the entire system

`promptgen.py` : generates a prompt using strava and weather data

`eval.py` : evaluates a response from gpt

`gpt.py` : handles requests to gpt

`strava.py` : handles requests to strava

`weather.py` : handles requests to datapoint (metoffice)

`results.txt` : artifacts (poems) are pasted here at the end of run-time, includes primer, prompt and poem

`artifacts-X.txt` : artifacts generated throughout the project's lifetime.

-------

### Disclaimer
The project uses my personal API keys and secrets for Datapoint, Strava and GPT. Therefore these are not shared. Please replace the dummy values with the ones that are need in `strava.py` and export your own API keys for datapoint and GPT under the names: `DATAPOINT_API_KEY` and `OPENAI_API_KEY`

To get access to the Strava API, a one time authentication has to be done in the browser once you have you API key. 