class shape:
    def __init__(self,s,a,b,c):
        self.s=s
        self.a=a
        self.b=b
        self.c=c

    def calc(self,s,a,b,c):
        return (self.s*(self.s-self.a)*(self.s-self.b)*(self.s-self.c))**0.5


s,a,b,c=map(int,input().split())
sh=shape(s,a,b,c)
s=sh.calc(s,a,b,c)
print(s)
