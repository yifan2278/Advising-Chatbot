import spacy


if __name__ == '__main__':
    # load the saved model
    nlp = spacy.load('./ner/ner_course/')

    doc = nlp(u"Available sections of ece 2020")
    print(doc.ents)
    doc = nlp(u"Available sections of cse 3521")
    print(doc.ents)
    doc = nlp(u"Available sections of cse1110")
    print(doc.ents)
    doc = nlp(u"Available sections of ece2020")
    print(doc.ents)
    doc = nlp(u"Available sections of ise 7200")
    print(doc.ents)
    doc = nlp(u"Available sections of math 7200")
    print(doc.ents)
    doc = nlp(u"Available sections of chem 7200")
    print(doc.ents)
    doc = nlp(u"Available sections of cse 5523")
    print(doc.ents)
    doc = nlp(u"Available sections of cse5526")
    print(doc.ents)
    doc = nlp(u"Available sections of engr 1181")
    print(doc.ents)