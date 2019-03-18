#!/usr/bin/env python
# -*- coding: utf-8 -*

import re
path1 = "./a.txt"   #数据来源
path2 = "./cpu.txt"
path3 = "./mem.txt"
f = open(path1)
g = open(path2)
h = open(path3)
line1 = f.readline()
line2 = g.read()
line3 = h.read()
list = []

while line1:
    a = line1.strip('\n')
    findword="\+?(\d|[1-9]\d|100)(\.\d{1})?% "+ a + ".*?: "  #需要查找的特定字符串
    pattern = re.compile(findword)
    result1 = pattern.search(line2)
    result1 = result1.group(0)
    result1 = result1.split( )[0]
    findword="\d+(,\d+)*K: .*?"+ a + "\)"
    pattern = re.compile(findword)
    result2 = pattern.search(line3)
    result2 = result2.group(0)
    a = result2.split(" ")[1]
    result2 = result2.split(":")[0]
    
    list.append([a,result1,result2])
    line1 = f.readline()
f.close
g.close
h.close
with open('002.txt', 'w') as month_file:    #提取后的数据文件
    for tag in list:
        for i in tag:
            month_file.write(str(i))
            month_file.write(' ')
        month_file.write('\n')



