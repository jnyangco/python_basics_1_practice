def login_message(username, environment):
    return f"Logging in as {username} in {environment}"

message = login_message("qa-user1", "qa-1")
print(message)
