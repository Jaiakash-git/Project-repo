BDA_marks = int(input("Enter your BDA marks: "))
ethics_marks = int(input("Enter your Ethics: "))
iot_marks = int(input("Enter your Iot: "))

total_marks = (BDA_marks + ethics_marks + iot_marks)
avg_marks = total_marks / 3
percentage = (total_marks/300) * 100

print("Total marks:",total_marks)
print("Average mark:",round(avg_marks,2))
print("Percentage:",round(percentage,2) ,"%")   
