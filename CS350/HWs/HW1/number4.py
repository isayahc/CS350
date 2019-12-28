def validtri(a,b,c):
    if (a + b <= c) or (a + c <= b) or (b + c <= a) : 
        return False
    else: 
        return True 

print("insert values for triangels ")
a = input()
b = input()
c = input ()

if validtri(a, b, c): 
    print("Valid")  
else: 
    print("Invalid") 

