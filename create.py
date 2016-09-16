# -*-coding:utf-8 -*-
from __future__ import with_statement
import ConfigParser

class Item:
     def __init__(self, key, value):
         self.key=key
         self.value=value

if __name__ == '__main__':
    print('input the \'Practise Name\'');
    name=raw_input();

    contentMap={};
    sessionName="";

    while name:
        if sessionName =="":
            sesstionList=[];
            print name,'子分类是'
            sessionName=raw_input();

        print('情景是:')
        title=raw_input();
        print('答案是:');
        answer=raw_input();
        print('保存s不保存n仅退出当前分类b退出并保存一切q')
        mode=raw_input();
        if mode=="s":
            sesstionList.append(Item(title,answer))
        if mode=="b":
            sesstionList.append(Item(title,answer))
            contentMap.setdefault(sessionName,sesstionList)
            sesstionList=[]
            sessionName=""

        elif mode=="q":
            sesstionList.append(Item(title,answer))
            contentMap.setdefault(sessionName,sesstionList)
            break;
        else:
            continue
    config=ConfigParser.ConfigParser()
    cfgfile=open(name,'w')
    for key in contentMap:
        config.add_section(key)
        for valueItem in contentMap[key]:
            config.set(key,valueItem.key,valueItem.value)
    config.write(cfgfile)
    print('save success')









