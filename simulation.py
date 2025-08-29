# Focus: Confidentiality

# --- hardcoded "login" (no input, no hashing) ---
current_user = {
    "username": "david",
    "role": "admin"   # change to "user" to test the other case
}

# each role maps to the list of allowed actions
permissions = {
    "admin": ["view_admin_panel"],
    "user":  ["view_user_dashboard"]
}

# --- protected actions (simulate two endpoints) ---
def view_admin_panel():
    print("ADMIN endpoint: Viewing system settings and reports.")

def view_user_dashboard():
    print("USER endpoint: Viewing personal dashboard.")

# map action name -> function
actions = {
    "view_admin_panel": view_admin_panel,
    "view_user_dashboard": view_user_dashboard
}

# --- access control check ---
def can_access(role: str, action: str) -> bool:
    return action in permissions.get(role, [])

def run_action(action_name: str):
    role = current_user["role"]
    if can_access(role, action_name):
        actions[action_name]()
    else:
        print(f"Access denied: role '{role}' cannot perform '{action_name}'.")

if __name__ == "__main__":
    print(f"Logged in as: {current_user['username']} (role: {current_user['role']})\n")

    # Simulate both endpoints
    run_action("view_admin_panel")      # only admin should pass
    run_action("view_user_dashboard")   # only user should pass

"""
Explanation (CIA Triad - Confidentiality):
this script hardcodes a username and role to simulate authentication, then restricts
access to two protected actions using role-based access control (RBAC)
only 'admin' can access the admin endpoint, and only 'user' can access the user endpoint
By preventing unauthorized roles from accessing certain actions/data, the design protects
Confidentiality (information is only available to authorized users).
"""
