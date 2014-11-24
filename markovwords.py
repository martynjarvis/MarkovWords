import random
import sys
import pickle
import collections

FILENAME = 'lookup.p'

# TODO lookup should be a default dict, with a Counter in it

def generate_lookup(text_file):
    f = open(text_file)
    # (k,k) : [val,val,....]
    lookup = collections.defaultdict(collections.Counter)
    for word in f.readlines():
        i = j = None
        for k in word.strip().lower():
            lookup[(i,j)][k] += 1
            i = j
            j = k
        lookup[(i,j)][None] += 1
    pickle.dump(lookup, open( FILENAME, "wb" ))

def random_from_generator(elements):
    '''http://www.perlmonks.org/?node_id=1910'''
    return_val = None
    for n,e in enumerate(elements, start=1):
        if random.random() < 1.0/n:
            return_val = e
    return return_val

def generate_words(n):
    lookup = pickle.load(open( FILENAME, "rb" ))
    for i in range(n):
        i = j = None
        k = random_from_generator(lookup[(i,j)].elements())
        word = []
        while k is not None:
            word.append(k)
            i = j
            j = k
            k = random_from_generator(lookup[(i,j)].elements())
        print ''.join(word)

if __name__=='__main__':
    if 'process' in sys.argv:
        if len(sys.argv)>2:
            input_file = sys.argv[2]
        else:
            input_file = '/usr/share/dict/words'
        generate_lookup(input_file)
    elif 'gen' in sys.argv and len(sys.argv)>2:
        generate_words(int(sys.argv[2]))
    else:
        print "Usage: "
        print "python markovwords.py process [input_file]"
        print "python markovwords.py gen n"
