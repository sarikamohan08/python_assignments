def func_map(arr):
    l=[]
    for i in arr:
        l.append(len(i))
    return l
        
    

def main():
    t=int(input("enter no.of words in list:"))
    arr=list(map(str,input().split()))
    s=func_map(arr)
    print(s)
main()
