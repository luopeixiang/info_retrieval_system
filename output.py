from os.path import join

from Doc import doc
from util import preprocess
from util import DATA_DIR

"""
本文件实现两种展示结果的方法：
1.命令行
2.网页输出

共同点是他们接受类Answer_query 中answer方法计算得出的
doc_index_scores 以及 query_tokens 作为输入

读取源文件  经过分词、等步骤
(需要保存源文件 的内容)

做交集  看出哪些位置 有交叉
使用 word_index  sent_index 标出位置
返回

两个接口 对这个返回结果的方法处理不同
"""


class Result(object):

    def __init__(self, doc_id, query_tokens, score, out):
        self.doc_id = doc_id
        self.query_tokens = query_tokens
        self.score = format(score, ".4f")
        self.out = out

        self.doc_token_sents, self.num_sents, self.num_tokens = self.init_doc_sents()
        # 需要重点标出的区域
        self.highlight_pos = self.get_pos()
        self.highlights = self.get_highlights()

    def init_doc_sents(self):
        doc_path = join(DATA_DIR, str(self.doc_id) + '.story')
        document = doc(doc_path, return_sents_list=True)
        doc_sents = document.article + document.abstract
        # 返回文档中句子的长度  token的数量
        num_sents = len(doc_sents)
        doc_token_sents = list(map(preprocess, doc_sents))

        num_tokens = 0
        for sent in doc_token_sents:
            num_tokens += len(sent)

        return doc_token_sents, num_sents, num_tokens

    def get_pos(self):
        highlight_pos = []

        for sent_i, sent in enumerate(self.doc_token_sents):
            word_i_list = []
            for word_i, word in enumerate(sent):
                if word in self.query_tokens:
                    word_i_list.append(word_i)
            if word_i_list:
                highlight_pos.append((sent_i, word_i_list))

        return highlight_pos

    def out_to_terminal(self):
        print("新闻ID: ", self.doc_id)
        print("相似度: ", self.score)
        print("搜索到的相关句子:")
        print('\n'.join(self.highlights))
        print("-" * 50)

    def strong(self, word):
        if self.out == "terminal":
            OKGREEN = '\033[92m'
            ENDC = '\033[0m'
            return OKGREEN + word + ENDC
        else:
            return '<span style="color:blue;font-weight:bold">' \
                + word + "</span>"

    def get_highlights(self):
        highlights = []
        for sent_i, word_i_list in self.highlight_pos:
            for word_i in word_i_list:
                words = self.doc_token_sents[sent_i]
                words[word_i] = self.strong(words[word_i])
            highlight = str(sent_i + 1) + " " + " ".join(words)
            highlights.append(highlight)

        return highlights


class Results(object):

    def __init__(self, doc_index_scores, query_tokens, out="terminal"):
        assert out in ['terminal', 'html']
        self.doc_index_scores = doc_index_scores
        self.query_tokens = query_tokens
        self.out = out

    def get_results(self):
        results = []
        for doc_index, score in self.doc_index_scores.iteritems():
            result = Result(str(doc_index), self.query_tokens, score, self.out)
            results.append(result)
        return results

    def out_to_terminal(self):
        for result in self.get_results():
            result.out_to_terminal()
