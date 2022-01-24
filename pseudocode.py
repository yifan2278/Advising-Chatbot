import requests
import spacy


def get_class(q):
    # send request to NLPC to get result
    pass


def get_entity(q, q_class, ner):
    # extract named entity using spaCy
    # may need branching to extract different
    # entity for different class
    pass


def get_info(keyword):
    # search KB for keyword using elasticsearch
    pass


if __name__ == '__main__':
    # load spaCy model for entity extraction
    ner = ...
    # read input / classify using NLPC
    q = input('Hello')
    q_class = get_class(q)
    while q_class != GOODBYE:
        # branching for each possible class
        if q_class == GREETING:
            print('Hi')
        if q_class == PREREQ:
            # extract entity
            class_num = get_entity(q, q_class, ner)
            # search KB for info
            class_info = get_info(keyword=class_num)
            # format and output answer
            print(class_info)
        # other classes follow the same paradigm
        if ...:
            pass

        # read input / classify using NLPC
        q = input('Anything else I can help with?')
        q_class = get_class(q)
    
    print('Goodbye!')