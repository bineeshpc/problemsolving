dictfile = '/usr/share/dict/words'

def getwords():
    with open(dictfile) as f:
        words = [x.strip('\n') for x in f.readlines()]
    return words

def process_anagrams():
    words = getwords()
    output = {}
    for word  in words:
        sorted_word = ''.join(sorted(word))
        output.setdefault(sorted_word, []).append(word)
    return output

def getanagrams(word):
    data = process_anagrams()
    sorted_word = ''.join(sorted(word))
    print 'anagrams of word {} are the following:'.format(word)
    for x in data[sorted_word]:
        if x != word:
            print x

getanagrams('listen')

def get_all_anagrams_of_length(n):
    data = process_anagrams()
    for key, value in data.iteritems():
        if len(key) == n and len(value) > 2:
            print value

get_all_anagrams_of_length(3)