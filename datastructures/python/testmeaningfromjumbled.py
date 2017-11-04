import meaningfromjumbled as mj

class Test:
    def setUp(self):
        self.mj = mj.MeaningFromJumbled()
        self.testwords = ['kura', 'karthi', 'jukn','bini','amtch',
                          'nimi', 'dog', 'for', 'exclusive','range',
                          'celebration','creation']


    def test_english_dict_to_hash(self):
        for word in self.testwords:
            print word, self.mj.getcorrectwords(word)