from time import time
from os.path import join

from util import DATA_DIR, summary_results
from query import Answer_query
from Doc import doc

from bottle import route, run, template, static_file, redirect


#for test
# from Doc import doc
# from os.path import join
# def get_docs(num):
#     path = "Data/cnn_samples"
#     docs = []
#     for i in range(num):
#         story = join(path, str(i)+".story")
#         document = doc(story, return_sents_list=True)
#         docs.append(document)
#     return docs
#
@route('/search/<keywords>')
def search(keywords):
    query = Answer_query(keywords)
    keywords_summary = query.summary()

    start = time()
    results = query.search(DATA_DIR, out="html")
    cost_time = format(time() - start, ".4f")

    highlight_count = summary_results(results)
    return template('index.tpl',
            results=results,
            query_string=keywords,
            highlight_count=highlight_count,
            cost_time=cost_time,
            keywords_summary=keywords_summary
            )


@route('/search')
def index():
    return redirect("/search/google")

@route('/news/<news_id>')
def news(news_id):
    doc_path = join(DATA_DIR, news_id+".story")
    document = doc(doc_path)

    return template('article.tpl', document=document)








@route('/<filename:path>')
def send_static(filename):
    return static_file(filename, root='static/')

run(host='localhost', port=8080)
