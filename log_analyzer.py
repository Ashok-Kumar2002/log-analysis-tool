# Open and read the log file
with open('sample.log', 'r') as file:
    log_lines = file.readlines()

# Set up counters and lists
failed_logins = 0
successful_logins = 0
invalid_users = []

# Goes through each line of the log
for line in log_lines:
    if "Failed password" in line:
        failed_logins += 1
        if "invalid user" in line:
            # Extract the invalid username
            parts = line.split("invalid user")
            if len(parts) > 1:
                user_part = parts[1].split()
                if user_part:
                    invalid_users.append(user_part[0])

    elif "Accepted password" in line:
        successful_logins += 1

# Print basic summary of it
print("===== Log Analysis Report =====")
print(f"Failed login attempts: {failed_logins}")
print(f"Successful logins: {successful_logins}")
print("Invalid users tried:")
for user in set(invalid_users):
    print(f" - {user}")

