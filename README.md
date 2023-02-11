# active-art
active art is a generative art assignment which will be submitted as part of an assignment in Computational Creativity at the University of Kent

the project will either be music oriented or language oriented

*generate music* \
or \
*generate poem*

the data used to generate this art will be from strava activities and met office weatherdata from when the activity was done

## poem
generate strange poems with seemingly weird or strange words, but they use rhyming schemes and patterns

the program can then highlight this and show why it used certain words based on activity and rhyming scheme

Context-Free Grammar to determine sentence stucture?

Create something similar to CFGs but for poem structure, maybe a meld of different poem structures or a unique one for Active Art.

Poem structure determined by Strava activity data, here is an example of how the data could influence a poem:

| Strava data | Determines  | +/-         |
| ----------- | ----------- | ----------- |
| Active time spent on activity | Poem length (in sentences) | X |
| Distance | Amount of words in each sentence | X |
| Avg. Pace | Amount of letters in words | X |
| Avg. Heart-rate | Rhyme scheme or avg. / max amount of syllables in words | X |
| Avg. Cadence | Rhyme scheme or avg. / max amount of syllables in words | X |


### Step-by-step, high-level flow:
To generate a dataset of words to use, the program can be fed poems and we can label all the words according to their part-of-speech (pos-tagging)

With this new dataset of words, we can generate our new poem structure based on Strava data (see table above) and we can pick out words that will fit into our "CFG" based on the rules set by the Strava data.

Since the program uses the Strava API, it is already in their system and should be able to be used by others. Once a run is complete, the program could generate a poem and it could be posted as a part of the activity. (novelty)


### libraries:
- nltk (pos-tagging)

## music
do make the music with bpm and stuff

### libraries:
- midiutil
- mingus

# resources

**description:** how to make music with python \
**link:** [medium article](https://medium.com/@stevehiehn/how-to-generate-music-with-python-the-basics-62e8ea9b99a5) \
**accessed:** 8th of feb

**description:** english word frequency dataset \
**link:** [kaggle](https://www.kaggle.com/datasets/rtatman/english-word-frequency) \
**accessed:** 8th of feb

**description:** elements of poetry (poetry structure) \
**link:** [mondaysmadeeasy.com](https://mondaysmadeeasy.com/elements-of-poetry/) \
**accessed:** 8th of feb

**description:** categorizing and tagging words with python \
**link:** [POS-tagger](https://www.nltk.org/book_1ed/ch05.html) \
**accessed:** 8th of feb

**description:** poem dataset
**link:** [kaggle](https://www.kaggle.com/datasets/michaelarman/poemsdataset)
**accessed:** 10th of feb
