#find largest number with out using max function

def largestnumber(a:int, b:int, c:int):
    if a >=b and a>=c:
        return a
    elif b>=c and b>=a:
        return b
    else:
        return c

 
a = int(input("Enter first number: "))  
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print(largestnumber(a, b, c))


# or instead of input you can write 
# print (largestnumber (5,12,8))