name = input("Enter your name: ")
mark1 = int(input("Enter mark1: "))
mark2 = int(input("Enter mark2: "))
mark3 = int(input("Enter mark3: "))

invalid_marks = mark1 < 0 or mark1 > 100 or mark2 < 0 or mark2 > 100 or mark3 < 0 or mark3 > 100

if invalid_marks:
    print("Error: Marks should be between 0 and 100.")

else:
    total_marks = mark1 + mark2 + mark3
    avg_mark = total_marks / 3

    print("Name:", name)
    print("Total:", total_marks)
    print("Average:", round(avg_mark, 2))

    if avg_mark >= 90:
        print("Performance: Excellent")

    elif avg_mark >= 75:
        print("Performance: Very Good")

    elif avg_mark >= 50:
        print("Performance: Pass")

    else:
        print("Performance: Needs Improvement")