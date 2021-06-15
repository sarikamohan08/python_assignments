def filter_long_words(arr,n):
    l=[]
    for i in arr:
        if(len(i)>n):
            l.append(i)
    return l

def main():
    t=int(input("enter no.of words in list:"))
    arr=list(map(str,input().split()))
    n=int(input("length of words:"))
    s=filter_long_words(arr,n)
    print(s)
main()
