# comp3005 final project

import psycopg2

# NOTE: edit these variables to fit your machine
conn = psycopg2.connect(database =  "FINAL3005",
                        host =      "localhost",
                        password =  "postgres",
                        user =      "postgres",
                        port =      "5432")

cursor = conn.cursor


def main():
    flag = True
    while flag == True:
        print("Hello! Welcome to BLANK personal fitness database, would you like to log in?")
        inp = input("\nY/N: ")
        if inp.upper() == "Y":
            pass
        else:
            conn.close()
            exit()


main()
conn.close()