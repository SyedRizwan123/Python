# Create an empty dictionary to store all users
users = {}
# SIGN UP MODULE
def signup():
    print("\n--- SIGN UP ---")
    username = input("Enter new username: ")
    # Check if username already exists
    if username in users:
        print("⚠️ Username already exists! Try another one.")
    else:
        password = input("Enter new password: ")
        users[username] = password  # Store username and password in dictionary
        print("✅ Account created successfully!")
# LOGIN MODULE
def login():
    print("\n--- LOGIN ---")
    username = input("Enter username: ")
    password = input("Enter password: ")
    # Check if username exists and password matches
    if username in users and users[username] == password:
        print("✅ Login Successful! Welcome,", username)
    else:
        print("❌ Invalid username or password!")
# 3️⃣ MAIN MENU
def main():
    while True:
        print("\n===== MENU =====")
        print("1. Sign Up")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")
        if choice == '1':
            signup()
            print(users)
        elif choice == '2':
            login()
        elif choice == '3':
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice, please try again.")

# Run the program
main()