""" 
    1. create account with email, username and password and save the details in the PostgreSQL database
    2. get username and password from user
    3. validate the credentials stored against the database
"""

import codecs
import pwinput
from psycopg2 import connect
from base64 import b64decode
from pyfiglet import figlet_format

header = figlet_format("Login using DB")
print(header)


def get_pasword(user):
    with open(f"C:/Users/user/passwords/{user}.b64") as file:
        encrypted_pasword = file.read()
    return codecs.decode(b64decode(encrypted_pasword))


def get_clinet():
    user = "postgres"
    password = get_pasword(user)
    conn = connect(host="127.0.0.1", port="5432", database="postgres",
                   user="postgres", password=password)
    print(conn.status)
    return conn


def create_table(table_name):
    conn = get_clinet()
    create_query = '''CREATE TABLE IF NOT EXISTS login_test (email varchar(128) primary key, user_name varchar(64) not null, password varchar(64) not null);'''
    print("Query Triggered: ", create_query)
    cur = conn.cursor()
    cur.execute(create_query)
    conn.commit()


def save_user_details(email, username, password):
    conn = get_clinet()
    insert_query = f"INSERT INTO login_test (email, user_name, password) VALUES('{email}','{username}','{password}')"
    print("Query Triggered: ", insert_query)
    cur = conn.cursor()
    cur.execute(insert_query)
    conn.commit()


def fetch_details(username, password):
    conn = get_clinet()
    select_query = f"select * from login_test where user_name='{username}'"
    print("Query Triggered: ", select_query)
    cur = conn.cursor()
    cur.execute(select_query)
    res = cur.fetchall()
    return res


def get_user_credentials():
    # create a table if not exists
    create_table("login")
    print("Login table created successfully")

    login_in = input("Do you want to create a new account[Y/n]:")

    if login_in.lower() == 'y':
        email = input("Email:")
        username = input("Username: ")
        password = pwinput.pwinput()
        try:
            save_user_details(email, username, password)
            print("Created account successfully ")
        except:
            print("Error in creating the account.Please try again!")
    elif login_in.lower() == 'n':
        username = input("Username: ")
        password = pwinput.pwinput()
        try:
            res = fetch_details(username, password)
            if username in res[0] and password in res[0]:
                print("Logged in successfully")
            else:
                print("Invalid Credentials.")
        except:
            print("Error in login. Please try again!")
    else:
        print("Invalid input.Please try again!!!")


get_user_credentials()
