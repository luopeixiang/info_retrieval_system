import os
from multiprocessing import Pool
from collections import Counter

from Doc import doc
from util import preprocess


import pandas as pd
from pandas import DataFrame
import numpy as np


class Documents(object):
    """文档类"""


    def __init__(self, data_dir, output_dir="DATA",
                    index_file="index.pkl", vocab_file="vocab.csv"):
        self.data_dir = data_dir
        if not os.path.isdir(output_dir):
            os.mkdir(output_dir)
        self.output_dir = output_dir
        self.index_file = os.path.join(output_dir, index_file)
        self.vocab_file = os.path.join(output_dir, vocab_file)

    def __len__(self):
        return len(os.listdir(self.data_dir))


    def _process_document(self, abs_path):
        """处理单个文档 返回文档的id以及 这个文档中每个词出现的次数"""
        document = doc(abs_path)

        content = document.article + document.abstract
        #分词 去掉禁用词 之后进行词性还原
        content_tokens = preprocess(content)

        return document.id_, Counter(content_tokens)


    def process_documents(self):
        """解析所有文档  返回一个tf-idf索引"""
        documents_path = ( os.path.join(self.data_dir, s) for s in os.listdir(self.data_dir) )
        pool = Pool(os.cpu_count())
        results = {}

        for doc_id, counter in list(pool.imap_unordered(self._process_document, documents_path, chunksize=64)):
            results[doc_id] = counter

        return results

    def generate_index(self, save=True):
        """生成索引 并进行保存"""
        results = self.process_documents()

        #大型稀疏矩阵
        df = DataFrame(results, dtype=np.float32)
        df = df.fillna(0)

        #文档的数量
        doc_num = len(list(df.columns))

        #增加一列 是每个单词在多少个文档中出现的值 这是单词出现的总次数
        count_series = df.sum(axis=1)
        #增加一列 每个单词在多少个文档中出现
        doc_count_series = (df > 0).sum(axis=1)

        #计算tf
        df = df/df.sum()
        tf_columns = list(df.columns)

        df['idf'] = np.log(doc_num/doc_count_series)

        #计算tf-idf
        #import pdb;pdb.set_trace()
        for col in tf_columns:
            #计算tf-idf
            df[col] *= df['idf']
            #正则化  将每个文档的向量归一成单位向量
            df[col] = df[col]/np.sqrt(sum(df[col]*df[col]))

        df['count'] = count_series
        df['doc_count'] = doc_count_series
        #按照idf值进行排序  大的在后面
        df = df.sort_values(by='idf')

        #进行保存
        if save:
            df.to_csv(self.vocab_file, index_label="word", columns=['count', 'doc_count', 'idf'])
            df = df.drop(columns=['count', 'doc_count', 'idf'])
            df.to_pickle(self.index_file)
            print("索引保存完毕!")
