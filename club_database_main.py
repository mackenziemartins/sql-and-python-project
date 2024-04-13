import psycopg2

# COMP 3005 B Project V2
# Kareem Kaddoura (101140255)
# Mackenzie Martins (101228049)
# Club Database Queries & Main

connection = psycopg2.connect(
    database = "club_database",
    host = "localhost",
    user = "postgres",
    password = "kareem872001",
    port = "5432",
)

cursor = connection.cursor()


# Member Functions

# Create a new member
def register_member(first_name, last_name, username, password):
    try:
        query = "INSERT INTO Members (first_name, last_name, username, password) VALUES (%s, %s, %s, %s)"
        data = (first_name, last_name, username, password)
        cursor.execute(query, data)
        connection.commit()
        print("Member registered successfully.")
    except psycopg2.Error as err:
        print("Unable to register member:", err.pgerror)
        exit()

# Retrieve member name
def get_member_name(username, password):
    try:
        query = "SELECT first_name, last_name FROM Members WHERE username = %s AND password = %s"
        data = (username, password)
        cursor.execute(query, data)
        member_data = cursor.fetchone()
        if member_data == None:
            print("\nThis member does not exist.")
        else:
            member_info = member_data[0] + " " + member_data[1]
            return member_info
    except psycopg2.Error as err:
        print("Unable to retrieve member:", err.pgerror)
        exit()

# Retrieve member number
def get_member_num(first_name, last_name):
    try:
        query = "SELECT member_id FROM Members WHERE first_name = %s AND last_name = %s"
        data = (first_name, last_name)
        cursor.execute(query, data)
        member_data = cursor.fetchone()
        if member_data == None:
            print("\nThis member does not exist.")
        else:
            member_info = member_data[0]
            return member_info
    except psycopg2.Error as err:
        print("Unable to retrieve member:", err.pgerror)
        exit()

# Retrieve all member info
def get_member_info(member_id):
    try:
        query = "SELECT * FROM Members WHERE member_id = %s"
        data = (member_id)
        cursor.execute(query, data)
        member_info_data = cursor.fetchone()
        if member_info_data == None:
            print("\nThis member does not exist.")
        else:
            print("Member Info:\n")
            print("Current First Name:", member_info_data[1])
            print("Current Last Name:", member_info_data[2])
            print("Current Username:", member_info_data[3])
            print("Current Password:", member_info_data[4])
    except psycopg2.Error as err:
        print("Unable to retrieve member:", err.pgerror)
        exit()

# Update member profile
def update_profile(member_id, first_name, last_name, username, password):
    try:
        query = "UPDATE Members SET first_name = %s, last_name = %s, username = %s, password = %s WHERE member_id = %s"
        data = (first_name, last_name, username, password, member_id)
        cursor.execute(query, data)
        connection.commit()
        print("Profile updated successfully.")
    except psycopg2.Error as err:
        print("Unable to update profile:", err.pgerror)
        exit()

# Insert member fitness goals
def insert_fitness_goals(member_id, goal_weight, goal_mile_time, goal_bench, goal_squat, goal_deadlift, goal_plank):
    try:
        query = """INSERT INTO Goals (member_id, goal_weight, goal_mile_time, goal_bench, goal_squat, goal_deadlift, goal_plank)
                VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        data = (member_id, goal_weight, goal_mile_time, goal_bench, goal_squat, goal_deadlift, goal_plank)
        cursor.execute(query, data)
        connection.commit()
        print("Goals added successfully.")
    except psycopg2.Error as err:
        print("Unable to add goals:", err.pgerror)
        exit()

# Update fitness goals
def update_fitness_goals(member_id, goal_weight, goal_mile_time, goal_bench, goal_squat, goal_deadlift, goal_plank):
    try:
        query = "UPDATE Goals SET goal_weight = %s, goal_mile_time = %s, goal_bench = %s, goal_squat = %s, goal_deadlift = %s, goal_plank = %s WHERE member_id = %s"
        data = (goal_weight, goal_mile_time, goal_bench, goal_squat, goal_deadlift, goal_plank, member_id)
        cursor.execute(query, data)
        connection.commit()
        print("Goals updated successfully.")
    except psycopg2.Error as err:
        print("Unable to update goals:", err.pgerror)
        exit()

# Display member fitness goals
def display_fitness_goals(member_id):
    try:
        query = "SELECT * FROM Goals WHERE member_id = %s"
        data = (member_id)
        cursor.execute(query, data)
        member_fg_data = cursor.fetchone()
        if member_fg_data == None:
            print("There are no fitness goals available for this member.")
        else:
            print("----", "Member #", member_fg_data[1], "----")
            print("Weight Goal:", member_fg_data[2])
            print("Mile Time Goal:", member_fg_data[3])
            print("Bench Goal:", member_fg_data[4])
            print("Squat Goal:", member_fg_data[5])
            print("Deadlift Goal:", member_fg_data[6])
            print("Plank Goal:", member_fg_data[7])
            print("------------------")
    except psycopg2.Error as err:
        print("Unable to display goals:", err.pgerror)
        exit()

# Insert member health metrics
def insert_health_metrics(member_id, date, height, weight, mile_time, resting_hr, blood_pressure):
    try:
        query = """INSERT INTO Health_metrics (member_id, date, height, weight, mile_time, resting_hr, blood_pressure)
                VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        data = (member_id, date, height, weight, mile_time, resting_hr, blood_pressure)
        cursor.execute(query, data)
        connection.commit()
        print("Health metrics added successfully.")
    except psycopg2.Error as err:
        print("Unable to add health metrics:", err.pgerror)
        exit()

# Display member health metrics
def display_health_metrics(member_id):
    try:
        query = "SELECT * FROM Health_metrics WHERE member_id = %s"
        data = (member_id)
        cursor.execute(query, data)
        member_hm_data = cursor.fetchall()
        if len(member_hm_data) == 0:
            print("There are no health metrics available for this member.")
        else:
            for entry in member_hm_data:
                print("----", "Entry #", entry[0], "----")
                print("Date:", entry[2])
                print("Height:", entry[3])
                print("Weight:", entry[4])
                print("Mile Time:", entry[5])
                print("Resting Heart Rate:", entry[6])
                print("Blood Pressure:", entry[7])
                print("------------------")
    except psycopg2.Error as err:
        print("Unable to display health metrics:", err.pgerror)
        exit()

# Display available exercise routines
def display_exercise_routines():
    try:
        cursor.execute("SELECT * FROM Routines")
        routine_data = cursor.fetchall()
        if len(routine_data) == 0:
            print("There are no routines.")
        else:
            for entry in routine_data:
                print(entry[1] + ": " + entry[2])
    except psycopg2.Error as err:
        print("Unable to display routines:", err.pgerror)
        exit()

# Schedule personal training session
def schedule_session():
    "" # FINISH

# Cancel personal training session
def cancel_session():
    "" # FINISH

# Sign up for group fitness class
def sign_up_class():
    "" # FINISH

# Unregister from group fitness class
def cancel_class():
    "" # FINISH

# View member schedule
def view_schedule():
    "" # FINISH

# View member bills
def view_bill(member_id):
    try:
        query = "SELECT * FROM Billing WHERE member_id = %s"
        data = (member_id)
        cursor.execute(query, data)
        bill_data = cursor.fetchall()
        if len(bill_data) == 0:
            print("There are no bills available for this member.")
        else:
            for entry in bill_data:
                print("Bill #" + str(entry[0]) + ": " + entry[2] + "- $" + str(entry[3]) + ", Due: " + str(entry[4]) + ", Paid? " + str(entry[5]))
    except psycopg2.Error as err:
        print("Unable to display billing:", err.pgerror)
        exit()

# Pay bill
def pay_bill(bill_id, bill_amount, bill_paid):
    try:
        query = "UPDATE Billing SET bill_paid = %s WHERE bill_id = %s AND %s >= bill_amount"
        data = (bill_paid, bill_id, bill_amount)
        cursor.execute(query, data)
        connection.commit()
        print("Billing paid successfully.")
    except psycopg2.Error as err:
        print("Unable to pay bill:", err.pgerror)
        exit()

# Display member dashboard
def display_dashboard(member_id):
    try:
        print("---------- Health Metrics ----------")
        display_health_metrics(member_id)
        print("\n---------- Fitness Goals  ----------")
        display_fitness_goals(member_id)
        print("\n------------- Schedule -------------")
        #FINISH
        print("\n------------- Routines -------------")
        display_exercise_routines()
        print("\n------------- Billing -------------")
        view_bill(member_id)
        print("------------------------------------")
    except psycopg2.Error as err:
        print("Unable to display dashboard:", err.pgerror)
        exit()

# Trainer Functions

# Retrieve trainer name
def get_trainer_name(username, password):
    try:
        query = "SELECT first_name, last_name FROM Trainers where username = %s AND password = %s"
        data = (username, password)
        cursor.execute(query, data)
        trainer_data = cursor.fetchone()
        if trainer_data == None:
            print("\nThis trainer does not exist.")
        else:
            trainer_info = trainer_data[0] + " " + trainer_data[1]
            return trainer_info
    except psycopg2.Error as err:
        print("Unable to retrieve trainer:", err.pgerror)
        exit()

# Retrieve trainer number
def get_trainer_num(first_name, last_name):
    try:
        query = "SELECT trainer_id FROM Trainers where first_name = %s AND last_name = %s"
        data = (first_name, last_name)
        cursor.execute(query, data)
        trainer_data = cursor.fetchone()
        if trainer_data == None:
            print("\nThis trainer does not exist.")
        else:
            trainer_info = trainer_data[0]
            return trainer_info
    except psycopg2.Error as err:
        print("Unable to retrieve trainer:", err.pgerror)
        exit()

# View all member names
def view_members():
    try:
        cursor.execute("SELECT first_name, last_name FROM Members")
        members_data = cursor.fetchall()
        if members_data == None:
            print("\nThere are no registered members.")
        else:
            print("\nRegistered Members:")
            for entry in members_data:
                print(entry[0] + " " + entry[1])
    except psycopg2.Error as err:
        print("Unable to retrieve members:", err.pgerror)
        exit()

# View member profile
def view_member_profile(first_name, last_name):
    try:
        num = get_member_num(first_name, last_name)
        display_dashboard(str(num))
    except psycopg2.Error as err:
        print("Unable to retrieve member:", err.pgerror)
        exit()

# Display trainer availabilites
def display_availability():
    "" # FINISH

# Update trainer availabilites
def update_availability():
    "" # FINISH

# Admins Functions

# Retrieve admin name
def get_admin_name(username, password):
    try:
        query = "SELECT first_name, last_name FROM Admins WHERE username = %s AND password = %s"
        data = (username, password)
        cursor.execute(query, data)
        admin_data = cursor.fetchone()
        if admin_data == None:
            print("\nThis admin does not exist.")
        else:
            admin_info = admin_data[0] + " " + admin_data[1]
            return admin_info
    except psycopg2.Error as err:
        print("Unable to retrieve admin:", err.pgerror)
        exit()

# Retrieve admin number
def get_admin_num(first_name, last_name):
    try:
        query = "SELECT admin_id FROM Admins WHERE first_name = %s AND last_name = %s"
        data = (first_name, last_name)
        cursor.execute(query, data)
        admin_data = cursor.fetchone()
        if admin_data == None:
            print("\nThis admin does not exist.")
        else:
            admin_info = admin_data[0]
            return admin_info
    except psycopg2.Error as err:
        print("Unable to retrieve admin:", err.pgerror)
        exit()

# View trainers
def view_trainers():
    try:
        cursor.execute("SELECT first_name, last_name FROM Trainers")
        trainers_data = cursor.fetchall()
        if trainers_data == None:
            print("\nThere are no registered trainers.")
        else:
            print("\nRegistered Trainers:")
            for entry in trainers_data:
                print(entry[0] + " " + entry[1])
    except psycopg2.Error as err:
        print("Unable to retrieve trainers:", err.pgerror)
        exit()

# Add new room
def add_room(room_name, max_members):
    try:
        query = "INSERT INTO Rooms (room_name, max_members) VALUES (%s, %s)"
        data = (room_name, max_members)
        cursor.execute(query, data)
        connection.commit()
        print("Room created successfully.")
    except psycopg2.Error as err:
        print("Unable to create room:", err.pgerror)
        exit()

# Display rooms
    "" # FINISH

# Manage room bookings
def manage_room():
    "" # FINISH

# View equipments
def view_equipments():
    try:
        cursor.execute("SELECT * FROM Equipment")
        equipment_data = cursor.fetchall()
        if equipment_data == None:
            print("\nThere are no available equipment.")
        else:
            print("\nAvailable Equipment:\n")
            for entry in equipment_data:
                print("----", entry[1], "ID:", entry[0], "----")
                print("Upcoming Maintenance Date:", entry[2])
                print("Last Maintenance Date:", entry[3])
                print("---------------------")
    except psycopg2.Error as err:
        print("Unable to retrieve equipment:", err.pgerror)
        exit()

# Equipment maintenance
def maintain_equipment(equipment_id, upcoming_maintenance_date, last_maintenance_date):
    try:
        query = "UPDATE Equipment SET upcoming_maintenance_date = %s, last_maintenance_date = %s WHERE equipment_id = %s"
        data = (upcoming_maintenance_date, last_maintenance_date, equipment_id)
        cursor.execute(query, data)
        connection.commit()
        print("Equipment maintained successfully.")
    except psycopg2.Error as err:
        print("Unable to maintain equipment:", err.pgerror)
        exit()

# View all bills
def view_all_bills():
    try:
        cursor.execute("SELECT * FROM Billing")
        billing_data = cursor.fetchall()
        if billing_data == None:
            print("\nThere are no available billings.")
        else:
            print("\nBilling:\n")
            for entry in billing_data:
                print("----", "Member ID:", entry[1], "----")
                print("Description:", entry[2])
                print("Amount: $" + str(entry[3]))
                print("Due Date:", entry[4])
                print("Bill paid?", entry[5])
                print("-------------------")
    except psycopg2.Error as err:
        print("Unable to retrieve equipment:", err.pgerror)
        exit()

# Create member billing
def create_billing(member_id, bill_desc, bill_amount, due_date, bill_paid):
    try:
        query = "INSERT INTO Billing (member_id, bill_desc, bill_amount, due_date, bill_paid) VALUES (%s, %s, %s, %s, %s)"
        data = (member_id, bill_desc, bill_amount, due_date, bill_paid)
        cursor.execute(query, data)
        connection.commit()
        print("Billing created successfully.")
    except psycopg2.Error as err:
        print("Unable to create billing:", err.pgerror)
        exit()

# View all classes
def view_classes():
    "" # FINISH

# Schedule new class
def schedule_class():
    "" # FINISH

# Update class schedules
def update_classes():
    "" # FINISH

# Delete class
def delete_class():
    "" # FINISH

def main():
    print("Welcome to the Mackioka Health & Fitness System!\n")
    while True:
        print("\nMackioka Health & Fitness\n")
        print("Please select your role:\n1: Member\n2: Trainer\n3: Administrative Staff\n4: Exit\n")
        user_role = input()
        print("\n")
        
        # Members
        if user_role == "1":
            print("Options:\n1: Login\n2: Create New User\n3: Return\n")
            request = input()
            print("\n")
            if request == "1":
                user = input("Username: ")
                pw = input("Password: ")
                if get_member_name(user, pw) == None:
                    print("Please try again.")
                else:
                    member_name = get_member_name(user, pw)
                    member_num = str(get_member_num(member_name.split()[0], member_name.split()[1]))
                    while True:
                        print("\nWelcome,", member_name, "\n")
                        print("Options:\n1: View Dashboard\n2: New Health Metrics Entry\n3: Update Fitness Goals\n4: Schedule Training Session\n5: Join Class\n6: Pay Bills\n7: Update Personal Information\n8: Logout\n")
                        member_request = input()
                        print("\n")
                        if member_request == "1":
                            print(member_name + ", ID #" + member_num + "\n")
                            display_dashboard(member_num)
                        elif member_request == "2":
                            display_health_metrics(member_num)
                            print("New Health Metrics Entry:\n")
                            hm_date = input("Date (YYYY/MM/DD): ")
                            hm_height = input("Height (cm): ")
                            hm_weight = input("Weight (kg): ")
                            hm_mile_time = input("Mile time (HH:MM:SS): ")
                            hm_resting_hr = input("Resting Heart Rate (BPM): ")
                            hm_blood_pressure = input("Blood Pressure (mmHg/mmHg): ")
                            insert_health_metrics(member_num, hm_date, hm_height, hm_weight, hm_mile_time, hm_resting_hr, hm_blood_pressure)
                        elif member_request == "3":
                            display_fitness_goals(member_num)
                            print("New Updates:\n")
                            update_weight = input("Weight Goal (kg): ")
                            update_mile_time = input("Mile Time Goal (HH:MM:SS): ")
                            update_bench = input("Bench Goal (kg): ")
                            update_squat = input("Squat Goal (kg): ")
                            update_deadlift = input("Deadlift Goal (kg): ")
                            update_plank = input("Plank Goal (HH:MM:SS): ")
                            update_fitness_goals(member_num, update_weight, update_mile_time, update_bench, update_squat, update_deadlift, update_plank)
                        elif member_request == "4":
                            "4" #FINISH SCHEDULE SESSIONS
                        elif member_request == "5":
                            "5" #FINISH JOIN CLASS
                        elif member_request == "6":
                            print("Billing:\n")
                            view_bill(member_num)
                            print("\nWhich bill would you like to pay?\n")
                            bill_num = input("Bill #: ")
                            #For UI, not real
                            card_name = input("Name on Card: ")
                            card_num = input("Card Number: ")
                            cvc_num = input("CVC: ")
                            # ---------------
                            amount = input("Amount ($): ")
                            pay_bill(bill_num, amount, "TRUE")
                        elif member_request == "7":
                            get_member_info(member_num)
                            print("New Updates:\n")
                            update_fname = input("First Name: ")
                            update_lname = input("Last Name: ")
                            update_us = input("Username: ")
                            update_pw = input("Password: ")
                            update_profile(member_num, update_fname, update_lname, update_us, update_pw)
                        elif member_request == "8":
                            print("Goodbye,", member_name, "\n")
                            break
                        else:
                            print("Incorrect input, please try again.")
            elif request == "2":
                m_fname = input("First Name: ")
                m_lname = input("Last Name: ")
                m_user = input("Username: ")
                m_pw = input("Password: ")
                register_member(m_fname, m_lname, m_user, m_pw)
                new_mem_num = get_member_num(m_fname, m_lname)
                print("Please enter your fitness goals upon joining this club:\n")
                new_weight = input("Weight Goal (kg): ")
                new_mile_time = input("Mile Time Goal (HH:MM:SS): ")
                new_bench = input("Bench Goal (kg): ")
                new_squat = input("Squat Goal (kg): ")
                new_deadlift = input("Deadlift Goal (kg): ")
                new_plank = input("Plank Goal (HH:MM:SS): ")
                insert_fitness_goals(new_mem_num, new_weight, new_mile_time, new_bench, new_squat, new_deadlift, new_plank)
            elif request == "3":
                continue
            else:
                print("Incorrect input, please try again.")
        
        # Trainers
        elif user_role == "2":
            print("Options:\n1: Login\n2: Return\n")
            request = input()
            print("\n")
            if request == "1":
                user = input("Username: ")
                pw = input("Password: ")
                if get_trainer_name(user, pw) == None:
                    print("Please try again.")
                else:
                    trainer_name = get_trainer_name(user, pw)
                    trainer_num = str(get_trainer_num(trainer_name.split()[0], trainer_name.split()[1])) # FINISH
                    while True:
                        print("\nWelcome,", trainer_name, "\n")
                        print("Options:\n1: View Member Profile\n2: Display Schedule\n3: Update Schedule\n4: Logout\n")
                        trainer_request = input()
                        print("\n")
                        if trainer_request == "1":
                            view_members()
                            print("\n")
                            m_first = input("Member First Name: ")
                            m_last = input("Member Last Name: ")
                            view_member_profile(m_first, m_last)
                        elif trainer_request == "2":
                            "" # FINISH
                        elif trainer_request == "3":
                            "" # FINISH
                        elif trainer_request == "4":
                            print("Goodbye,", trainer_name, "\n")
                            break
                        else:
                            print("Incorrect input, please try again.")
            elif request == "2":
                continue
            else:
                print("Incorrect input, please try again.")
            
        # Admins
        elif user_role == "3":
            print("Options:\n1: Login\n2: Return\n")
            request = input()
            print("\n")
            if request == "1":
                user = input("Username: ")
                pw = input("Password: ")
                if get_admin_name(user, pw) == None:
                    print("Please try again.")
                else:
                    admin_name = get_admin_name(user, pw)
                    admin_num = str(get_admin_num(admin_name.split()[0], admin_name.split()[1])) # FINISH
                    while True:
                        print("\nWelcome,", admin_name, "\n")
                        print("Options:\n1: View Trainers\n2: Manage Room Bookings\n3: Equipment Maintnance\n4: Update Class Schedule(s)\n5: Process Billing\n6: Logout\n")
                        admin_request = input()
                        print("\n")
                        if admin_request == "1":
                            view_trainers()
                        elif admin_request == "2":
                            "" # FINISH ROOM BOOKINGS
                        elif admin_request == "3":
                            view_equipments()
                            print("\n")
                            equipment_id = input("Equipment ID: ")
                            new_upcoming_date = input("Next Maintenance Date: ")
                            new_last_date = input("Maintained On: ")
                            maintain_equipment(equipment_id, new_upcoming_date, new_last_date)
                        elif admin_request == "4":
                            "" # FINISH UPDATE CLASS SCHEDULES
                        elif admin_request == "5":
                            print("Options:\n1: View All Billings\n2: Create Billing\n")
                            selection = input()
                            if selection == "1":
                                view_all_bills()
                            elif selection == "2":
                                view_members()
                                print("Which member would you like to bill?\n")
                                bill_fname = input("First Name: ")
                                bill_lname = input("Last Name: ")
                                mem_bill_num = get_member_num(bill_fname, bill_lname)
                                bill_desc = input("Bill Description: ")
                                bill_amount = input("Bill Amount ($): ")
                                due_date = input("Due Date (YYYY-MM-DD): ")
                                bill_paid = "FALSE"
                                create_billing(mem_bill_num, bill_desc, bill_amount, due_date, bill_paid)
                            else:
                                print("Incorrect input, please try again.")
                        elif admin_request == "6":
                            print("Goodbye,", admin_name, "\n")
                            break
                        else:
                            print("Incorrect input, please try again.")
            elif request == "2":
                continue
            else:
                print("Incorrect input, please try again.")

        # Exit
        elif user_role == "4":
            print("Have a nice day!")
            connection.close()
            break
        else:
            print("Incorrect input, please try again.")


main()