a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a > b and a > c:
    max_num = a
elif b > c:
    max_num = b
else:
    max_num = c
if a < b and a < c:
    min_num = a
elif b < c:
    min_num = b
else:
    min_num = c
print("Maximum number:", max_num)
print("Minimum number:", min_num)