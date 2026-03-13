import random
file = open("random_numbers.txt", "w")
for i in range(20):
    num = random.randint(1, 100)
    file.write(str(num) + "\n")
file.close()
file = open("random_numbers.txt", "r")
print(file.read())
file.close()
