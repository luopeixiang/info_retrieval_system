from time import time
import sys

from query import Answer_query
from util import INDEX_FILE,DATA_DIR
from util import load_index



def main():
    args = sys.argv
    query = Answer_query(" ".join(args[1:]))

    start = time()
    query.search(DATA_DIR)
    print("共花费 {}秒！".format(time()-start))


if __name__ == "__main__":
    main()
