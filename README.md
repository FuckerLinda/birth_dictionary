## need你需要：

​	python3



## model用到的模块：

​	import sys
​	import getopt



# Help帮助：

1. use "-h" for help
2. use "-m x" to set mode, and it should follow with yyyymmdd yyyymmdd

"x" is a number you input.

"yyyymmdd":the first is Start Date and the second is End Date

x=1, output YYYYMMDD

x=2, output YYYY-MM-DD

x=3, output YYYY/MM/DD

x=4, output YYYY-M-D

x=5, output YYYY/M/D

for example, use `python3 birth.py -m2 20000102 20200102` and it output a dictionary named "birth.txt". It ranges from 2000-01-02 to 2020-01-02

------

birth.py文件可以生成一个生日字典。5个模式可以生成不同风格的字典。

usage：python3 birth.py -m <mode\> <start-date\><end-date\>

用法：python3 birth.py -m [模式] [起始日期] [结束日期]

***It also applies to leap years**

***遇到闰年也适用**