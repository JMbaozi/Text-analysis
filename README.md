**本项目用于文本分析的基础学习，为后续项目的辅助项目。**
**如果你对此感兴趣，可以Star，一起来学习并维护。也可以通过以下方式联系我。**


### 1.联系方式

* QQ: 2316705476

* E-mail: baozicrd@foxmail.com

* WECHAT: JMbaozi

* WEIBO: @追风若航

### 2.内容来源

文章大部分内容来源于：

#### 1.1 图书

* [《文本分析与文本挖掘》——姜维](https://book.douban.com/subject/30433554/) 

* [《在线文本数据挖掘：算法原理与编程实现》——刘通 ](http://product.dangdang.com/27916151.html) 
  
  > 图书可以到图书馆借阅，除这两本外，其它更优质的书亦可。

#### 1.2 文章

* [《基于在线交通数据的中国城市交通经济协调》](https://mp.weixin.qq.com/s?__biz=MzA3OTU3ODgxNA==&amp;mid=2650589295&amp;idx=1&amp;sn=f167bfd7ef46dbf690aeb46e13c0a9a8&amp;chksm=87b93bbeb0ceb2a88a7cfa2a772996c34ae9adfc2bf367cbba4396cb0b3de08164f7dd039936&amp;scene=0&amp;xtrack=1&amp;key=0d2d4c6f8e7ea878f5c770815601e4b3b18ab0da7ebd6a8a75ca94e4195b77fb77f8e2741a04b28ab450b28bf86f952ad7fd095f5631ce90cb268ccc68cdfa95086be085dce0d37e1a6fb0463584199b&amp;ascene=14&amp;uin=MTkwOTkyODYzMg%3D%3D&amp;devicetype=Windows+7&amp;version=62060841&amp;lang=zh_CN&amp;pass_ticket=9rd6B4KoX9uTF0tGKVZaA7cSQQLbatl7z398QmutuMyh96FrkPrDbDyEqh8toLcw "")

* [《如何从冰雪奇缘入门网络分析？》](https://mp.weixin.qq.com/s?__biz=MzIzMjQyNzQ5MA==&amp;mid=2247499076&amp;idx=1&amp;sn=6089d100c9d20c0421ad986ebe1c53a3&amp;chksm=e897a7c9dfe02edfde8c284d1743e04e0624d70fd23b4754689074f7379563d8c0cfd3534404&amp;scene=0&amp;xtrack=1&amp;key=0d2d4c6f8e7ea87865be2c8503e3e07dda9540387b285b6f63a29e08bac95f1d2b5b509da5d10b56b8e952ceae3205b1a28b1e14b9126f1014a35a13c15689d640ffa30f62a791ee794fd8c2a46b21a9&amp;ascene=14&amp;uin=MTkwOTkyODYzMg%3D%3D&amp;devicetype=Windows+7&amp;version=62060841&amp;lang=zh_CN&amp;pass_ticket=PMh1%2B%2BjLSmZgnWTCI0uQC7aoLG4YIwnaZtQ35Bq8XBuH%2FoZ1ZXmjkgN7OEg%2BVgOM	"")


#### 1.3 网络

* [用Python分析红楼梦](https://zhuanlan.zhihu.com/p/29209681)

### 3.备注

* [文本分析术语.docx](https://github.com/JMbaozi/Text-analysis/blob/master/%E6%96%87%E6%9C%AC%E5%88%86%E6%9E%90%E6%9C%AF%E8%AF%AD.docx) ：用于下载文本分析术语的文档，提供原文件，以便添加和修改。 

* [文本分析.docx](https://github.com/JMbaozi/Text-analysis/blob/master/%E6%96%87%E6%9C%AC%E5%88%86%E6%9E%90.docx) ：用于下载文本分析（总文章）的文档，提供原文件，以便添加和修改。
  
  > 建议下载该文档进行修改，网页版排版有误。 

* [文本分析的主要技术（文件夹）](https://github.com/JMbaozi/Text-analysis/tree/master/%E6%96%87%E6%9C%AC%E5%88%86%E6%9E%90%E7%9A%84%E4%B8%BB%E8%A6%81%E6%8A%80%E6%9C%AF)：用于下载对应的文档。
  
   > 建议下载该文档进行修改，网页版排版有误。 

-------
## 以《红楼梦》为例的简单应用

### 数据来源
* 由红楼梦研究所校注、人民文学出版社出版的《红楼梦》以庚辰（1760）本《脂砚斋重评石头记》为底本，以甲戌（1754）本、已卯（1759）本、蒙古王府本、戚蓼生序本、舒元炜序本、郑振铎藏本、红楼梦稿本、列宁格勒藏本（俄藏本）、程甲本、程乙本等众多版本为参校本。[下载链接](https://github.com/JMbaozi/Text-analysis/blob/master/%E7%BA%A2%E6%A5%BC%E6%A2%A6%E5%BA%9A%E8%BE%B0%E6%9C%AC%EF%BC%88%E4%BA%BA%E6%B0%91%E6%96%87%E5%AD%A6%E5%87%BA%E7%89%88%E7%A4%BE%EF%BC%89.docx)
* 网络下载的《红楼梦.txt》[下载链接](https://github.com/JMbaozi/Text-analysis/blob/master/hongloumeng.txt)

### 分析工具
* Python3.6.6
  * [官方网址](https://www.python.org/) 
* jieba中文分词模块
  * [模块网址](https://github.com/JMbaozi/jieba)
  * [帮助文档](https://github.com/fxsjy/jieba/blob/master/README.md)
### 部分应用
#### 1.分词
* 代码
```python
# encoding=utf-8
import jieba

seg_list = jieba.cut("_text", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  # 精确模式
```
* 实例

  * “也想要到人间去享一享这荣华富贵。”经过分词后变为“也/想要/到/人间/去/享一享/这/ 荣华富贵。”；
  * “将一块大石登时变成一块鲜明莹洁的美玉”经过分词后变为“将/一块/大石/登时/变成/一块/鲜明/莹洁/的/美玉”；
  * “然后好携你到那昌明隆盛之邦、诗礼簪缨之族、花柳繁华地、温柔富贵乡去安身乐业。”经过分词后变为“然后/好/携/你/到/那/昌明/隆盛/之邦/ 、/诗礼/簪缨/之族/ 、/花柳/繁华/地/ 、/温柔/富贵/乡去/安身乐业/。”；
  * “原来女娲氏炼石补天之时，于大荒山无稽崖炼成高经十二丈、方经二十四丈顽石三万六千五百零一块。”经过分词后变为“原来/女娲/氏/炼石补天/之/时/，/于/大/荒山/无稽/崖/炼成/高经/十二/丈/、/方经/二十四丈/顽石/三万/六千五百/零/一块/。”。

#### 2.词性标注
* [词性列表](https://github.com/JMbaozi/Text-analysis/blob/master/%E8%AF%8D%E6%80%A7%E5%88%97%E8%A1%A8.txt)
* 代码
```python
import jieba.posseg as pseg
words = pseg.cut("_text")
for word, flag in words:
    print('%s %s' % (word, flag))
```
* 实例
  * “你看看这玉上穿的穗子”：
你r看看v这r玉n上f穿v的uj穗子n
  * “那贾母见他两个都生了气，只说趁今儿那边看戏，他两个见了也就完了，不想又都不去。”：
那 r 贾母nr 见v他r两个m都d生v了ul气n ，x只说c趁p今儿t那边r看v戏n，x他r两个m见v了ul也d就d完v了ul，x不想v又d都d不d去v 。x
  * “一时宝钗、凤姐儿去了，黛玉笑向宝玉道："你也试着比我利害的人了。谁都像我心拙口笨的，由着人说呢！"宝玉正因宝钗多了心，自己没趣，又见黛玉来问着他，越发没好气起来。待要说两句，又恐黛玉多心，说不得忍着气，无精打彩一直出来了。”：
一m时宝钗nr、x凤姐儿nr去v了ul，x黛玉笑nr向宝玉nr道 q：x"x你r也d试v着uz比p我r利害v的uj人n了ul。x谁r都d像v我心n拙ag口q笨a的uj，x由着c人n说v呢y！x"x宝玉nr正d因p宝钗nr多m了ul心s，x自己r没趣v，x又d见v黛玉nr来v问v着uz他r，x越发d没好气l起来v。x待v要说c两句m，x又d恐d黛玉nr多心n，x说不得l忍v着uz气n，x无精打彩i一直d出来v了ul。x

#### 3.基于TF-IDF算法的关键词提取
* 语句关键词提取
  * 代码
    ```python
    #jieba.analyse.extract_tags(string,topK=20,withWeight=True,allowPOS=(" "))
    #string：待处理语句
    #topK：返回TF、IDF权重最大的关键字的个数，默认20
    #withWeight：是否返回权重值，默认false
    #allowPOS：是否仅返回指定类型，默认为空
    import jieba.analyse
    # 字符串前面加u表示使用unicode编码
    content = u'_text'
    keywords = jieba.analyse.extract_tags(content, topK=20,withWeight=True, allowPOS=())
    # 访问提取结果
    for item in keywords:
        print(item[0], item[1])
    ```
  * 实例
    > “原来贾珍近因居丧,每不得游顽旷荡,又不得观优闻乐作遣.无聊之极,便生了个破闷之法. 日间以习射为由,请了各世家弟兄及诸富贵亲友来较射.因说:"白白的只管乱射,终无裨益,不但不能长进,而且坏了式样,必须立个罚约,赌个利物,大家才有勉力之心."因此在天香楼下箭道内立了鹄子,皆约定每日早饭后来射鹄子.贾珍不肯出名, 便命贾蓉作局家.这些来的皆系世袭公子,人人家道丰富,且都在少年,正是斗鸡走狗,问柳评花的一干游荡纨裤.因此大家议定,每日轮流作晚饭之主,----每日来射, 不便独扰贾蓉一人之意.于是天天宰猪割羊,屠鹅戮鸭,好似临潼斗宝一般,都要卖弄自己家的好厨役好烹炮.不到半月工夫,贾赦贾政听见这般,不知就里,反说这才是正理, 文既误矣,武事当亦该习,况在武荫之属.两处遂也命贾环,贾琮,宝玉,贾兰四人于饭后过来,跟着贾珍习射一回,方许回去.”

    > 关键词：由于文字较少，所以按权值占比选前五个
    贾珍 0.2248850718385
    每日 0.15875041022175002
    问柳评花 0.11583898043333334
    临潼斗宝 0.11583898043333334
    纨裤 0.10428652742416666

* 文本关键词提取
  * 代码
    ```python
    from jieba.analyse import *
    with open('_text.txt',encoding = 'utf-8') as f:
        data = f.read()
    for keyword, weight in extract_tags(data, topK=10, withWeight=True):
        print('%s %s' % (keyword, weight))
    ```
  * 实例
    > 以 hongloumeng.txt为例
    
    > 关键词：取权值占比前十个
    宝玉 0.11174015386450631
    贾母 0.04096279485052852
    凤姐 0.03679341393983838
    王夫人 0.03238483108809296
    老太太 0.029228577284745143
    奶奶 0.025319232252404632
    那里 0.024846723669342888
    什么 0.024490410824605114
    贾琏 0.02434048230267443
    太太 0.024266427970154856

#### other function
> Waiting to be added
------------
## 正式项目
* 时间：12月13日左右
* 项目：暂定《红楼梦》分析
* 说明：此项目仅作为正式项目的辅助项目，并不能依靠该项目完成整个工作。






