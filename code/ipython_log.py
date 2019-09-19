# IPython log file

import bokeh
from math import pi

import pandas as pd

from bokeh.io import output_file, show
from bokeh.palettes import Category20c
from bokeh.plotting import figure
from bokeh.transform import cumsum
c = Counter(list(vocab['doc_count']))
from collections import Counter
vocab = pd.read_csv("DATA/not_stop/vocab.csv")
c = Counter(list(vocab['doc_count']))
c
top10 = c.most_common(10)
top10
top_dict = dict(top10)
top_dict
output_file("pie.html")
for key,value in top_dict.items():
    x[str(key)] = value
    
x = {}
for key,value in top_dict.items():
    x[str(key)] = value
    
x
pd.Series(x).reset_index(name='value')
pd.Series(x)
pd.Series(x).reset_index(name='value').rename(columns={'index':'country'})
pd.Series(x)
data = pd.Series(x).reset_index(name='value').rename(columns={'index':'doc_count'})
data['angle'] = data['value']/data['value'].sum() * 2*pi
data['color'] = Category20c[len(x)]
p = figure(plot_height=350, title="Pie Chart", toolbar_location=None,
           tools="hover", tooltips="@doc_count: @value", x_range=(-0.5, 1.0))
           
p.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend='country', source=data)
        
data
p.axis.axis_label=None
p.axis.visible=False
p.grid.grid_line_color = None
show(p)
p
data = pd.Series(x).reset_index(name='value').rename(columns={'index':'country'})
data['angle'] = data['value']/data['value'].sum() * 2*pi
data['color'] = Category20c[len(x)]

p = figure(plot_height=350, title="Pie Chart", toolbar_location=None,
           tools="hover", tooltips="@country: @value", x_range=(-0.5, 1.0))

           
p.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend='doc_count', source=data)
        
p.axis.axis_label=None
p.axis.visible=False
p.grid.grid_line_color = None

show(p)
data
data['country']
x = {}
for key,value in top_dict.items():
    x["出现在"+str(key)+"个文档"] = value
    
    
data = pd.Series(x).reset_index(name='value').rename(columns={'index':'doc_count'})
data['angle'] = data['value']/data['value'].sum() * 2*pi
data['color'] = Category20c[len(x)]
p = figure(plot_height=350, title="Pie Chart", toolbar_location=None,
           tools="hover", tooltips="@country: @value", x_range=(-0.5, 1.0))
           
data
p.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend='doc_count', source=data)
        
p.axis.axis_label=None
p.axis.visible=False
p.grid.grid_line_color = None
show(p)
show(p)
c
top10 = c.most_common(10)
top10
type(c)
len(c)
vocab
vocab.head()
vocab.tail()
top10
top5 = c.most_common(5)
top5
vocab[vocab['doc_count'] > 5].sum()
vocab[vocab['doc_count'] > 5].sum()['doc_count']
vocab[vocab['doc_count'] == 1].sum(axis=1)['doc_count']
vocab[vocab['doc_count'] == 1].sum()['doc_count']
(vocab['doc_count'] > 5).sum()['doc_count']
(vocab['doc_count'] > 5).sum()
top10
x = {}
top_dict = dict(top5)
for key,value in top_dict.items():
    x["出现在"+str(key)+"个文档"] = value
    
    
    
x
x['其他'] = 10350
x
data = pd.Series(x).reset_index(name='value').rename(columns={'index':'doc_count'})
data['angle'] = data['value']/data['value'].sum() * 2*pi
data['color'] = Category20c[len(x)]
p = figure(plot_height=350, title="Pie Chart", toolbar_location=None,
           tools="hover", tooltips="@doc_count: @value", x_range=(-0.5, 1.0))
           
p.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend='doc_count', source=data)
        
p.axis.axis_label=None
p.axis.visible=False
p.grid.grid_line_color = None

show(p)
from bokeh.palettes import Category10_6
Category10_6
data['color'] = Category10_6
p = figure(plot_height=350, title="Pie Chart", toolbar_location=None,
           tools="hover", tooltips="@doc_count: @value", x_range=(-0.5, 1.0))
           
p.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend='doc_count', source=data)
        
p.axis.axis_label=None
p.axis.visible=False
p.grid.grid_line_color = None

show(p)
p = figure(plot_height=350, title="df与单词数量的关系", toolbar_location=None,
           tools="hover", tooltips="@doc_count: @value", x_range=(-0.5, 1.0))
           
           
p.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend='doc_count', source=data)
        
p.axis.axis_label=None
p.axis.visible=False
p.grid.grid_line_color = None

show(p)
data
len(vocab)
10350/len(vocab)
100-21.69
data
data_s = pd.Series(data['value'],index=data['doc_count'])
data_s
data['value']
data_s = pd.Series(data['value'])
data_s
data_s.index = data['doc_count']
data_S
data_s
from bokeh.charts import Donut
from bokeh.charts import Donut, show
vocab.head()
对标点符号进行过滤
def is_word(word):
    for char in word:
        if char not in strings:
            return False
        
import re
word_pa = r'[a-zA-Z0-9]+'
re.match(word_pa, "the")
re.match(word_pa, "the900")
re.match(word_pa, ",")
word_pa = re.compile(r'[a-zA-Z0-9]+')
re.match(word_pa, ",")
re.match(word_pa, "the")
def is_word(word):
    if re.match(word_pa, word):
        return True
    return False
is_word("the")
is_word("the,")
pa2 = r'^[a-zA-Z0-9]+$'
re.match(pa2, "the8,")
re.match(pa2, "the8")
pa2 = re.compile('^[a-zA-Z0-9]+$')
pa2
def is_word(word):
    if re.match(pa2, word):
        return True
    return False
is_word("the")
is_word("the,")
is_word("the8080")
vocab['word'].apply(is_word)
help(vocab['word'].apply)
def is_word(word):
    import pdb;pdb.set_trace()
    if re.match(pa2, word):
        return True
    return False
vocab['word'].apply(is_word)
vocab['word'].apply(is_word)
def is_word(word):
    if re.match(pa2, word):
        return True
    return False
vocab['word'].apply(is_word)
def is_word(word):
    if re.match(pa2, word):
        return word
    return 'NOT_WORD'
vocab['word'].apply(is_word)
pa2
is_word(a)
a = Object()
class A():
    pass
a = A()
is_word(a)
def is_word(word):
    if re.match(pa2, str(word)):
        return word
    return 'NOT_WORD'
vocab['word'].apply(is_word)
new_vocab = vocab
new_vocab['word'] = vocab['word'].apply(is_word)
new_vocab.head()
new_vocab = new_vocab[new_vocab['word'] != "NOT_WORD"]
new_vocab
new_vocab.head()
len(new_vocab)
#绘制zipf定律曲线图
new_vocab.to_csv("DATA/new_vocab.csv")
new_vocab.reindex()
new_vocab.reindex(range(len(new_vocab)))
new_vocab
new_vocab = new_vocab.reindex(range(len(new_vocab)))
new_vocab
new_vocab = pd.read_csv("DATA/new_vocab.csv")
new_vocab
new_vocab.drop(columns=["Unnamed: 0"])
help(new_vocab.drop_duplicates)
new_vocab_unique = new_vocab.drop_duplicates(columns=['doc_count'])
help(new_vocab.drop_duplicates)
new_vocab_unique = new_vocab.drop_duplicates(sub_set = 'doc_count')
help(new_vocab.drop_duplicates)
new_vocab_unique = new_vocab.drop_duplicates(subset = 'doc_count')
new_vocab_unique
len(new_vocab_unique)
new_vocab_unique.drop(columns=['Unnamed: 0'])
new_vocab_unique.index = range(len(new_vocab_unique))
new_vocab_unique
new_vocab_unique = new_vocab_unique.drop(columns=['Unnamed: 0'])
new_vocab_unique
help(new_vocab_unique.sort_values)
new_vocab_unique.sort_values(by=['count'],ascending=True)
new_vocab_unique = new_vocab_unique.sort_values(by=['count'],ascending=True)
new_vocab_unique.head()
new_vocab_unique = new_vocab_unique.sort_values(by=['count'],ascending=False)
new_vocab_unique
new_vocab_unique.head()
C = 80871.0
new_vocab_unique['rank'] = range(len(new_vocab_unique))
new_vocab_unique.head()
new_vocab_unique['rank'] = range(1,len(new_vocab_unique)+1)
new_vocab_unique.head()
new_vocab_unique['n(r)'] = np.log(C) - np.log(new_vocab_unique['rank']) 
import numpy as np
np.lpg
np.log
def cal_nr(r):
    return np.log(C) - np.log(r)
new_vocab_unique['rank'].apply(cal_nr)
new_vocab_unique['logn(r)'] = new_vocab_unique['rank'].apply(cal_nr)
new_vocab_unique.head()
new_vocab_unique['rank'].apply(np.log)
new_vocab_unique['logr'] = new_vocab_unique['rank'].apply(np.log)
new_vocab_unique['log_count'] = new_vocab_unique['count'].apply(np.log)
new_vocab_unique.head()
new_vocab_unique.tail()
new_vocab_unique.to_csv(index=False)
new_vocab_unique.to_csv("DATA/zif.csv",index=False)
new_vocab
new_vocab.drop("Unnamed: 0")
new_vocab
new_vocab.drop('Unnamed: 0')
new_vocab.drop(columns=['Unnamed: 0'])
new_vocab = new_vocab.drop(columns=['Unnamed: 0'])
new_vocab
from util import load_index
index = load_index("DATA/not_stop/index.pkl")
index.head()
index.sum()
tfs = index.sum(axis=1)
tfs
new_vocab.head()
tfs.values
len(tfs.values)
t = tfs.reindex(new_vocab.index)
t.head()
tfs.head()
t = tfs.reindex(new_vocab['word'])
t.head()
len(t)
len(new_vocab)
t.tail()
new_vocab['word'].head()
new_vocab['word'].tail()
new_vocab['tf_i'] = t.values
new_vocab.head()
new_vocab.tail()
def mscatter(p, x, y, marker):
    p.scatter(x, y, marker=marker, size=5,
              line_color="navy", fill_color="orange", alpha=0.5)
              
p = figure(title = "TF与IDF的关系分布")
mscatter(p,x=range(len(new_vocab)),new_vocab['idf'])
mscatter(p,range(len(new_vocab)),new_vocab['idf'], 'x')
show(p)
help(new_vocab.drop_duplicates)
idf_tf_plot_data = new_vocab.drop_duplicates(subset="idf")
len(idf_tf_plot_data)
def mscatter(p, x, y, marker):
    p.scatter(x, y, marker=marker, size=9,
              line_color="navy", fill_color="orange", alpha=0.5)
              
              
mscatter(p,range(len(idf_tf_plot_data)),idf_tf_plot_data['idf'], 'x')
show(p)
p = figure(title = "TF与IDF的关系分布")
mscatter(p,range(len(idf_tf_plot_data)),idf_tf_plot_data['idf'], 'x')
show(p)
mscatter(p,range(len(idf_tf_plot_data)),idf_tf_plot_data['tf_i'], 'cross / +')
show(p)
p = figure(title = "TF与IDF的关系分布")
mscatter(p,range(len(idf_tf_plot_data)),idf_tf_plot_data['idf'], 'x')
mscatter(p,range(len(idf_tf_plot_data)),idf_tf_plot_data['tf_i'], 'cross')
show(p)
help(new_vocab.plot)
idf_tf_plot_data
idf_tf_plot_data.to_csv(columns=['idf','tf_i'],index=False)
idf_tf_plot_data.to_csv("DATA/idf_tf_plot_data.csv",columns=['idf','tf_i'],index=False)
get_ipython().system('pwd')
get_ipython().system('vim DATA/idf_tf_plot_data.csv')
idf_tf_plot_data
idf_tf_plot_data['tf_i'] / idf_tf_plot_data['idf']
idf_tf_plot_data['tf_i_'] = idf_tf_plot_data['tf_i'] / idf_tf_plot_data['idf']
idf_tf_plot_data.head()
0.394552 / 0.001501
plt
idf_tf_plot_data.plot(y=['tf_i_','idf'], style=['x','+'])
idf_tf_plot_data.head()
idf_tf_plot_data['tf_i_'] = np.log(idf_tf_plot_data['tf_i_'])
idf_tf_plot_data.head()
idf_tf_plot_data['IDF'] = idf_tf_plot_data['idf']
idf_tf_plot_data['TF'] = idf_tf_plot_data['tf_i_']
idf_tf_plot_data['TF x IDF'] = idf_tf_plot_data['tf_i_'] * idf_tf_plot_data['idf']
idf_tf_plot_data.head()
idf_tf_plot_data.to_csv("DATA/idf_tf_plot_data.csv", index=False, columns=['TF','IDF','TF-IDF'])
get_ipython().system('vim DATA/idf_tf_plot_data.csv')
idf_tf_plot_data
len(idf_tf_plot_data)
new_vocab.head()
len(new_vocab.head())
len(new_vocab)
len(vocab)
vocab.head()
index
len(vocab)
vocab.index == index.index
vocab.head()
index.head()
vocab.drop('word')
vocab = vocab.drop(columns=['word'])
vocab.index = index.index
vocab.head()
vocab.tail()
index.tail()
index.sum(axis=1)
vocab.columns
vocab['TF-idf'] = index.sum(axis=1)
vacab.head()
vocab.head()
len(vocab)
TFs = index.sum(axis=1)
TFs.max()
TFs.min()
TFs.plot()
TFs
zuida = TFs.max()
zuixiao = TFs.min()
zuixiao
zuida 
def y(data, x):
    return (data > x).sum()
(TFs > 13).sum()
(TFs > 5).sum()
len(TFs)
(TFs > 1).sum()
list((TFs > 1).index)
y(TFs, 0.5)
x = np.linspace(0, TFs.max(), 10000)
def y(x):
    return (TFs > x).sum()
plt
from matplotlib.pyplot as plt
import  matplotlib.pyplot as plt
plt.plot(x,np.array(list(map(y,x))))
plt.xlabel("TF-idf")
plt.ylabel('VOCAB SIZE')
plt.show()
plt.clf()
plt.show()
plt.plot(x,np.array(list(map(y,x))))
plt.xlabel("TF-idf")
爬楼梯、
plt.show()
plt.show()
plt.plot(x,np.array(list(map(y,x))))
vocab_size = np.array(list(map(y,x)))
plt.xlabel("TF-idf")
plt.ylabel("word_size")
plt.show()
y
x = np.linspace(0, 5.0, 10000)
plt.clf()
plt.plot(x,np.array(list(map(y,x))))
plt.xlabel("TF-idf")
plt.ylabel("word_size")
plt.show()
def y(x):
    return np.log((TFs > x).sum())
plt.clf()
plt.xlabel("TF-idf")
plt.ylabel("log(word_size)")
plt.show()
plt.plot(x,np.array(list(map(y,x))))
plt.show()
plt.xlabel("TF-idf")
plt.ylabel("log(word_size)")
plt.show()
plt.xlabel("TF-idf")
plt.ylabel("log(word_size)")
plt.plot(x,np.array(list(map(y,x))))
plt.show()
get_ipython().run_line_magic('logstart', '')
get_ipython().system('vim ipython_log.py')
get_ipython().run_line_magic('pinfo', '%logstart')
get_ipython().system('vim ipython_log.py')
quit()
