import re
# 匹配字符串中所有匹配到的内容
lst = re.findall(r'\d+', '号码A:10086,号码B:10010')
print(lst)

# 匹配到的内容以迭代器的形式返回
it = re.finditer(r'\d+', '号码A:10086,号码B:10010')
for i in it:
    print(i.group())

# 找到第一个结果就返回，返回的是match的结果
s = re.search(r'\d+', '号码A:10086,号码B:10010')
print(s.group())

# match默认是从头开始匹配，即在正则字符串前面加个 '^'
s = re.match(r'\d+', '1号码A:10086,号码B:10010')
# print(s.group())

# 预编译正则，后期可以直接使用
obj = re.compile(r'\d+')
res = obj.finditer('号码A:10086,号码B:10010')
print(res)
for i in res:
    print(i.group())

html = '''
<div class='jay'><span id='1'>aaa</span></div>
<div class='jre'><span id='2'>bbb</span></div>
<div class='jrg'><span id='3'>ccc</span></div>
<div class='jpg'><span id='4'>ddd</span></div>
<div class='jwq'><span id='5'>eee</span></div>
'''
# 指定特定的组
reg = re.compile(r"<div class='(?P<cId>.*?)'><span id='(?P<sId>.*?)'>(?P<name>.*?)</span></div>", re.S)
result = reg.finditer(html)
for i in result:
    print(i.group('name'))
