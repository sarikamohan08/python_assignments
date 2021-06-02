#1.
l=[]
n=int(input())
arr=list(map(str,input().split()))
for i in range(n):
    for j in range(1,6):
        res=(arr[i]*j)
        l.append(res)

print(l)
"""
o/p:
3
x y z
['x', 'xx', 'xxx', 'xxxx', 'xxxxx', 'y', 'yy', 'yyy', 'yyyy', 'yyyyy', 'z', 'zz', 'zzz', 'zzzz', 'zzzzz']
>>>
"""

#2.
l=[]
n=int(input())
arr=list(map(str,input().split()))
for i in range(1,5):
    for j in range(n):
        res=(arr[j]*i)
        l.append(res)

print(l)
"""
o/p:
3
x y z
['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']
"""

#3
n=int(input())
arr=list(map(int,input().split()))
result = [ [i+j] for i in arr for j in range(0,n)]
print(str(result))
"""
o/p:
3
2 3 4
[[2], [3], [4], [3], [4], [5], [4], [5], [6]]
>>>
"""

#4
n=int(input())
arr=list(map(int,input().split()))
result = [[i+j for i in arr] for j in range(n)]
print(str(result))
"""
o/p:
4
2 3 4 5
[[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
>>> 
"""
#5
n=int(input())
arr=list(map(int,input().split()))
result = [(i,j) for i in arr for j in arr]
print(str(result))
"""
o/p:
3
1 2 3
[(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
>>>
"""
