def is_prime_loop(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
def is_prime_recursion(num, i=2):
    if num <= 1:
        return False
    if i == num:
        return True
    if num % i == 0:
        return False
    return is_prime_recursion(num, i + 1)
num = int(input("Enter a number: "))
print("\nWithout Recursion:")
if is_prime_loop(num):
    print("Prime number")
else:
    print("Not a prime number")
print("\nWith Recursion:")
if is_prime_recursion(num):
    print("Prime number")
else:
    print("Not a prime number")
