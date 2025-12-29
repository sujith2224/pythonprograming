base = int(input("Enter base number: "))
exp = int(input("Enter exponent: "))
power = 1
for i in range(exp):
    power = power * base
print("Power =", power)
