string = input("Enter a string: ")
reverse_string = string[::-1]
if string == reverse_string:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
