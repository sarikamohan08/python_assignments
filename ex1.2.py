
def is_even(a):
    for i in arr:
        if i%2==0:
            arr1.append(i)
    print(arr1)
    
def filters(is_even,arr):
    return is_even(arr)



n=int(input())
arr=list(map(int,input().split()))
arr1=[]
print(arr)
(filters(is_even,arr))

"""
o/p:
5
1 2 3 4 5
[1, 2, 3, 4, 5]
[2, 4]
>>>
"""
