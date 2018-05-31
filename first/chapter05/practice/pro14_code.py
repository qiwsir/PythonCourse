#coding:utf-8
'''
14. 编写函数，判断某字符串中的字母是否含有指定集合中的字母。
'''

def contain_any_1(seq, aset):
    '''
    刚到门口
    '''
    for c in seq:
        if c in aset:
            return True
return False

def contain_any_2(seq, aset):
    '''
    渐入佳境
    '''
    for item in filter(aset.__contains__, seq):
        return True
    return False

def contain_any_3(seq, aset):
    '''
    会当凌绝顶
    '''
    return bool(aset.intersection(seq))

if __name__ == "__main__":
    seq = "apython"
    aset = set(['a', 'b', 'c', 'd', 'e'])
    result = contain_any_2(seq, aset)
    print(result)