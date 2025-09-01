# A hardcoded dictionary of users and their roles
# In a real application, this data would come from a database.
USERS_DATABASE = {
    "admin_user": {"role": "admin"},
    "standard_user": {"role": "user"},
}

# Variable to simulate the currently logged-in user session
# The value is hardcoded for this simulation.
# Change this variable to test different roles.
logged_in_user = "standard_user"  # Try changing this to "admin_user"

# Function to simulate logging in
def login(username):
    """Sets the global variable to simulate a successful login."""
    global logged_in_user
    if username in USERS_DATABASE:
        logged_in_user = username
        print(f"User '{username}' logged in successfully.")
    else:
        print(f"Error: User '{username}' not found.")

# The admin-only protected action
def admin_action():
    """Simulates an action that only an admin can perform."""
    if USERS_DATABASE.get(logged_in_user, {}).get("role") == "admin":
        print(f"Access Granted: User '{logged_in_user}' is an admin and can access this route.")
        print("--- Executing admin-only action ---")
    else:
        print(f"Access Denied: User '{logged_in_user}' does not have admin privileges.")

# The user-only protected action
def user_action():
    """Simulates an action that only a standard user can perform."""
    if USERS_DATABASE.get(logged_in_user, {}).get("role") == "user":
        print(f"Access Granted: User '{logged_in_user}' is a standard user and can access this route.")
        print("--- Executing user-only action ---")
    else:
        print(f"Access Denied: User '{logged_in_user}' does not have standard user privileges.")

# --- Simulation Execution ---

print(f"--- Simulating login for: '{logged_in_user}' ---\n")

# Attempt to access both protected actions
admin_action()
print("-" * 20)
user_action()

# Example: Simulate logging in as the other user
print("\n" + "=" * 30 + "\n")
login("admin_user")

print(f"\n--- Simulating login for: '{logged_in_user}' ---\n")

# Attempt to access both protected actions again
admin_action()
print("-" * 20)
user_action()
