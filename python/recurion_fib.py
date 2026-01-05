n=int(input("enter a number :"))
a=0
b=1
c=0
def fibonacci():
    global a , b, c,n
    while n:
        n-=1
        print(c,end=" ")
        a=b
        b=c
        c=a+b
        
        fibonacci()

fibonacci()
