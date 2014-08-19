import random
import sys
import pickle

FILENAME = 'lookup.p'

def generate_lookup():
    f = open('/usr/share/dict/words')
    # (k,k) : [val,val,....]
    lookup = {}
    for word in f.readlines():
        i = j = None
        for k in word.strip().lower():
            lookup.setdefault((i,j),[]).append(k)
            i = j
            j = k
        lookup.setdefault((i,j),[]).append(None)
    pickle.dump(lookup, open( FILENAME, "wb" ))

def generate_words(n):
    lookup = pickle.load(open( FILENAME, "rb" ))
    for i in range(n):
        i = j = None
        k = random.choice(lookup[(i,j)])
        word = []
        while k is not None:
            word.append(k)
            i = j
            j = k
            k = random.choice(lookup[(i,j)])
        print ''.join(word)

if __name__=='__main__':
    if 'process' in sys.argv:
        generate_lookup()
    elif 'gen' in sys.argv and len(sys.argv)>2:
        generate_words(int(sys.argv[2]))
    else:
        print "Usage: python markovwords.py [process | gen n]"
