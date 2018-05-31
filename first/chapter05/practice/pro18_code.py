#coding:utf-8
'''
18. 编写函数，实现根据字典的键进行排序的功能，并保持原有的映射关系。
'''

def sort_dict_value(adict):
    keys = adict.keys()
    keys = sorted(keys)
    #return [ adict[k] for k in keys ]
    return map(adict.get, keys)

if __name__ == "__main__":
    d = {"lang":"python", "book":"learn python with laoqi", "publish":"phei"}
    print(d)
    #print(sort_dict_value(d))
    print(list(sort_dict_value(d)))