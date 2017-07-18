# /usr/bin/python
# -*- encoding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 1 Set important paths
import os

BASE = os.path.join(os.path.dirname(__file__), ".")
# DOCS = os.path.join(BASE, "data", "docs")
DOCS = os.path.join(BASE, "docs")

def get_documents(path=DOCS):
    """
    Returns a filtered list of paths to PDF files representing our corpus.
    """
    for name in os.listdir(path):
        # print 'name: ', name
        # if name.startswith('p') and name.endswith('.pdf'):
        if name.endswith('.pdf'):
            yield os.path.join(path, name)

# Print the total number of documents
# print(len(list(get_documents())))
# print 'HERE : ', list(get_documents())[0]
print 'BASE: ', BASE
print 'DOCS: ', DOCS

# 2 Create corpus
import re
import nltk
import codecs
import string
import subprocess
import unicodedata
from subprocess import PIPE, Popen

## Create a path to extract the corpus.
# CORPUS = os.path.join(BASE, "data", "corpus")
CORPUS = os.path.join(BASE, "corpus")
SEC = os.path.join(BASE, "section")
print 'CORPUS: ', CORPUS
print 'SECTIONS: ', SEC


def extract_corpus(docs=DOCS, corpus=CORPUS):
    """
    Extracts a text corpus from the PDF documents and writes them to disk.
    """
    # Create corpus directory if it doesn't exist.
    if not os.path.exists(corpus):
        os.mkdir(corpus)

    # For each PDF path, use pdf2txt to extract the text file.
    for path in get_documents(docs):
        # print 'Path: ', path

        # Call the subprocess command (must be on your path)
        # document = subprocess.check_output(
        #     ['pdftotxt', path, '-']
        # )
        document = Popen(['pdftotext', path, '-'], stdout=PIPE).communicate()[0]
        # print document
    
        # Encode UTF-u and remove non-printable characters
        document = filter(
            lambda char: char in string.printable,
            unicodedata.normalize('NFKD', document.decode('utf-8'))
        )

        # Write the document out to the corpus directory
        fname = os.path.splitext(os.path.basename(path))[0] + ".txt"
        outpath = os.path.join(corpus, fname)

        with codecs.open(outpath, 'w') as f:
            f.write(document)


# Run the extraction
# extract_corpus()


# 3 Descriptive Stastics
# Create an NLTK corpus reader to access text data on disk.
kddcorpus = nltk.corpus.PlaintextCorpusReader(CORPUS, '.*\.txt')

words = nltk.FreqDist(kddcorpus.words())
count = sum(words.values())
vocab = len(words)

print("Corpus contains vocabulary of {} and word count of {}.".format(vocab, count))
# exit()

# 4 extract the titles from the corpus
def titles(fileid=None,corpus=kddcorpus):
    """
    Use a regular expression to extract the titles from the corpus.
    """
    pattern = re.compile(r'^(.*)[\s]+[\s]?(.*)?')

    if fileid is not None:
        match = pattern.search(kddcorpus.raw(fileid))
        yield " ".join(map(lambda s: s.strip(), match.groups()))
    else:
        for fileid in corpus.fileids():
            # Search for a pattern match
            match = pattern.search(corpus.raw(fileid))

            if match:
                # If we find one, yield the space joined groups.
                yield " ".join(map(lambda s: s.strip(), match.groups()))

# for idx, title in enumerate(titles()):
#      print title
#      if idx >= 10:
#          break

# exit()

def extract_sec(fileids=None, corpus=kddcorpus, sec=SEC):
    if not os.path.exists(sec):
        os.mkdir(sec)

    # section == 'acknowledgements':
    # Get everything after section REFERENCES
    # section = re.compile('(?<=' + 'REFERENCES' + ')(.+)')
    section = re.compile('(?<=MATERIALS AND METHODS)(.+)')

    # Iterate through all text for each file id.
    fileids = fileids or corpus.fileids()
    # print section
    print 'fileids', fileids

    for fileid in fileids:
        text   = corpus.raw(fileid)
        # clean section title name
        # print text

    #     # Extract the text and search for the section target
        text   = re.sub('[\s]', " ", text)
        # print text
        target = section.search(text)
        
        if target:
            # group(0) The entire match, group(1) The first parenthesized subgroup.
            # yield fileid, target.group(0), target.group(1)
            print fileid, target.group(0)
            print "======================================="

# Run the extraction
# extract_sec()
# print 'HERE'
# exit()

# 5 pull sections from a file
def sectpull(fileids=None, section=None, corpus=kddcorpus):
    """
    Uses a regular expression to pull sections from a file:

        - "top": everything until the references section
        - "ref": the references and anything that follows.

    Yields the text as top, ref respectively.

    The sequence
    prog = re.compile(pattern)
    result = prog.match(string)
    is equivalent to
    result = re.match(pattern, string)

    re.sub(pattern, repl, string, count=0, flags=0)
    \s	Matches whitespace
    [aeiou]	Matches a single character in the listed set
    (	Indicates where string extraction is to start
    )	Indicates where string extraction is to end
    .	Matches any character
    *?	Repeats a character zero or more times (non-greedy)
    +	Repeats a character one or more times
    +?	Repeats a character one or more times (non-greedy)

    (?=...)
    Matches if ... matches next, but doesn’t consume any of the string.
    This is called a lookahead assertion. For example, Isaac (?=Asimov)
    will match 'Isaac ' only if it’s followed by 'Asimov'.

    (?<=...)
    >>> m = re.search('(?<=abc)def', 'abcdef')
    >>> m.group(0)
    'def'
    """

    # Select either a single fileid or a list of fileids
    section_name = section
    fileids = fileids or corpus.fileids()
    if section == None:
        section = None
    elif section == 'acknowledgements':
        # Get everything after section REFERENCES
        # section = re.compile('(?<=' + 'REFERENCES' + ')(.+)')
        section = re.compile('(?<=Acknowledgements)(.+)(?=REFERENCES)')

    elif section == 'references':
        # Get everything after section REFERENCES
        # section = re.compile('(?<=' + 'REFERENCES' + ')(.+)')
        section = re.compile('(?<=REFERENCES)(.+)')
    elif section == 'body':
        # Get everything before section REFERENCES
        # section = re.compile("(.+?)(?="+'REFERENCES'+ ")")
        section = re.compile("(.+?)(?=REFERENCES)")
    elif section == 'title':
        # Get everything before section ABSTRACT
        section = re.compile("(.+?)(?="+'ABSTRACT'+ ")")
    elif section == 'ner':
        # Get everything before section ABSTRACT
        section = re.compile('(?<=MATERIALS AND METHODS)(.+)(?=REFERENCES)')

    elif section == 'top':
        section = ["ABSTRACT","Abstract",'A B S T R A C T',"Bio","Panel Summary"]
        for sect in section:
            try:
                section = re.compile("(.+?)(?="+sect+ ")")
                break
            except:
                pass

    # Iterate through all text for each file id.
    for fileid in fileids:
        text   = corpus.raw(fileid)
        # clean section title name
        # prohibitedWords = ['Abstract', 'A B S T R A C T']
        # big_regex = re.compile('|'.join(map(re.escape, prohibitedWords)))
        # text = big_regex.sub("ABSTRACT", text)


        # Extract the text and search for the section target
        if section == None:
            # substitute whitespace with single space
            target = re.sub('[\s]', " ", text)
        else:
            text   = re.sub('[\s]', " ", text)
            target = section.search(text)

        if target:
            # print target.group(0)
            # print '=============='
            yield fileid, target.group(0), target.group(1)
        else:
            yield fileid, text, text
            
            # yield fileid, target.group(0)


# def refstats(fileids=None, section=None, corpus=kddcorpus):
#     """
#     Code to pull only the references section, store a character count, number
#     of references, as well as a "words per reference" count.

#     Pass either a specific document id, a list of ids, or None for all ids.
#     """
#     # Create reference number to match pattern
#     refnum  = re.compile(r'\[[0-9]{1,3}\]', re.I)

#     for fileid, top, refs in sectpull(fileids, section, corpus):

#         # Yield the statistics about the references
#         n_refs = len(set((refnum.findall(refs))))

#         words  = sum(1 for word in nltk.word_tokenize(refs))
#         wp_ref = float(words) / float(n_refs) if n_refs else 0

#         # Yield the data from the generator
#         yield (fileid, len(refs), n_refs, wp_ref)

def stats(fileids=None, section=None, corpus=kddcorpus):
    for fileid, top, refs in sectpull(fileids, section, corpus):
        # Yield the statistics about the references
        sents  = sum(1 for sent in nltk.sent_tokenize(top))
        words  = sum(1 for word in nltk.word_tokenize(top))
        # Yield the data from the generator
        yield (fileid, sents, words, int( float(words+1)/(sents+1) ))


from tabulate import tabulate
from operator import itemgetter
import random

# # Create table sorted by number of references
# # table = sorted(list(refstats(random.sample(kddcorpus.fileids(),15),section='body')))
# table = sorted(list(stats(kddcorpus.fileids(),section='ner')))

# # Print the table with headers
# headers = ('File', 'Sentences', 'Words', 'Words/Sentence')
# print(tabulate(table, headers=headers))
# exit()

# 6
# We need the top and references sections from p19.txt and p29.txt
# annotated = sectpull(['p1.txt', 'p2.txt', 'p11.txt'])
# annotated = sectpull(['p1.txt'])

# print 'title: ', list(titles(['p2.txt']))[0], type(list(titles(['p2.txt'])))
# # print 'body: ', list(sectpull(['p2.txt'], section='references'))[0][1], type(list(sectpull(['p2.txt'], section='top')))
# print 'body: ', list(sectpull(['pp1.txt'], section='body'))[0][1], type(list(sectpull(['p2.txt'], section='top')))
# exit()


from collections import defaultdict

from nltk import ne_chunk
# import polyglot
# from polyglot.text import Text
from nltk.tag import StanfordNERTagger


def polyglot_entities(fileids=None, section = None, corpus=kddcorpus):
    """
    Extract entities from each file using polyglot
    """
    results = defaultdict(lambda: defaultdict(list))
    fileids = fileids or corpus.fileids()

    for fileid in fileids:
        if section is not None:
            text = Text((list(sectpull([fileid],section=section))[0][1]))
        else:
            text = Text(corpus.raw(fileid))



        for entity in text.entities:
            etext = " ".join(entity)

            if entity.tag == 'I-PER':
                key = 'persons'
            elif entity.tag == 'I-ORG':
                key = 'organizations'
            elif entity.tag == 'I-locations':
                key = 'locations'
            else:
                key = 'other'

            results[fileid][key].append(etext)

    return results

def stanford_entities(model, jar, fileids=None, corpus=kddcorpus, section = None):
    """
    Extract entities using the Stanford NER tagger.
    Must pass in the path to the tagging model and jar as downloaded from the
    Stanford Core NLP website.
    """
    results = defaultdict(lambda: defaultdict(list))
    fileids = fileids or corpus.fileids()
    tagger  = StanfordNERTagger(model, jar)
    section = section

    for fileid in fileids:
        if section is not None:
            text = nltk.word_tokenize(list(sectpull([fileid],section=section))[0][1])
        else:
            text  = corpus.words(fileid)

        chunk = []

        for token, tag in tagger.tag(text):
            if tag == 'O':
                if chunk:
                    # Flush the current chunk
                    etext =  " ".join([c[0] for c in chunk])
                    etag  = chunk[0][1]
                    chunk = []

                    # if etag == 'PERSON':
                    #     key = 'persons'
                    # elif etag == 'ORGANIZATION':
                    #     key = 'organizations'
                    # elif etag == 'LOCATION':
                    #     key = 'locations'
                    # else:
                    #     key = 'other'

                    if etag == 'LOCATION':
                        key = 'locations'
                    else:
                        key = 'other'
                    results[fileid][key].append(etext)

            else:
                # Build chunk from tags
                chunk.append((token, tag))

    return results


def nltk_entities(fileids=None, section = None,corpus=kddcorpus):
    """
    Extract entities using the NLTK named entity chunker.
    """
    results = defaultdict(lambda: defaultdict(list))
    fileids = fileids or corpus.fileids()

    for fileid in fileids:
        if section is not None:
            text = nltk.pos_tag(nltk.word_tokenize(list(sectpull([fileid],section=section))[0][1]))
        else:
            text = nltk.pos_tag(corpus.words(fileid))



        for entity in nltk.ne_chunk(text):
            if isinstance(entity, nltk.tree.Tree):
                etext = " ".join([word for word, tag in entity.leaves()])
                label = entity.label()
            else:
                continue

            if label == 'PERSON':
                key = 'persons'
            elif label == 'ORGANIZATION':
                key = 'organizations'
            elif label == 'LOCATION':
                key = 'locations'
            elif label == 'GPE':
                key = 'locations'
            else:
                key = None

            if key:
                results[fileid][key].append(etext)

    return results

def iter_dict(ne, file_name):
    # Iterating over key and value of defaultdict dictionaries
    for key, value in ne[file_name].items():
        # print "%s - %s" % (str(key), str(value))
        print key, value[0:5]

# Only extract our annotated files.
# fids  = ['p1.txt', 'p2.txt', 'p3.txt', 'p4.txt', 'p5.txt', 'p6.txt','p7.txt', 'p8.txt', 'p9.txt','p10.txt']
# fids_noise  = ['pp1.txt', 'pp2.txt', 'pp3.txt', 'pp4.txt', 'pp5.txt', 'pp6.txt','pp7.txt', 'pp8.txt', 'pp9.txt','pp10.txt']
# fids  = ['p1.txt', 'p2.txt']
fids  = ['p1.txt']
# fids_noise  = ['pp1.txt', 'pp2.txt']
fids_noise  = ['pp1.txt']


# NLTK Entities
# nltkents = nltk_entities(fids,section='body')
# nltkents_noise = nltk_entities(fids_noise,section='body')
# nltkents = nltk_entities(kddcorpus.fileids(),section='ner')


print '=========== NLTK ==========='
# iter_dict(nltkents, 'p1.txt')
# iter_dict(nltkents, kddcorpus.fileids()[0])


# Polyglot Entities
# polyents = polyglot_entities(fids, section='top')
print '=========== Polyglot ==========='
# iter_dict(polyents, 'p1.txt')
# exit()


# Stanford Model Loading
# root  = os.path.expanduser('~/models/stanford-ner-2014-01-04/')
# model = os.path.join(root, 'classifiers/english.muc.7class.distsim.crf.ser.gz')
# jar   = os.path.join(root, 'stanford-ner-2014-01-04.jar')

# model = '/usr/share/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz'
# jar = '/usr/share/stanford-ner/stanford-ner.jar'

model = '/Users/yuleinku/Google Drive/cs_master/ner/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz'
jar = '/Users/yuleinku/Google Drive/cs_master/ner/stanford-ner/stanford-ner-3.4.jar'
# Stanford Entities
# stanents = stanford_entities(model, jar, fids, section='title')
# stanents = stanford_entities(model, jar, fids, section='top')
# stanents = stanford_entities(model, jar, fids, section='body')
# stanents = stanford_entities(model, jar, fids, section='references')
# stanents_noise = stanford_entities(model, jar, fids_noise, section='body')
print '=========== Stanford ==========='
stanents = stanford_entities(model, jar, kddcorpus.fileids(), section='ner')
print 'NER Processing Completed.'
# iter_dict(stanents, 'p1.txt')

# import numpy as np
# # Save
# # dictionary = {'hello':'world'}
# np.save('stanents.npy', stanents) 
# # Load
# # read_dictionary = np.load('city_to_state.txt').item()
# stanents = np.load('stanents.npy')

# import pickle

# with open('stanents.pickle', 'wb') as handle:
#     pickle.dump(stanents, handle)

# with open('stanents.pickle', 'rb') as handle:
#     stanents = pickle.load(handle)
import json

from city_to_state import city_to_state_dict
city_to_state = {}
city_to_state = city_to_state_dict

# print('Number of cities =', len(city_to_state.keys()))
# print(city_to_state['Los Angeles'])
# print(city_to_state['Ennis'])
# print(city_to_state['Long Branch'])

loc_dic = {}

for each in kddcorpus.fileids():
    # print '======================='
    # iter_dict(stanents, each)
    # print each
    file_n = each[:-8]
    # print file_n
    loc_dic[file_n] = {}
    for key, value in stanents[each].items():
        if key !='locations':
            continue
        # yield info, infors[info]['id'], infors[info]['journal'], infors[info]['date']
        # print key, value[0:5]
        for each in value:
            if each in city_to_state.keys():
                city = each
                state = city_to_state[city]
                break
    loc_dic[file_n]['city'] = city
    loc_dic[file_n]['state'] = state

print 'Dictionary Completed.'

with open('loc_dic.json', "w") as f:
    json.dump(loc_dic, f)
    print 'Save Completed.'

with open('loc_dic.json') as f:
    loc_dic_test = json.load(f)
    print 'Load Completed'

# print '======================='
# print loc_dic_test

exit()


with open('info/info_test.json') as f:
    infors = json.loads(f.read())

# def jsonstats(infors=infors):
#     for info in infors:
#         yield info, infors[info]['id'], infors[info]['journal'], infors[info]['date']


# table = sorted(list(jsonstats(infors)))
# # # Print the table with headers
# headers = ('File', 'ID', 'Journal', 'Date')
# print(tabulate(table, headers=headers))


# # finding the state based on geotags
# from geopy.geocoders import Nominatim

# # the Geonamescache library contains information
# # about continents, cities and US states
# import geonamescache

# # get a dictionary of cities: 'c'
# gc = geonamescache.GeonamesCache()
# c = gc.get_cities()

# # extract the US city names and coordinates
# US_cities = [c[key]['name'] for key in list(c.keys())
#              if c[key]['countrycode'] == 'US']
# US_longs = [c[key]['longitude'] for key in list(c.keys())
#             if c[key]['countrycode'] == 'US']
# US_latts = [c[key]['latitude'] for key in list(c.keys())
#             if c[key]['countrycode'] == 'US']

# print 'Number of US cities: ', len(US_cities)
# print 'Number of US_longs: ', len(US_longs)
# print 'Number of US_latts: ', len(US_latts)

# # how many cities exist more than once?
# import collections
# duplicates = [item for item, count in collections.Counter(US_cities).items() if count > 1]
# print(len(duplicates))
# print('')
# print(duplicates)

# def get_states(longs, latts):
#     ''' Input two 1D lists of floats/ints '''
#     # a list of states
#     states = []
#     # use a coordinate tool from the geopy library
#     geolocator = Nominatim()
#     for lon, lat in zip(longs, latts):
#         try:
#             # get the state name
#             location = geolocator.reverse(str(lat)+', '+str(lon))
#             state = location.raw['address']['state']
#         except:
#             # return empty string
#             state = ''
#         states.append(state)
#     return states

# # find the states of each city
# # WARNING: this takes a while
# US_states = get_states(US_longs, US_latts)
# print US_states
# print len(US_states)
# exit()
# # create a dictionary linking cities
# # as keys with their states
# city_to_state = {}
# for city, state in zip(US_cities, US_states):
#     if state:
#         city_to_state[city] = state

# print city_to_state
# output = json.dumps(city_to_state, ensure_ascii=False,indent=3)
# with open('city_to_state.json', 'wb') as outfile:
#     outfile.write(output)
# exit()

# with open('city_to_state.json') as f:
#     city_to_state = json.loads(f.read())

# import numpy as np





# exit()
info_ner = {}

def get_ner(infors=infors):
    for info in infors:
        title = info
        title_r = title.replace(':', '-').rstrip()
        title_r = title_r.replace('"', '')
        file_name = title_r + '.pdf.txt'
        city = ''
        state = ''
        # print 'file_name : ', file_name
        # print stanents[file_name].items()
        # file_name = os.path.join('/', title_r + '.pdf.txt')
        for key, value in stanents[file_name].items():
            if key !='locations':
                continue
            # yield info, infors[info]['id'], infors[info]['journal'], infors[info]['date']
            # print key, value[0:5]
            for each in value:
                if each in city_to_state.keys():
                    city = each
                    state = city_to_state[city]
                    break
            # yield info, infors[info]['id'], infors[info]['journal'], infors[info]['date'], value[0:5], city, state
            # yield infors[info]['id'], value[0:5], city, state
        info_ner[info] = {}
        info_ner[info]['id'] = infors[info]['id']
        info_ner[info]['date'] = infors[info]['date']
        print 'infors[info]["journal"] : ', infors[info]['journal']
        info_ner[info]['journal'] = infors[info]['journal']
        info_ner[info]['doi'] = infors[info]['doi']
        info_ner[info]['type'] = infors[info]['type']
        info_ner[info]['abstract'] = infors[info]['abstract']
        for i in range(5):
            author = 'author'+str(i+1)
            info_ner[info][author] = infors[info][author]

        info_ner[info]['city'] = city
        info_ner[info]['state'] = state


# table = sorted(list(get_ner(infors)))
# # # Print the table with headers
# headers = ('ID', 'Locations', 'City', 'State')
# print(tabulate(table, headers=headers))
get_ner()
print info_ner

with open('info_ner.json', "w") as f:
    json.dump(info_ner, f)

exit()

# stanents = stanford_entities(model, jar, fids, section='title')
# print stanents['p1.txt']['persons']
# stanents = stanford_entities(model, jar, fids, section='body')
# print stanents['p1.txt']['locations']
# stanents = stanford_entities(model, jar, fids, section='Acknowledgements')

'''
# print 'persons', stanents['p1.txt']['persons']
# print 'organizations', stanents['p1.txt']['organizations']
# print 'locations', stanents['p1.txt']['locations']
# p = stanents['p1.txt']['persons']
# o = stanents['p1.txt']['organizations']
# l = stanents['p1.txt']['locations']
#
# # Output to files
# import csv
# num = 0
# rows = zip(['PERSON']+p, ['ORGANIZATION']+o, ['LOCATION']+l)
# for file in os.listdir('paper_NER/'):
# 	if file != '.DS_Store':
# 		# print file
# 		num = num + 1
# 		# f = open('paper_NER/'+file)
# 		print file, type(file)
# 		file_name = file[:-4]
# 		print file_name
# 		path = 'csv_NER/'
# 		with open(path+file_name+'.csv', 'wb') as csvfile:
# 			# rows = zip('PERSON', 'ORGANIZATION', 'LOCATION')
# 			writer = csv.writer(csvfile)
# 			writer.writerows(rows)
# 		# myfile =
#
# exit()
'''

# 7
import pandas as pd
import json

# p1Authors = json.load(open('../data/p1Authors.json'))
# p1Authors = pd.read_csv('../data/p1Authors.csv')
p1Authors = pd.read_csv('./data/p1_Location.csv')
print p1Authors, type(p1Authors)

# df1 = pd.Series(polyents['p1.txt']['LOCATION'], index=None,
# dtype=None, name='Polyglot NERC Authors', copy=False, fastpath=False)

# df2=pd.Series([re.sub('\*',"",l) for l in stanents['p1.txt']['LOCATION']],
# index=None, dtype=None, name='Stanford NERC Authors', copy=False, fastpath=False)
#
# df3=pd.Series([re.sub('\*',"",l) for l in nltkents['p1.txt']['LOCATION']],
# index=None, dtype=None, name='NLTKStandard NERC Authors', copy=False, fastpath=False)
#
# df4 = pd.Series(p1Authors['LOCATION'], index=None,
# dtype=None, name='Hand-labeled True Authors', copy=False, fastpath=False)
#
# # met = pd.concat([df4,df3,df2,df1], axis=1).fillna('')
# met = pd.concat([df4,df3,df2], axis=1).fillna('')
# # met.to_csv('result.csv', sep=',', index=False)
# # print met

# print 'stanents : ', stanents, type(stanents), len(stanents.items())
# print 'stanents.items() : ', stanents.items(), type(stanents.items()), len(stanents.items())
# print 'stanents.items()[0] : ', stanents.items()[0], type(stanents.items()[0]), len(stanents.items()[0])


nltkents_all = []
for key, dic in nltkents.items():
    nltkents_all = nltkents_all + dic['locations']

stanents_all = []
for key, dic in stanents.items():
    stanents_all = stanents_all + dic['locations']

nltkents_noise_all = []
for key, dic in nltkents_noise.items():
    nltkents_noise_all = nltkents_noise_all + dic['locations']

stanents_noise_all = []
for key, dic in stanents_noise.items():
    stanents_noise_all = stanents_noise_all + dic['locations']


df2=pd.Series([re.sub('\*',"",l) for l in stanents_all],
index=None, dtype=None, name='Stanford NERC Authors', copy=False, fastpath=False)
df3=pd.Series([re.sub('\*',"",l) for l in nltkents_all],
index=None, dtype=None, name='NLTKStandard NERC Authors', copy=False, fastpath=False)
df4 = pd.Series(p1Authors['LOCATION'], index=None,
dtype=None, name='Hand-labeled True Locations', copy=False, fastpath=False)
met = pd.concat([df4,df3,df2], axis=1).fillna('')


# 8
# Calculations and logic from http://www.kdnuggets.com/faq/precision-recall.html
accuracy_plot = []
precision_plot = []
recall_plot = []
fmeasure_plot = []
def metrics(truth,run):
    # truth = truth
    # run = run
    truth = set(truth)
    run = set(run)

    TP = float(len(set(run) & set(truth)))
    # print 'truth: %r, run: %r, TP: %r.' % ( truth, run, TP )
    # print 'truth: %r, run: %r, TP: %r.' % ( len(truth), len(run), TP )
    if float(len(run)) >= float(TP):
        FP = len(run) - TP
    else:
        FP = TP - len(run)
    TN = 0
    if len(truth) >= len(run):
        FN = len(truth) - len(run)
    else:
        FN = 0

    # accuracy = (float(TP)+float(TN))/float(len(truth))
    # recall = (float(TP))/float(len(truth))
    accuracy = (float(TP)+float(TN))/float(len(run))
    precision = float(TP)/(float(FP)+float(TP))
    recall = (float(TP))/(float(TP)+float(FN))
    fmeasure = 2 * precision * recall / (precision+recall)

    accuracy_plot.append(accuracy)
    precision_plot.append(precision)
    recall_plot.append(recall)
    fmeasure_plot.append(fmeasure)
    print "The accuracy is %r" % accuracy
    print "The precision is %r" % precision
    print "The recall is %r" % recall
    print 'The F-measure is %r' % fmeasure
    print 'Total truth is %r' % len(truth)
    print 'Total run is %r' % len(run)
    print

    print '%r, %r, %.2f, %.2f, %.2f, %.2f' % ( len(truth), len(run), accuracy, precision, recall, fmeasure )

    d = {'Predicted Negative': [TN,FN], 'Predicted Positive': [FP,TP]}
    metricsdf = pd.DataFrame(d, index=['Negative Cases','Positive Cases'])

    return metricsdf




print
print
str2 = "=========== Hand Labeled Metrics ==========="
print str2.center(40, ' ')
print
print metrics(p1Authors['LOCATION'], [re.sub('\*',"",l) for l in p1Authors['LOCATION']])


print
print
str1 = "=========== NLTK Standard NERC Tool Metrics ==========="
print str1.center(40, ' ')
print
# print metrics(p1Authors['LOCATION'], [re.sub('\*',"",l) for l in nltkents['p1.txt']['locations']])
# print str1.center(40, ' ')
# print metrics([re.sub('\*',"",l) for l in nltkents['p1.txt']['locations']], [re.sub('\*',"",l) for l in nltkents_noise['pp1.txt']['locations']])

print metrics(p1Authors['LOCATION'], [re.sub('\*',"",l) for l in nltkents_all])
print str1.center(40, ' ')
print metrics([re.sub('\*',"",l) for l in nltkents_all], [re.sub('\*',"",l) for l in nltkents_noise_all])



print
print
str2 = "=========== Stanford NERC Tool Metrics ==========="
print str2.center(40, ' ')
print
# print metrics(p1Authors['LOCATION'], [re.sub('\*',"",l) for l in stanents['p1.txt']['locations']])
# print str1.center(40, ' ')
# print metrics([re.sub('\*',"",l) for l in stanents['p1.txt']['locations']], [re.sub('\*',"",l) for l in stanents_noise['pp1.txt']['locations']])

print metrics(p1Authors['LOCATION'], [re.sub('\*',"",l) for l in stanents_all])
print str1.center(40, ' ')
print metrics([re.sub('\*',"",l) for l in stanents_all], [re.sub('\*',"",l) for l in stanents_noise_all])



# print
# print
# str3 = "=========== Polyglot NERC Tool Metrics ==========="

# print str3.center(40, ' ')
# print
# print
# metrics(p1Authors['authors'],polyents['p1.txt']['persons'])


# 9 Plot histo
import matplotlib.pyplot as plt
import numpy as np
fig = plt.style.use('ggplot')

# df2 = pd.DataFrame(np.random.rand(3, 4), columns=['a', 'b', 'c', 'd'])
# df2.plot(kind='bar')
# plt.show()


# print accuracy_plot
# print precision_plot
# print recall_plot
# print fmeasure_plot
# df = pd.DataFrame( { 'celltype':['NLTK Chunker', 'Stanford NER', 'Polyglot NER'], 'Precision':x, 'Recall':y } )
df = pd.DataFrame( { 'celltype':['Hand Labeled','NLTK Chunker-clean','NLTK Chunker-noise/clean', 'Stanford NER-clean', 'Stanford NER-noise/clean'], 'Accuracy':accuracy_plot, 'Precision':precision_plot, 'Recall':recall_plot, 'F-measure':fmeasure_plot } )
df = df[ ["celltype", "Accuracy", "Precision", "Recall", "F-measure"] ]
df.set_index(["celltype"],inplace=True)
# 0red:#EC7063 , 1purple:#9B59B6 , 2blue:#3498DB, 3green:#7DCEA0 , 4pink:#E6B0AA , 5brown:#B9770E , 6orange:#F0B27A , 7gray: #85929E
c = [ '#f08080', '#9B59B6', '#3498DB', '#7DCEA0', '#D7BDE2','#B9770E', '#F0B27A', '#85929E' ]
fig = df.plot(kind='bar',alpha=1, rot=10, title='Performance Metrics for NER', fontsize=14, figsize=(10.5,8.5), color=[c[0], c[2], c[3], c[1]] )
# fig = df.plot(kind='bar',alpha=1, rot=10, title='Performance Metrics for NER', fontsize=10, figsize=(10.5,8.5), cmap='viridis' )
plt.xlabel("")
plt.ylabel("Score", fontsize=14)
# plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.25])
# plt.show()

# fig.set_size_inches(12.5, 10.5)
# # plt.savefig('NLTK_All_In_One.svg', dpi=100)
plt.savefig('figure.png', dpi=100)

# exit()


# 10
# A Simple Ensemble Classifier
# Create intersection of true authors from NLTK standard output
a =set(sorted(nltkents_all)) & set(p1Authors['LOCATION'])

# Create intersection of true authors from Stanford NER output
b =set(sorted(stanents_all)) & set(p1Authors['LOCATION'])

# Create intersection of true authors from Polyglot output
# c = set(sorted(polyents['p1.txt']['locations'])) & set(p1Authors['LOCATION'])

# Create union of all true positives from each NERC output
# (a.union(b)).union(c)
# print '====Create union of all true positives from each NERC output===='
# (a.union(b))

dfensemble = pd.Series(list((a.union(b))), index=None, dtype=None, name='Ensemble Method Authors',
                       copy=False, fastpath=False)
# met = pd.concat([df4,dfensemble,df3,df2,df1], axis=1).fillna('')
met = pd.concat([df4,dfensemble,df3,df2], axis=1).fillna('')
# print met

# print
# print
str = "=========== Ensemble NERC Metrics ==========="

print str.center(40, ' ')
print
print metrics(p1Authors['LOCATION'],list((a.union(b))))


exit()


df = pd.DataFrame( { 'celltype':['Hand Labeled','NLTK Chunker-clean','NLTK Chunker-noise/clean', 'Stanford NER-clean', 'Stanford NER-noise/clean', 'Ensemble Method'], 'Accuracy':accuracy_plot, 'Precision':precision_plot, 'Recall':recall_plot, 'F-measure':fmeasure_plot } )
df = df[ ["celltype", "Accuracy", "Precision", "Recall", "F-measure"] ]
df.set_index(["celltype"],inplace=True)
# 0red:#EC7063 , 1purple:#9B59B6 , 2blue:#3498DB, 3green:#7DCEA0 , 4pink:#E6B0AA , 5brown:#B9770E , 6orange:#F0B27A , 7gray: #85929E
c = [ '#f08080', '#9B59B6', '#3498DB', '#7DCEA0', '#D7BDE2','#B9770E', '#F0B27A', '#85929E' ]
fig = df.plot(kind='bar',alpha=1, rot=10, title='Performance Metrics for NER', fontsize=14, figsize=(10.5,8.5), color=[c[0], c[2], c[3], c[1], c[7]] )
# fig = df.plot(kind='bar',alpha=1, rot=10, title='Performance Metrics for NER', fontsize=10, figsize=(10.5,8.5), cmap='viridis' )
plt.xlabel("")
plt.ylabel("Score", fontsize=14)
# plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.25])
# plt.show()

# fig.set_size_inches(12.5, 10.5)
# # plt.savefig('NLTK_All_In_One.svg', dpi=100)
plt.savefig('figure2.png', dpi=100)


# 11
# Getting Your Data in Open File Format
# Add ensemble results for author to the nested python dictionary; use our functions

# p1={'docName':'p1.txt','ensembleLocation':list((a.union(b))),
#     'body':list(sectpull(['p1.txt'], section='body'))[0][1],
#     'title':list(titles(['p1.txt']))[0]}

# print 'title: ', list(titles(['p1.txt']))[0], type(list(titles(['p1.txt'])))
# print 'body: ', list(sectpull(['p1.txt'], section='top'))[0][1], type(list(sectpull(['p1.txt'], section='top')))
# exit()

# p1={'docName':'p1.txt','ensembleLocation':list((a.union(b))),
#     'body':list(sectpull(['p1.txt'], section='body'))[0][1],
#     'title':list(titles(['p1.txt']))[0]}
p1={'docName':'p1.txt','ensemble_Location':list((a.union(b)))}

# covert nested dictionary to json for open data storage
# json can be stored in mongodb or any other disk store
# output = json.dumps(p1['ensembleLocation'], ensure_ascii=False,indent=3)
output = json.dumps(p1, ensure_ascii=False,indent=3)

with open('data.txt', 'wb') as outfile:
    outfile.write(output)

# print out the authors section we just created in our json
# print json.dumps(json.loads(output)['ensembleLocation'],indent=3)

# uncomment to see full json output
# print json.dumps((json.loads(output)),indent=3)
