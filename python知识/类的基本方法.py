class animal:
    def __init__(self,name):# 初始化对象
        self.name = name
        self.weight = 0
    def __del__(self):# 对象被删除之前调用
        print("删除对象",self.name)

    def __str__(self):

        return "打印{}".format(self.name)
    def __len__(self): # 使用len()方法时调用
        print("使用len()方法")
        return len(self.name)
    def __lt__(self, other): # 判断self对象是否小于other对象
        if len(self.name)<len(other.name):
            return True
        elif len(self.name)>len(other.name):
            return False
    def __eq__(self, other): # 判断self对象是否等于other对象
        if len(self.name)==len(other.name):
            return True
        else:
            return  False
    def __gt__(self, other):# 判断self对象是否大于other对象
        return  not self.__lt__(other)
    def __ge__(self, other): # 判断self对象是否大于等于other对象
        return self.__gt__(other) or self.__eq__(other)
    def __le__(self, other): # 判断self对象是否小于等于other对象
        return self.__lt__(other) or self.__eq__(other)
    def __getitem__(self, item):# 当获取这个对象索引的值时，调用这个方法
        pass
    def __setitem__(self, key, value): #当设置对象的键值对，调用这个方法
        pass
    def __getattribute__(self, item):
        print("调用__getattribute__方法")
        try:
            return object.__getattribute__(self,item)
        except KeyError:
            print("错误，调用__getattr__方法")
            return 'default'
    def __getattr__(self, item):
        print("没有{}属性,调用了getattr方法".format(item))

    def __setattr__(self, key, value):
        print("添加或者修改属性时，触发__setattr__")
        self.__dict__[key] =value
    def __delattr__(self, item):
        print("删除属性{}".format(item))
        self.__dict__.pop(item)
    def __iter__(self): # 让对象可以循环
        return iter([self.name])
    def __call__(self, *args, **kwargs):
        self.name = args[0]

a = animal("dog")

b =animal("tiger")
len(a)
print(a<b)
print(a>b)
print(a>=b)
print(a<=b)
print(a==b)
print(sorted([a,b])[0].name) # 实现了__lt__ ,__gt__ ,__le__,__ge__可以实现排序
a.key = 'value' # 设置新的属性
del a.key # 删除属性key
# 删除属性
print(a.key) #没有key属性,调用了getattr方法

a[1:1] = [1,2,3,4,5]

for n in a:
    print("循环",n) # 循环 dog

a('dogggg') # 触发 __call__()
print(a.name) #a.name = dogggg
print(a.__module__) # 当前操作对象所在的模块
print(a.__class__) # 当前操作对象是什么类
print(a.__dict__) # 对象中的属性
