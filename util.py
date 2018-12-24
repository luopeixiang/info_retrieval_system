
from nltk.corpus import stopwords  #禁用词
from nltk.tokenize import word_tokenize #分词
from nltk.stem import WordNetLemmatizer #词性还原

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from Stopwords import Stopwords


DATA_DIR = '/home/luo/HomeWork/news_retrieval/Data/cnn_samples'
INDEX_FILE = "./docs_tf-idf_index.pkl"
VOCAB_FILE = "./vocab.csv"


#STOPWORDS = stopwords.words('english')
stop = Stopwords('not_stop')

def preprocess(content):
    #分词 同时过滤掉禁用词
    content_tokens = [token for token in word_tokenize(content)]
    content_tokens = stop.filter(content_tokens)

    #词性还原
    wl = WordNetLemmatizer()
    content_tokens = [ wl.lemmatize(token) for token in content_tokens]

    return content_tokens


def load_index(index_file=INDEX_FILE):
    """加载索引文件"""
    index = pd.read_pickle(index_file)
    return index


def summary_results(results):
    """对结果进行总结 返回结果数  找到的相关行"""
    highlight_count = 0
    for result in results:
        highlight_count += len(result.highlights)

    return highlight_count





#绘制 idf值选取跟词汇表大小的关系
#用作缩减词汇表的 参考
def plot_idf_vocabsize(vocab_file):
    vocab = pd.read_csv(vocab_file)

    max_idf = vocab['idf'].max()
    min_idf = vocab['idf'].min()

    def y(x):
        return (vocab['idf'] > x).sum()

    x1 = np.linspace(0, max_idf+0.1/2.0, num=5000)
    x2 = np.linspace(max_idf+0.1/2.0, max_idf+0.1, num=15000)
    x = np.concatenate((x1,x2))

    plt.plot(x,np.array(list(map(y,x))))
    plt.xlabel('IDF')
    plt.ylabel('VOCAB SIZE')

    plt.show()
