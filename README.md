RMSSD Assignment: 
# Sentiment Analysis for Fake News
19th November 2019

## OVERVIEW
**Training:** Trained a Naive Bayes classifier using any 800 news headlines from the dataset. 

**Evaluation:** Using the trained model, report the accuracy of the remaining 60 headlines.

## Preprocessing steps used:
1. Removed non-English entries in the given dataset.
2. Read modified .csv files and converted into Pandas data frames.
3. Dropped the first two columns of the dataset as they were not required.
4. Removed punctuations in the headlines by clean().
5. Tokenized the sentences into a list of words by nltk.tokenize.word_tokenize().
6. Removed stop words by remstop() using nltk.corpus.stopwords.
7. Tagged each word with the category of part of speech they belong to using nltk.pos_tag().
8. Collected the prepositions, nouns, pronouns, participle and verbs
9. Lemmatized the words collected using nltk.stem.WordNetLemmatize.lemmatize().
10. Converted words to lowercase.
11. Made feature words out of the words that occur more than twice so that there aren't any classifications on words that are irrelevant.

## Assumptions
* Assumed we do not need to run the classifier on the non-English headlines and thus removed 3 entries leaving us with 857 total headlines. 
* Trained the classifier on 800 entries and tested on 57.

## Observations
* ["IN", "NN”, "NNP", "PRP", "PRP$”, "RP", "VBP"]
The prepositions, nouns, pronouns, participle and verbs in the headlines were the most descriptive of the headlines in our context and relevance.

* There wasn’t much difference found in lemmatizing and stemming the words as reflected by the classifier accuracy, however, lemmatizing seemed to be a slightly more accurate method.

## Accuracy value:
**92.98245614035088**

## Files
* Dataset folder contains the modified datasets used as mentioned above.
* .ipynb and .py files contain the running code
* Pickle dump of the trained model of the Naive Bayes classifier used, saved as naivebayes.pickle
