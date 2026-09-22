mark = int(input("Enter your marks: "))

if mark < 0 or mark > 100:
    print("Invalid marks. Enter a value between 0 and 100.")

elif mark >= 90:
    print("Grade: A")

elif mark >= 75:
    print("Grade: B")

elif mark >= 60:
    print("Grade: C")

elif mark >= 40:
    print("Grade: D")

else:
    print("You have failed the exam.")