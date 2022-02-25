# CSE-Advising-Chatbot

A chatbot capable of answering basic frequenly asked CSE advising questions.

## Getting Started
1. Run Python server inside the backend directory (port 8000)
```
python3 ./backend/server.py
```
2. Install dependencies and run Angular frontend inside the frontend directory (port 4200)
```
cd frontend
npm install
ng serve
```
3. Run Elastic Search version 7.12.1. as database (port 9200)
```
docker run --name elasticsearch -d -p 9200:9200 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.12.1
```


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
* SIMILAR-COURSES (e.g., What courses cover the similar topics to CSE 3521)
* RELATED-COURSES (e.g., What are the AI related courses)
  * RELATED-COURSES-AI
  * RELATED-COURSES-DATABASE
  * RELATED-COURSES-PYTHON
* TOPICS (e.g., What is CSEXXXX about)
* WHO-TEACH
* TEACH-WHAT
* AVAILABLE-SEC
* NOT-SUPPORTED
* **TODO**

**Note: Data format must match the definition by [NLPC](https://github.com/osu-cse-5914/natural-language-processing-classifier).**

## Named Entity Definitions

* COURSE (model in [test_spaCy.py](test_spaCy.py))
* INSTRUCTOR (use [pretrained model](https://spacy.io/models/en/))
* ~~TRACK (e.g., AI, Database)~~
* **TODO**

**Note: Data format must match that in [train_ner_course.py](./ner/train_ner_course.py).**

## Search KB for Answer

**TODO**
