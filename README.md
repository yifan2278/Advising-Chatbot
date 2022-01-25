# CSE-Advising-Chatbot

A chatbot capable of answering basic frequenly asked CSE advising questions.

[test_NLPC.py](test_NLPC.py) gives an example of using [NLPC](https://github.com/osu-cse-5914/natural-language-processing-classifier) in Python. Clone [NLPC](https://github.com/osu-cse-5914/natural-language-processing-classifier), run start.py, and run [test_NLPC.py](test_NLPC.py).

[test_spaCy.py](test_spaCy.py) gives an example of using  [spaCy](https://spacy.io/usage/training#training-data) to extract named entities. Here, it extracts the course number (e.g., CSE 5914).

[test_elasticsearch.py](test_elasticsearch.py) gives an example of using  [Elasticsearch](https://www.elastic.co/downloads/elasticsearch). Download Elasticsearch on the website. Run bin\elasticsearch.bat. Run [test_elasticsearch.py](test_elasticsearch.py).

## Pipeline

1. Read user input
2. Classify input into one of the supportd categories using [NLPC](https://github.com/osu-cse-5914/natural-language-processing-classifier)
3. Extract target entity from the input using [spaCy](https://spacy.io/usage/training#training-data)
4. Search for corresponding desired information in the knowledge base
5. Format and output the information

## Class Label Definitions

* GREETING
* GOODBYE
* PREREQ
* RELATED-COURSES (e.g., What are the AI related courses)
* TOPICS (e.g., What is CSEXXXX about)
* WHO-TEACH
* TEACH-WHAT
* AVAILABLE-SEC
* NOT-SUPPORTED
* **TODO**

**Note: Data format must match the definition by [NLPC](https://github.com/osu-cse-5914/natural-language-processing-classifier).**

## Named Entity Definitions

* COURSE
* INSTRUCTOR
* TRACK (e.g., AI, Database)
* **TODO**

**Note: Data format must match that in [test_spaCy.py](test_spaCy.py).**

## Search KB for Answer

**TODO**
