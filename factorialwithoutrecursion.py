def fact_iter(n):
    f=1
    for i in range(1,n+1):
        f=f * i
    return f
def fact_rec(n):
    if n == 0 or n==1:
        return 1
    return n * fact_rec(n-1)
n=int(input("Enter a number:"))
print("Factorial without recursion:", fact_iter(n))
print("Factorial with recursion:", fact_rec(n))

