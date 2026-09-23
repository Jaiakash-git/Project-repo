name = input("Enter your name: ")
average_mark = int(input("Enter your Average mark: "))
attendance = int(input("Enter your attendance percentage: "))

invalid_details = average_mark < 0 or average_mark > 100 or attendance < 0 or attendance > 100


if invalid_details:
    print("Enter valid details")
else:
    print("Name: ",name)
    print("Average: ",average_mark)
    print("attendance: ",attendance)

    if average_mark >= 50 and attendance >= 75:
      print("status: Eligible")
    else:
      print("Status: Not Eligible")
