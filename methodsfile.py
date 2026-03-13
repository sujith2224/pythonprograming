file = open("sample.txt", "w")

file.write("Hello Student\n")
file.write("This is a Python File Handling Program\n")

lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
file.writelines(lines)

file.close()

file = open("sample.txt", "r")
print("Using read():")
print(file.read())
file.close()

file = open("sample.txt", "r")
print("Using readline():")
print(file.readline())
print(file.readline())
file.close()

file = open("sample.txt", "r")
print("Using readlines():")
print(file.readlines())
file.close()