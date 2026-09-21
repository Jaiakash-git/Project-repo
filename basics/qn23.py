s_username="Akash"
S_password="123"

uname=input("enter the username")
password=input("enter the password")

def validate():
    if(s_username==uname and S_password==password):
       return True
    else:
        return False

a=validate()
print(a)
