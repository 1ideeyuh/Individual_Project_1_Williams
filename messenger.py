import os

name = "lydia"

file_name = input("Please enter the messenger filename (must end in .txt)".strip())
if not file_name.endswith(".txt"):
    file_name += ".txt"

if os.path.exists(file_name):
    print(f"\n'{file_name}' found. Reading contents: \n")
    with open (file_name, "r") as f:
        contents = f.read()
    print(contents)

else:
    print(f"n'\{file_name}' does not exist. Creating it now...")
    #create empty file
    with open(file_name, "w") as f:
        pass

#prompt user for message
user_message = input("\nEnter your message: ")

#format message with the name prefix
formatted_message = f"{name}: {user_message}\n"

#append new message to the file 
with open(file_name, "a") as f:
    f.write(formatted_message)

print(f"\nMessage saved to '{file_name}'.")


