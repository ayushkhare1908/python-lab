n=input('enter the no')
def fact(n):
    if(n>1):
        return n*fact(n-1)
    else:
        return 1;

fact(5)    
