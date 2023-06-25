a=0
b=1
print(a)
print(b)

end=int(input("Enter the end for Fibonacci sequence: "))

print("the Fibonacci sequence until ", end," is: ")
while b < end:
    c = a + b
    print(c, end=" ")
    a=b
    b=c
