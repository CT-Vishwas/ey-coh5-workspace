inp_str = input("Enter your email id: ")

if inp_str.find('@') == -1 or inp_str.count('@') > 1 :
    print("Invalid Email ID")
else:
    username = inp_str[: inp_str.find('@')]
    print(f"The user name for {inp_str} is {username}")