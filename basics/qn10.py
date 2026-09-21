age=int(input("Enter your age:" ))
salary=int(input("Enter your Salary"))
if(salary>=2000 or age<=20):
    loanamount=int(input("Loan amount:"))
    if(loanamount>=50000):
        print("max lm is 50000")
    else:
        print("You are eligible for loan")
else:
    print("You are not eligible for loan")