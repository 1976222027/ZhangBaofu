# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/4/6 17:23
# 文件名称: hw_010_基础.py
# 开发工具: PyCharm
"""
^	匹配字符串的开头
$	匹配字符串的末尾。
.	匹配任意字符，除了换行符
[abc] 表示abc其中一个
aaaaaaaaaaabbbbbbbbbbbbcccccde

[^abc] 表示除了abc之外的字符

正则表达式的作用:查找匹配
所谓正则表达式,就是匹配字符的  依据

[abc]

* 表示0个或多个  一个都匹配不到 也可以
+ 表示1个或多个  必须匹配到一个


{n} 表示n个
{n,}表示n个以上 [n:]
{m,n} 表示m到n个 [m:n]

切片是一样 正则表达式 可以同时有好多个

a| b	匹配a或b  [ab] 本身就是一个正则表大会
    (正则表达式1)|(正则表达式2)
()	匹配括号内的表达式，也表示一个组


10个是最常用 结合使用
最常用 [] |  {} () *  + ?(非)贪婪模式
# 万能表达式

\w	匹配数字字母下划线  abc321_
\W	匹配非数字字母下划线


\s	匹配任意空白字符，等价于 [\t\n\r\f]
\S	匹配任意非空字符


\d	匹配任意数字，等价于 [0-9]
\D	匹配任意非数字

"""
