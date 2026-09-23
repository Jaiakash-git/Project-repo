name = input("Enter your name: ")
attendance = int(input("Enter your attendance percentage: "))

invalid_attendance = attendance < 0 or attendance > 100

print("Name: ",name)
print("attendance: ",attendance)

if invalid_attendance:
        print("Enter a valid Attendance Percentage")
elif attendance >= 75:
    print("Status: Eligible for Exam")
else:
    print("Status: Not Eligible for Exam")            
                 