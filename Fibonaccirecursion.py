def fib_iter(n):
    a,b=0,1
    for i in range(n):
        print(a,end="")
        a,b = b,a+b
def fib_rec(n):
    if n<=1:
        return n
    return fib_rec(n-1)+fib_rec(n-2)
n = int(input("Enter number of terms:"))
print("Iteration:")
fib_iter(n)
print("\nRecursion:")
for i in range(n):
    print(fib_rec(i), end="")

