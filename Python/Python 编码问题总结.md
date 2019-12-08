# Python编码问题总结

当我还是编程小白的时候，编码问题一直困扰了我很久，一碰到编码异常报错，就各种百度谷歌，一个个试别人的方法直到解决问题，Python因为Python2, Python3在编码处理不完全一样，导致在python处理编码问题是更是错误频发，网上的博客又是良莠不齐，费时费力还不一定解决自己的问题，终于我受不了了，花了时间集中学习了python编码的知识，基本囊括了常见的编码问题，并总结如下，希望对你有所帮助。

[TOC]

## 一、字符、编码规范的概念

### 字节

首先我们都知道计算机只能识别0跟1组成的二进制位，任何数据最终都是以二进制的形式存储在计算机中的，1个二进制位表示0和1（1bit），为了方便计算，我们规定1个字节等于8个位，即1byte=8bit。

### 字符&字符集

字符（character）是各种文字和符号的总称，包括各个国家的文字、标点符号、图形符号、数字等。字符集是（character set）是多个字符的集合，字符集有很多种，比如我们常见的ascii、unicode、GBK、GBK2312, BIG5字符集等，不同的字符集包含的字符的种类和个数都不一样。

### 编码规范

上面我们说的ascill、gbk字符集其实是编码规范的一个子概念，为了表示让计算机显示字符，各个国家、国际组织定义了自己的编码规范，将不同的字符映射到不同的二进制数，例如GBK编码规范就定义了中文字符跟二进制数的映射关系，这样采用GBK编码规范，我们的计算机就可以显示中文。

编码规范其实有三个主要的子概念：字符库、编码字符集、字符编码。

* 字符库

  不同的编码规范包含的字符种类数量都不一致，有各自的应用场景，我们把每种编码规范所存储的所有的字符的集合成为字符库。

  例如：在GBK编码规范的字符库中，几乎包含了所有的中文字符，但是其他语音，比如法语，德语并不包含在内，所以用GBK无法显示法语。

* 编码字符集（字符集）

  根据上面我们提到的，字符是无法直接存储在计算机中的，都是以二进制地址的形式存储在计算机中，我们把这些二进制地址的集合称为编码字符集，也就是我们常说的字符集。
  
  例如：在ASCILL编码字符集中，字符a的地址是97，95的二进制地址是0110001, 根据这个地址就可以显示字符a, 编码字符集和字符库是一一对应的。
  
* 字符编码（编码方式）

  当定义了字符库和编码字符集后，我们就可以用二进制地址来显示字符了。

  在Unicode编码规范中，定义了数百万个字符，Unicode使用4个字节来来存储这些字符。但是这样就造成了空间浪费，在存储单字节对的字符，比如字符a（二进制地址00000000 00000000 00000000 0110001），这种其实只需要一个字节就可以。

  为了节省空间，这时候我们需要引入编码方式，一套编码规范可以有多种编码方式，适用于不同的场景。例如：UTF-8 其实就是Unicode的一种主要的编码方式，他采用1-4个不定长字节来表示不同的字符，比如中文字符在UTF-8占用3个字节，ascill字符只需要1个字节。此外，UTF-16，UTF-32也是Unicode的编码方式，具体区别在文章后面列出。

### 常见的编码方式

#### 1. ASCII

ASCII最早的编码规范（American Standard Code for Information Interchange），包含了00000000 ~ 01111111共128个字符，最高位为0，可以表示大小写字母、阿拉伯数字、常用的标点符号和(\r\n\v\f\t)等，ASCII码本身没有特殊的编码方式，直接采用二进制地址来表示。

#### 2. ISO-8859-1

ISO-8859-1收录的字符除ASCII收录的字符外，还包括西欧语言、希腊语、泰语、阿拉伯语、希伯来语对应的文字符号。因为ISO-8859-1编码范围使用了单字节内的所有空间，在支持ISO-8859-1的系统中传输和存储其他任何编码的字节流都不会被抛弃。

#### 3. UTF-8

UTF-8使用1-4个变长字节来表示所有的Unicode字符。

① 对于**单字节**的符号，字节的第一位设为 0，后面的7位为这个符号的 Unicode 码，因此对于英文字母，UTF-8 编码和 ASCII 码是相同的。

② 对于**n字节**的符号 **（n>1）**,第一个字节的前 n 位都设为 1，第 n+1 位设为 0，后面字节的前两位一律设为 10，剩下的没有提及的二进制位，全部为这个符号的 Unicode 码 。

例如：汉字"简"的Unicode编码是'\u7b80'（7b80是十六进制表示）,二进制表示是（01111011 10000000），在UTF-8中编码是'\xe7\xae\x80'，占用3个字节，它的二进制地址是（**1110**0111 **10**101110 **10**000000），可以发现UTF-8表示中文使用3字节，除去规则用的（4 2 2）8个bit，剩下的16个bit拼成2个字节正好跟'简'的Unicode二进制地址一致。

#### 4. UTF-16

UTF-16 使用变长字节来表示所有的Unicode字符。
​① 对于编号在 U+0000 到 U+FFFF 的字符（常用字符集），直接用两个字节表示。
​② 编号在 U+10000 到 U+10FFFF 之间的字符，需要用四个字节表示。
同样，UTF-16 也有字节的顺序问题（大小端），所以就有 UTF-16BE 表示大端，UTF-16LE 表示小端。

#### 5. UTF-32

UTF-32采用4个字节来表示所有的Unicode字符。

直接采用字符的Unicode编号表示字符，不需要编码转换。

#### 6. GBK & GBK2312 & GBK18030

背景：当计算机传播到亚洲，先前定义的ASCII码无法表示汉字，于是产生了诸如大陆的**GB2312**、港台的BIG5、日本的Shift JIS等等。采用双字节表示字符。由于双字节编码可以是变长的，也就是说同一个编码里面有些字符是单字节表示，有些字符是双字节表示。这样做的好处是，一方面可以兼容ASCII，另一方面可以节省存储容量，代价就是会损失一部分码位。

**GBK编码**，是在[GB2312-80](https://baike.baidu.com/item/GB2312-80)标准基础上的[内码](https://baike.baidu.com/item/内码)扩展规范，使用了双[字节](https://baike.baidu.com/item/字节)编码方案，其编码范围从8140至FEFE（剔除xx7F），共23940个码位，共收录了21003个汉字，完全兼容[GB2312-80](https://baike.baidu.com/item/GB2312-80)标准，支持国际标准ISO/IEC10646-1和国家标准GB13000-1中的全部中日韩汉字，并包含了BIG5编码中的所有汉字。GBK编码方案于1995年10月制定， 1995年12月正式发布。

**GB 18030**，全称《信息技术 中文编码字符集》，是[中华人民共和国](https://baike.baidu.com/item/中华人民共和国)[国家标准](https://baike.baidu.com/item/国家标准)所规定的变长多字节字符集。其对GB 2312-1980完全[向后兼容](https://baike.baidu.com/item/向后兼容)，与[GBK](https://baike.baidu.com/item/GBK)基本[向后兼容](https://baike.baidu.com/item/向后兼容)，并支持[Unicode](https://baike.baidu.com/item/Unicode)（GB 13000）的所有码位。GB 18030共收录汉字70,244个。

本身这三者也是3种编码规范，主要的区别就是：

**GB2312**：通常采用EUC储存方法，以便兼容于ASCII。每个汉字及符号以两个字节来表示。

**GBK**：GBK是采用单双字节变长编码，英文使用单字节编码，完全兼容ASCII字符编码，中文部分采用双字节编码。

**GB18030** ：GB18030包含三种长度的编码：单字节的ASCII、双字节的GBK（略带扩展）、以及用于填补所有Unicode码位的四字节UTF区块。

**总结**：由于这三种编码规范只有唯一的编码方式，所以有时候我们又说GBK字符集（CharacterSet=GBK），又有GBK编码（Encoding=GBK）。

​

## 二、Python2跟Python3的编码处理区别

### 文件编码方式

首先，我们要知道，python程序运行时，是解释器将.py文件读取写入内存，写入的时候就需要指定编码方式，在Python2中，默认的编码式Ascii，而在Python3中则是Utf-8, 我们经常在文件第一行或者第二行看到类似#coding:utf-8`或`＃-*-coding:utf-8-*-的定义，其实这就是指定了文件编码方式，当然你也可以指定gbk。使用sys.getdefaultencoding()可以查看默认的编码方式。

```python
Python 3.7.4 (default, Aug 13 2019, 15:17:50)
>>>
>>> import sys
>>> print(sys.getdefaultencoding())
utf-8
>>>

Python 2.7.17 |Anaconda, Inc.| (default, Oct 21 2019, 14:10:59)
>>> import sys
>>> print(sys.getdefaultencoding())
ascii
>>> reload(sys)
<module 'sys' (built-in)>
>>> sys.setdefaultencoding('utf8') # 更改默认的编码
>>> print(sys.getdefaultencoding())
utf8
>>>
```

### Str 、Unicode、Bytes区别

在Python2中有两种字符串类型str和Unicode，其中带前缀u的字符串就是Unicode类型，eg. ***u'简书'***, 不带的就是Str类型，eg. '简书', 需要说明的是Python2中的Str类型也是以bytes字节流形式存储。

![unicode_bytes_convert](/Users/johnson/Pictures/unicode_bytes_convert.jpg)

在Python3中，所有的字符串类型都是Unicode类型，所以从字符串到字节流bytes需要encode，从bytes字节流到字符串需要decode，Bytes不能encode，Unicode不能decode。

## 三、常见的编码错误&解决

```python
1. SyntaxError: Non-ASCII character '\xe4' in file /Users/johnson/Documents/代码学习/test/py2_de_encode.py on line 9, but no encoding declared
answer: py文件没有指定编码方式，代码中出现默认编码方式（ASCII）外的字符

2.UnicodeDecodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)

3.UnicodeDecodeError: 'utf8' codec can't decode byte 0xd6 in position 0: invalid continuation byte

4.UnicodeDecodeError: 'gbk' codec can't decode byte 0x81 in position 8: incomplete multibyte sequence
2、3、4都是使用错误的编码方式，encode和decode的编码方式要一致, 使用指定的编码方式将Unicode编码encode成Bytes，就需要用同样的编码方式decode解码成Unicode,否则就会报错。
  
5.cp936， CP936其实就是GBK，IBM在发明Code Page的时候将GBK放在第936页，所以叫CP936
```

> 参考资料

1. https://realpython.com/python-encodings-guide/
2. https://blog.csdn.net/qq_42068856/article/details/83792174

转载请标明来源

如果文章对你有所把帮助，请帮忙点赞，有任何疑问和建议，可以在下面评论留言。

祝生活愉快！
