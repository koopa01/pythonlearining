# 正则表达式：记录文本规则的代码，是一个特殊的字符序列
# 由普通字符和元字符组成
'''
元字符
. 匹配除换行符以外的任意字符
\w 匹配字母/数字/下划线/汉字
\W 匹配非字母/数字/下划线/汉字(反义字符为大写)
\s 匹配任意空白符
\d 匹配数字
\b 匹配单词的开始或结束
^ 匹配字符串的开始
[^a] 匹配除a以外的任意字符
$ 匹配字符串的结束

限定符
* 重复零次或多次
+ 重复一次或多次
? 重复零次或一次
{n} 重复n次
{n,} 重复n次或更多次数
{n,m} 重复n到m次

re.findout() 匹配所有--常用
re.search() 只匹配第一个
re.match() 只匹配开头的 

组匹配:
re.search(reg,announcement).group(0)
re.match().group()
'''

import re

# 元字符串
reg_string = "koopa2831829@hardcorekoopa123!学英语ihellooawjfwoaiihello "
# 字符串
# reg = "core"
# reg = "\d"
# reg = "^koopa"
# reg = "\w"
# reg = "\s"
# reg = "\W"
# reg = "\w{4}"
reg = "[0-9a-z]{4}"

result = re.findall(reg , reg_string)
print(result)

ip = "this is ip: 192.168.1.1 : 202.201.123.321"
reg = "\d{3}.\d+.\d+.\d+"
ip_result = re.findall(reg,ip)
print(ip_result)

# search只匹配第一个,findall匹配所有
ip_1 = "this is ip: 192.168.1.1 : 202.201.123.321"
reg = "(\d{1,3}.){3}\d{1,3}"
ip_result = re.search(reg ,ip_1)[0]
print(ip_result)

# 组匹配
announcement = "this is a phone number: 13612891236, this is zipcode: 11373"
reg = "this is a phone number: (\d{11}), this is zipcode: (\d{5})"
announcement_result = re.search(reg,announcement).group(0)
print(announcement_result)
announcement_result = re.search(reg,announcement).group(1)
print(announcement_result)
announcement_result = re.search(reg,announcement).group(2)
print(announcement_result)

#re.match()只匹配开头的  
example_string1 = "koopa2831829@hellohardcorekoopa123!学英语ihellooawjfkoopawoaiihello "
reg = "KoOpA"
# string_result = re.match(reg ,example_string1)
string_result = re.match(reg,example_string1,re.I) #re.I作用是忽略大小写
print(string_result)

'''
贪婪: 尽可能多的匹配 (默认)
非贪婪:尽可能少的匹配 (操作符为?)
?操作符用在 * + ? 后面要求正则匹配越少越好
*? 重复零次或多次--重复零次
+? 重复一次或多次--重复一次
?? 重复零次或一次--重复零次
'''

example_string2 = "123koopaaaaa425fiowejfoakoopa^*&koop"
# reg = "koopa*" #贪婪
# reg = "koopa*?" #非贪婪
# reg = "koopa+?"
reg = "koopa??"
string_result = re.findall(reg,example_string2)
print(string_result)

'''
手机号码验证
移动：139,138,137,136,135,134,150,151,
152,157,158,159,182,183,187,188,147
联通：130,131,132,185,186,145
电信：133,153,180,189
'''

def checkphonenumbercarrier():
    # 创建正则表达式对象 使用了前瞻和回顾来保证手机号前后不应该出现数字
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    # pattern = re.compile(r'(?<=\D)(1[38]\d{9}|14[57]\d{8}|15[0-35-9]\d{8}|17[678]\d{8})(?=\D)')
    sentence = '''
    重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    不是15600998765，也是110或119，王大锤的手机号才是15600998765。
    '''
    # 查找所有匹配并保存到一个列表中
    mylist = re.findall(pattern, sentence)
    print(mylist)
    print('--------华丽的分隔线--------')
    # 通过迭代器取出匹配对象并获得匹配的内容
    for temp in pattern.finditer(sentence):
        print(temp.group())
    print('--------华丽的分隔线--------')
    # 通过search函数指定搜索位置找出所有匹配
    m = pattern.search(sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence, m.end())


if __name__ == '__main__':
    checkphonenumbercarrier()




符号              解释                          示例                  说明
.               匹配任意字符                     b.t          可以匹配bat / but / b#t / b1t等
\w              匹配字母/数字/下划线 b\wt                      可以匹配bat / b1t / b_t等,但不能匹配b#t
\s              匹配空白字符（包括\r、\n、\t等）   love\syou     可以匹配love you
\d              匹配数字                        \d\d          可以匹配01 / 23 / 99等
\b              匹配单词的边界 \bThe\b 
^               匹配字符串的开始                 ^The          可以匹配The开头的字符串
$               匹配字符串的结束                 .exe$         可以匹配.exe结尾的字符串
\W              匹配非字母/数字/下划线           b\Wt          可以匹配b#t / b@t等,但不能匹配but / b1t / b_t等
\S              匹配非空白字符                   love\Syou     可以匹配love#you等,但不能匹配love you
\D              匹配非数字                       \d\D         可以匹配9a / 3# / 0F等
\B              匹配非单词边界                   \Bio\B  
[]              匹配来自字符集的任意单一字符      [aeiou]       可以匹配任一元音字母字符
[^]             匹配不在字符集中的任意单一字符    [^aeiou]      可以匹配任一非元音字母字符
*               匹配0次或多次                    \w* 
+               匹配1次或多次                    \w+ 
?               匹配0次或1次                     \w? 
{N}             匹配N次                         \w{3}   
{M,}            匹配至少M次                      \w{3,}  
{M,N}           匹配至少M次至多N次               \w{3,6} 
|               分支                            foo|bar       可以匹配foo或者bar
(?#)            注释      
(exp)           匹配exp并捕获到自动命名的组中        
(? <name>exp)   匹配exp并捕获到名为name的组中      
(?:exp)         匹配exp但是不捕获匹配的文本     
(?=exp)         匹配exp前面的位置                \b\w+(?=ing)    可以匹配I'm dancing中的danc
(?<=exp)        匹配exp后面的位置                (?<=\bdanc)\w+\b    可以匹配I love dancing and reading中的第一个ing
(?!exp)         匹配后面不是exp的位置        
(?<!exp)        匹配前面不是exp的位置        
*?              重复任意次，但尽可能少重复        a.*b  a.*?b    将正则表达式应用于aabab，前者会匹配整个字符串aabab，后者会匹配aab和ab两个字符串
+?              重复1次或多次，但尽可能少重复     
??              重复0次或1次，但尽可能少重复     
{M,N}?          重复M到N次，但尽可能少重复      
{M,}?           重复M次以上，但尽可能少重复      