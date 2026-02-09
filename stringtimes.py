string = input("Enter a string: ")
letter = input("Enter a letter: ")

count = 0
for ch in string:
    if ch == letter:
        count += 1

print("The letter", letter, "occurs", count, "times.")
