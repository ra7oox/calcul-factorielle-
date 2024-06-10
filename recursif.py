def recursif(x):
    f=1
    if x==0:
        return f
    
    f=x*recursif(x-1)
    return  f
        
print(recursif(6))