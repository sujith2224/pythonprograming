student_marks = {
    "Math": 95,
    "Science": 88,
    "English": 90
}
value_to_find = 88
found = False
for key, value in student_marks.items():
    if value == value_to_find:
        print("Key for value", value_to_find, "is:", key)
        found = True
        break
if not found:
    print("Value not found in dictionary")