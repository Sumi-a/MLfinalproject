import xml.etree.ElementTree as ET
import pandas as pd
from collections import defaultdict, Counter

# Load and parse the SentiSense categories XML
categories_tree = ET.parse('sentisense_cats.xml')
categories_root = categories_tree.getroot()

# Create a dictionary to map emotional categories and antonyms
emotional_categories = {}
for category in categories_root.findall('EmotionalCategory'):
    name = category.get('name')
    antonym = category.get('antonym')
    emotional_categories[name] = antonym

# Load and parse the SentiSense corpus XML
corpus_tree = ET.parse('sentisense_corpus.xml')
corpus_root = corpus_tree.getroot()

# Create a dictionary for the corpus with words as keys and emotions as values
senti_corpus = defaultdict(list)
for concept in corpus_root.findall('Concept'):
    gloss = concept.get('gloss')  # The description of the concept
    emotion = concept.get('emotion')
    if gloss:
        words = gloss.replace('"', '').split()  # Extract words from the gloss
        for word in words:
            senti_corpus[word.lower()].append(emotion)

# Function to categorize a list of keywords using the SentiSense corpus
def categorize_emotion(keywords, corpus):
    """
    Takes a list of keywords and matches them to emotions using the SentiSense corpus.
    Returns a list of emotions found in the keywords.
    """
    emotions_found = []
    for word in keywords:
        if word.lower() in corpus:
            emotions_found.extend(corpus[word.lower()])
    return list(set(emotions_found))  # Return unique emotions

# Read the films.csv file
films_df = pd.read_csv('film.csv')

# Initialize a list to store the results
results = []

# Iterate over each row to extract keywords and categorize emotions
for index, row in films_df.iterrows():
    keywords = row['keywords'].split()  # Split the keywords string into a list
    emotions = categorize_emotion(keywords, senti_corpus)
    
    # Append the data to the results list
    results.append({
        'index': row['index'],
        'genres': row['genres'],
        'title': row['title'],
        'senti_emotions': ', '.join(emotions) if emotions else 'None'
    })

# Create a new DataFrame from the results
senti_df = pd.DataFrame(results)

# Save the new DataFrame to a CSV file
senti_df.to_csv('filmSenti.csv', index=False)

# Print confirmation and a preview of the new CSV
print("New CSV file 'filmSenti.csv' created successfully!")
print(senti_df.head())
