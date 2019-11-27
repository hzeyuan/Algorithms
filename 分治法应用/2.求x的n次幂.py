# 求x的n次幂,非递归
def power(x,n):
    base = 1
    while n !=1:
        if n %2!=0:
            base *= x
        x *= x
        n//=2
    return base*x

# 递归
def power1(x,n,result=1):
    if n==1:
        return x*result
    if n%2 !=0:
        result *= x
    return power1(x*x,n//2,result)
print(power(3,5))
print(power1(3,5))
print(pow(3,5))