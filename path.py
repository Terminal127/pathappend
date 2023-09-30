#!/usr/bin/env python3

import os

# Function to update the user database
def update_user_database(username):
    # Replace this with your actual database update logic
    print(f"Updating user database for {username}...")

# Function to locate and modify /etc/bash.bashrc
def modify_bashrc(path_to_append):
    bashrc_path = "/etc/bash.bashrc"

    # Check if the bashrc file exists
    if os.path.exists(bashrc_path):
        try:
            with open(bashrc_path, "a") as bashrc_file:
                # Check if the path exists before appending
                if os.path.exists(path_to_append):
                    bashrc_file.write(f'\nexport PATH="$PATH:{path_to_append}"\n')
                    print(f"Path '{path_to_append}' added to PATH in {bashrc_path}")
                else:
                    print(f"Path '{path_to_append}' does not exist, skipping modification of {bashrc_path}")
        except Exception as e:
            print(f"An error occurred while modifying {bashrc_path}: {str(e)}")
    else:
        print(f"{bashrc_path} does not exist. Unable to modify.")

# Input from the user
username = input("Enter the username to update the database: ")

# Ask the user if they want to update the database
update_database = input("Do you want to update the database? (yes/no): ").lower()

if update_database == "yes":
    # Update the user database
    update_user_database(username)

# Prompt for the path to append to PATH variable
path_to_append = input("Enter the path to append to the PATH variable: ")

# Modify /etc/bash.bashrc
modify_bashrc(path_to_append)

