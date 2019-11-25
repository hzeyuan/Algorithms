string1  = "BBC ABCDAB ABCDABCDABE"
string2 = "ABCDABD"


def compare(prefix,suffix):
    count = 0
    prefixArr = [prefix[:i+1] for i in range(len(prefix))] # 前缀
    # 添加后缀数组中的元素
    suffixArr = [suffix[i:] for i in range(len(suffix))] # 后缀
    for s in prefixArr:
        if s in suffixArr:
            count  = len(s)
    return count



# 生成匹配表
def partialMatchTable(str):
    table = []
    var = ''
    for s in str:
        var += s
        prefix = var[:-1]  # 前缀
        suffix = var[1:]  # 后缀
        table.append(compare(prefix,suffix))
        #比较前缀和后缀的匹配值个数
    return table

# 在str1字符串中找到str2
def KMP(str1,str2):
    # 先生成《部分匹配表》
    table = partialMatchTable(str2)
    table.insert(0,0) # 我在匹配表里面插入了一个空的匹配值
    index = 0
    while index <len(str1):# 当索引小于字符串长度时
        oldIndex = index # oldIndex 代表,还没比较时，索引的位置
        for i in range(len(str2)):# 遍历要比较的字符串
            if str1[index+i] !=str2[i]:#当两者有字符不同时，跳出循环，并执行以下操作
                index +=i - table[i] # 索引的值 = 当前索引值 + 更改已经匹配的字符串长度 - 匹配表对应匹配值
                if i - table[i]==0: # 这里是为了避免死循环，当上一步操作，索引没有增加时，就让索引+1,让循环能够继续
                    index +=1
                break
        if index == oldIndex: #如果都匹配的话，for循环相当于没有执行，oldIndex会等于index,通过这个条件来判断是否找到匹配的字符串
            return index
    return -1







print(compare('A','B'))
print(compare('AB','BC'))
print(compare('ABCD','BCDA'))
print(partialMatchTable(string2))

print(KMP(string1,string2))