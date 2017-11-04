class MeaningFromJumbled:
    def __init__(self):
        self.english_dict_to_hash()


    def english_dict_to_hash(self):
        self.hashtable = {}
        with open('/usr/share/dict/words') as f:
            for line in f:
                word = line.strip('\n')
                sortedword = ''.join(sorted(word))
                #print line, type(line), type(s)
                self.hashtable.setdefault(sortedword ,[]).append(word)
                
    def getcorrectwords(self, word):
        sortedword = ''.join(sorted(word))
        return self.hashtable.get(sortedword)
        


    