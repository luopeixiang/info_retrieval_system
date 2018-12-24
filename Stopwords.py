

from nltk.corpus import stopwords  #禁用词
import nltk

#但是stopword主要影响 index构建
class Stopwords(object):

    def __init__(self, name="nltk"):
        self.name = name

    def filter(self, words):
        if self.name == "nltk":
            nltk_stopwords = stopwords.words('english')
            return [ word for word in words if word not in nltk_stopwords]
        elif self.name == "not_noun":
            return [word for (word, pos) in nltk.pos_tag(words) if self.is_noun(pos)]
        elif self.name == "not_stop":
            return words

    def is_noun(self, pos):
        return pos[:2] == 'NN'
