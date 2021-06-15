def func(a):
    if(a=='a' or a=='A' or a=='e' or a=='E' or a=='i' or a=='I' or a=='o' or a=='O' or a=='u' or a=='U' ):
        return True
    else:
        return False
def main():
    a=input()
    print(func(a))
main()
