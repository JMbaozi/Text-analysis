"""
# encoding=utf-8
import jieba
seg_list = jieba.cut("三万六千五百零一块", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

"""
"""
# encoding=utf-8
import jieba

jieba.load_userdict("hlmdict.txt")
jieba.add_word('大荒山',freq = None,tag = None)
jieba.add_word('女娲氏',freq = None,tag = None)
jieba.add_word('无稽崖',freq = None,tag = None)
jieba.add_word('高经十二丈',freq = None,tag = None)
jieba.add_word('方经二十四丈',freq = None,tag = None)
seg_list = jieba.cut("原来女娲氏炼石补天之时，于大荒山无稽崖炼成高经十二丈、方经二十四丈顽石三万六千五百零一块。", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

"""


"""
import jieba

data = "原来女娲氏炼石补天之时，于大荒山无稽崖炼成高经十二丈、方经二十四丈顽石三万六千五百零一块。"

cut_result = jieba.cut(data)
print('==' * 20)
print('/'.join(cut_result))

jieba.load_userdict('hlmdicttest.txt')
cut_result = jieba.cut(data)
print('=='*20)
print('/'.join(cut_result))

"""

"""
import sys
sys.path.append('../')

import jieba
import jieba.analyse
from optparse import OptionParser

USAGE = "usage:    python -extract_tags.py [file name] -k [top k]"

parser = OptionParser(USAGE)
parser.add_option("-k", dest="topK")
opt, args = parser.parse_args()


if len(args) < 1:
    print(USAGE)
    sys.exit(1)

file_name = args[0]

if opt.topK is None:
    topK = 10
else:
    topK = int(opt.topK)

content = open('_test.txt', 'rb').read()

tags = jieba.analyse.extract_tags(content, topK=topK)

print(",".join(tags))

"""

"""
import jieba
import jieba.analyse
import math
keywords1=jieba.analyse.extract_tags("当日地陷东南，这东南一隅有处曰姑苏，有城曰阊门者，最是红尘中一二等富贵风流之地。这阊门外有个十里街，街内有个仁清巷，巷内有个古庙，因地方窄狭，人皆呼作葫芦庙。庙旁住着一家乡宦，姓甄名费，字士隐。嫡妻封氏，情性贤淑，深明礼义。家中虽不甚富贵，然本地便也推他为望族了。只因这甄士隐禀性恬淡，不以功名为念，每日只以观花修竹、酌酒吟诗为乐，倒是神仙一流人品。只是一件不足：如今年已半百，膝下无儿，只有一女，乳名英莲，年方三岁。")
print('关键词提取'+"/".join(keywords1))
keywords_top=jieba.analyse.extract_tags("当日地陷东南，这东南一隅有处曰姑苏，有城曰阊门者，最是红尘中一二等富贵风流之地。这阊门外有个十里街，街内有个仁清巷，巷内有个古庙，因地方窄狭，人皆呼作葫芦庙。庙旁住着一家乡宦，姓甄名费，字士隐。嫡妻封氏，情性贤淑，深明礼义。家中虽不甚富贵，然本地便也推他为望族了。只因这甄士隐禀性恬淡，不以功名为念，每日只以观花修竹、酌酒吟诗为乐，倒是神仙一流人品。只是一件不足：如今年已半百，膝下无儿，只有一女，乳名英莲，年方三岁。",topK=3)
print('关键词topk'+"/".join(keywords_to#有时不确定提取多少关键词，可利用总词的百分比
print('总词数{}'.format(len(list(jieba.cut("当日地陷东南，这东南一隅有处曰姑苏，有城曰阊门者，最是红尘中一二等富贵风流之地。这阊门外有个十里街，街内有个仁清巷，巷内有个古庙，因地方窄狭，人皆呼作葫芦庙。庙旁住着一家乡宦，姓甄名费，字士隐。嫡妻封氏，情性贤淑，深明礼义。家中虽不甚富贵，然本地便也推他为望族了。只因这甄士隐禀性恬淡，不以功名为念，每日只以观花修竹、酌酒吟诗为乐，倒是神仙一流人品。只是一件不足：如今年已半百，膝下无儿，只有一女，乳名英莲，年方三岁。")))))
total=len(list(jieba.cut("当日地陷东南，这东南一隅有处曰姑苏，有城曰阊门者，最是红尘中一二等富贵风流之地。这阊门外有个十里街，街内有个仁清巷，巷内有个古庙，因地方窄狭，人皆呼作葫芦庙。庙旁住着一家乡宦，姓甄名费，字士隐。嫡妻封氏，情性贤淑，深明礼义。家中虽不甚富贵，然本地便也推他为望族了。只因这甄士隐禀性恬淡，不以功名为念，每日只以观花修竹、酌酒吟诗为乐，倒是神仙一流人品。只是一件不足：如今年已半百，膝下无儿，只有一女，乳名英莲，年方三岁。")))
get_cnt=math.ceil(total*0.1)  #向上取整
print('从%d 中取出%d 个词'% (total,get_cnt))
keywords_top1=jieba.analyse.extract_tags("当日地陷东南，这东南一隅有处曰姑苏，有城曰阊门者，最是红尘中一二等富贵风流之地。这阊门外有个十里街，街内有个仁清巷，巷内有个古庙，因地方窄狭，人皆呼作葫芦庙。庙旁住着一家乡宦，姓甄名费，字士隐。嫡妻封氏，情性贤淑，深明礼义。家中虽不甚富贵，然本地便也推他为望族了。只因这甄士隐禀性恬淡，不以功名为念，每日只以观花修竹、酌酒吟诗为乐，倒是神仙一流人品。只是一件不足：如今年已半百，膝下无儿，只有一女，乳名英莲，年方三岁。",topK=get_cnt)
print('关键词topk'+"/".join(keywords_top1))''

"""


"""
import jieba.posseg as pseg
import jieba

#jieba.load_userdict("hlmdict.txt")
words = pseg.cut("当日地陷东南，这东南一隅有处曰姑苏，有城曰阊门者，最是红尘中一二等富贵风流之地。")
for word, flag in words:
    print('%s %s' % (word, flag))

"""




"""
import sys
sys.path.append('../')

import jieba
import jieba.analyse
from optparse import OptionParser

USAGE = "python extract_tags_with_weight.py E:\文本分析学习\_test.txt -k [top k] -w [with weight=1 or 0]"

parser = OptionParser(USAGE)
parser.add_option("-k", dest="topK")
opt, args = parser.parse_args()


if len(args) < 1:
    print(USAGE)
    sys.exit(1)

file_name = args[0]

if opt.topK is None:
    topK = 10
else:
    topK = int(opt.topK)

content = open(file_name, 'rb').read()

tags = jieba.analyse.extract_tags(content, topK=topK)

print(",".join(tags))
"""


"""
#jieba.analyse.extract_tags(string,topK=20,withWeight=True,allowPOS=(" "))
#string：待处理语句
#topK：返回TF、IDF权重最大的关键字的个数，默认20
#withWeight：是否返回权重值，默认false
#allowPOS：是否仅返回指定类型，默认为空
import jieba.analyse
# 字符串前面加u表示使用unicode编码
content = u'_text'
keywords = jieba.analyse.extract_tags(content, topK=20, withWeight=True, allowPOS=())
# 访问提取结果
for item in keywords:
    print(item[0], item[1])

"""


"""
from jieba.analyse import *
with open('liulaolao.txt',encoding = 'utf-8') as f:
    data = f.read()
for keyword, weight in extract_tags(data, topK=10, withWeight=True):
    print('%s %s' % (keyword, weight))
"""


"""
from jieba.analyse import *
import jieba
stopwords = ['奶奶','那里','什么','姑娘','说道','众人','如今','一面','你们','袭人','只见']
with open('hongloumeng.txt',encoding = 'utf-8') as f:
    data = f.read()
for keyword, weight in extract_tags(data, topK=21, withWeight=True):
    tag = 1
    for i in range(11):
        if keyword == stopwords[i]:
            tag = 0
    if tag == 1: 
        print('%s %s' % (keyword,weight))

"""



#刘姥姥进大观园

from jieba.analyse import *
import jieba
stopwords = ['奶奶','婆子','一个','姑娘','说道','众人','如今','一面','你们','丫鬟','只见']
with open('liulaolao.txt',encoding = 'utf-8') as f:
    data = f.read()
for keyword, weight in extract_tags(data, topK=10, withWeight=True):
    tag = 1
    for i in range(11):
        if keyword == stopwords[i]:
            tag = 0
    if tag == 1: 
        print('%s %s' % (keyword,weight))

