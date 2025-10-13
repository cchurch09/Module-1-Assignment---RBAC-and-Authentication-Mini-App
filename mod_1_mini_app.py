#Create a dictionary (This is to define to variables for our code)
def main():
      
    users = {"Cailli": "admin",
         "Clive": "user"}
    username = input("Enter username: ")
    role = users.get(username, None)

    if role:
            print(f"Welcome {username}, your are a {role}")
            if role == "admin":
                print("You can access the admin panel.")
                adminPanel()
            else:
                print("You can access the user dashboard")
                userDashboard()
    else:
            print("access denied")
def adminPanel():
    print("1) Users")
    print("2) Settings")
    print("3) Backrounds")
    input()
def userDashboard():
    print("1) Settings")
    print("2) Change password")

main()