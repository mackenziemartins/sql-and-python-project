# comp3005 final project

import psycopg2

# NOTE: edit these variables to fit your machine
conn = psycopg2.connect(database =  "FINAL3005",
                        host =      "localhost",
                        password =  "postgres",
                        user =      "postgres",
                        port =      "5432")

cursor = conn.cursor


# function that checks the users role, then takes their login information.
def userLogin():
    print("Welcome to the login page, please indicate your status.")
    status = input("1. Member\n2. Trainer\n3. Admin\n")
    if status == "1":
        status = "members"
    elif status == "2":
        status = "trainers"
    elif status == "3":
        status = "admins"
    
    print(f"Welcome to the login page for {status}. Please enter your information below:\n")
    username = input("Enter your username:")
    password = input("Enter your password:")
    try:
        SQL = "SELECT * FROM %s WHERE username = %s AND pass = %s"
        cursor.execute(SQL, (status, username, password))
        cursor.fetchall()
    except psycopg2.Error as e:
        print("Something went wrong, please try again.")
        print(e.diag.message_hint)
    return status, username

# gets the users memberID/adminID/trainerID from the respective table
def getID(status, username):
    if status == "Members":
        try:
            SQL = "SELECT member_id FROM members WHERE username = %s"
            cursor.execute(SQL, username)
            ID = cursor.fetchone()
        except psycopg2.Error as e:
            print("Something went wrong retrieving your ID number, please try again.")
            print(e.diag.message_hint)
    elif status == "Trainers":
        try:
            SQL = "SELECT trainer_id FROM trainers WHERE username = %s"
            cursor.execute(SQL, username)
            ID = cursor.fetchone()
        except psycopg2.Error as e:
            print("Something went wrong retrieving your ID number, please try again.")
            print(e.diag.message_hint)
    elif status == "admins":
        try:
            SQL = "SELECT admin_id from MEMBERS where username = %s"
            cursor.execute(SQL, username)
            ID = cursor.fetchone()
        except psycopg2.Error as e:
            print("Something went wrong retrieving your ID number, please try again.")
            print(e.diag.message_hint)

# functon that allows a user to register for the platform as a MEMBER
def registerMember():
    pass

# function that allows an ADMIN user to change a users role from member -> trainer
def promoteTrainer():
    pass

# function that allows a TRAINER user to lookup a MEMBER user by name
def memberLookup():
    pass

# function allowing a USER member to edit any information related to their account.
# uses helper functions
def updatingProfile():
    pass



# main function, where the actual application is made.
def main():
    flag = True
    while flag == True:
        print("Hello! Welcome to BLANK personal fitness database, would you like to log in or register a new account?")
        inp = input("1. Register a new account \n2. Log in as an existing user \n3. Quit")
        if inp == "1":
            pass
        elif inp == "2":
            pass
        elif inp == "3":
            flag = False
        else:
            print("\nInvalid Inputs were provided, please try again.")




main()
conn.close()
