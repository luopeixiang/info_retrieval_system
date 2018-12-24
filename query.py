from os.path import join
from collections import Counter
import time

from util import preprocess, load_index
from util import VOCAB_FILE
from Doc import doc
from documents import Documents
from output import Results

import pandas as pd
from pandas import DataFrame
import numpy as np


INDEX = load_index()

class Answer_query(object):
    """这个类 将一个查询语句  解析成向量的形式 """
    def __init__(self, query_string, topk=10):
        """args:
            query_string:查询的字符串
            topk:返回的文档的个数

        """
        self.query_string = query_string
        self.query_tokens = preprocess(self.query_string)
        self.topk = topk

    def vectorize(self):

        q_vec = pd.Series(Counter(self.query_tokens), index=INDEX.index)
        q_vec = q_vec.fillna(0)
        #正则化
        q_vec = q_vec/np.sqrt(sum(q_vec*q_vec))

        return q_vec

    def search(self, data_dir, out="terminal"):
        """计算相似度 返回前topk个相关的文档"""
        vec = self.vectorize()
        similities = (INDEX.T*vec).sum(axis=1)

        #doc_index_scores = similities.nlargest(self.topk)
        #doc_index_scores = doc_index_scores[ doc_index_scores>0 ]
        doc_index_scores = similities[ similities>0 ]
        doc_index_scores = doc_index_scores.sort_values(ascending=False)

        results = Results(doc_index_scores, self.query_tokens, out)
        #打印文档的名字 以及相应的分值

        if out == "terminal":
            results.out_to_terminal()
        else:
            return results.get_results()

    def summary(self):
        """总结： 关键词是哪些呈现出来， 每个关键词出现总次数  文档数  idf值"""
        vocab = pd.read_csv(VOCAB_FILE)
        token_summary = {}
        for token in self.query_tokens:
            res = vocab[ vocab['word'] == token ]
            #import pdb;pdb.set_trace()
            if res.empty:
                continue
            info = list(res.iterrows())[0][1]
            token_summary[token] = dict(list(info.iteritems()))

        return token_summary








"""
if __name__ == "__main__":
    DATA_DIR = "/home/luo/HomeWork/news_retrieval/Data/cnn_samples"

    start = time.time()
    print("正在建造索引...")
    docs = Documents(DATA_DIR)
    docs.generate_index()
    point1 = time.time()
    print("花费时间： {}s ".format(point1-start))
    #39s  float64 位存储  726M
"""
