import os


class doc(object):
    """表示单个文档"""

    def __init__(self, doc_path, return_sents_list=False):
        self.doc_path = doc_path
        self.id_, _ = os.path.splitext(os.path.basename(doc_path))
        self.return_sents_list = return_sents_list

        with open(doc_path) as f:
            self._process_lines(f.readlines())

    def _process_lines(self, lines):
        highlight_count = 0
        sents = []
        for line in lines:
            if line.startswith("@highlight"):
                highlight_count += 1
            elif line == "\n":
                continue
            else:
                sents.append(line.strip('\n').lower())
        if not self.return_sents_list:
            self.article = " ".join(sents[:-highlight_count])
            self.abstract = " ".join(sents[-highlight_count:])
        else:
            self.article = sents[:-highlight_count]
            self.abstract = sents[-highlight_count:]


    def out(self, tf_score):
        """打印出摘要 以及id"""
        print("ID: ", self.id_)
        print("SCORE: ", tf_score)
        print("*"*25 + '\n' + self.abstract + '\n' + "*"*25)
        print('\n\n')
