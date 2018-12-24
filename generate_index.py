
"""
读入索引
解析 查询

进行索引
"""
from time import time

from query import Answer_query,INDEX
from documents import Documents


# DATA_DIR = '/home/luo/HomeWork/news_retrieval/Data/cnn_samples'
#
# q = "loop"
# qa = Answer_query(q)
#
# start = time()
# qa.search(DATA_DIR)
# print("cost {}s".format(time()-start))

if __name__ == "__main__":
    DATA_DIR = "/home/luo/HomeWork/news_retrieval/Data/cnn_5000"
    start = time()
    print("正在建造索引...")
    docs = Documents(DATA_DIR, output_dir="DATA/cnn_5000/")
    docs.generate_index()
    point1 = time()
    print("花费时间： {}s ".format(point1-start))
    #39s  float64 位存储  726M
