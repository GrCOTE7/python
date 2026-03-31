from pymox_kit import cls, end, GREEN, CYAN, RED, R, CLIW
from pathlib import Path
import sqlite3, sys

if __name__ == "__main__":

    # cls()
    print("─" * CLIW)

    dir = Path(__file__).parent
    connection = sqlite3.connect(dir / "people.db")
    cursor = connection.cursor()

    try:
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS people (name TEXT, age INTEGER, skills STRING)"
        )
    except Exception as e:
        print(f"{RED}Error: {e}{R}")


def user_is_unic(name):

    rows = cursor.execute("SELECT name, age, skills FROM people").fetchall()

    for user in rows:
        if user[0] == name:
            return False
    return True


def insert_db():
    name = input("Name >> ")
    if user_is_unic(str(name)):
        age = input("Age >> ")
        skills = input("Skills >> ")

        if name != "" and age != "" and skills != "":
            cursor.execute(f"INSERT INTO people VALUES ('{name}', {age}, '{skills}')")
            connection.commit()

            print(name, "has been added to DB")
        else:
            print("All fields are required")
            insert_db()
    else:
        print(f"{RED}User already exists{R}")


def edit_db():
    name = input("Name of the person you'd like to edit >> ")
    field = input("Field to edit (name, age, skills)? >> ")
    updated_field = input(f"What would you like to update it to? >> ")

    try:
        cursor.execute(
            f"UPDATE people SET {field} = '{updated_field}' WHERE name = '{name}'"
        )
        connection.commit()
        print(f"{GREEN}{field} of {name} has been updated to {updated_field}{R}")
    except Exception as e:
        print(f"{RED}Error: {e}{R}")


def get_user_info():
    name = input("Name of the person you'd like to get info about >> ")
    try:
        user_info = cursor.execute(
            f"SELECT name, age, skills FROM people WHERE name = '{name}'"
        ).fetchone()
        if user_info:
            print(
                f"{GREEN}Name: {user_info[0]}, Age: {user_info[1]}, Skills: {user_info[2]}{R}"
            )
        else:
            print(f"{RED}User not found{R}")
    except Exception as e:
        print(f"{RED}Error: {e}{R}")


def delete_db():
    name = input("Name of the person you'd like to delete >> ")
    try:
        cursor.execute(f"DELETE FROM people WHERE name = '{name}'")
        connection.commit()
        print(f"{GREEN}{name} has been deleted from DB{R}")
    except Exception as e:
        print(f"{RED}Error: {e}{R}")


def display_db():
    rows = cursor.execute(
        "SELECT name, age, skills FROM people ORDER BY name ASC"
    ).fetchall()
    try:
        print("Users:")
        for user in rows:
            print(f"{GREEN}Name: {user[0]}, Age: {user[1]}, Skills: {user[2]}{R}")
    except Exception as e:
        print(f"{RED}Error: {e}{R}")


def exit_db():
    try:
        cursor.close()
        connection.close()
        sys.exit()
        print(f"{GREEN}Goodbye!{R}")
    except Exception as e:
        pass
    finally:
        print(f"{GREEN}Goodbye!{R}")
        sys.exit()


def select_options():
    print(
        f"{CYAN}Select an option:\n0. Exit\n1. Insert\n2. Display All\n3. Delete\n4. Edit\n5. Get Info{R}"
    )
    option = input("Option? >> ")
    if option == "0":
        exit_db()
    elif option == "1":
        insert_db()
    elif option == "2":
        display_db()
    elif option == "3":
        delete_db()
    elif option == "4":
        edit_db()
    elif option == "5":
        get_user_info()
    else:
        print(f"{RED}Invalid option{R}")

    # infinite loop
    while True:
        select_options()


if __name__ == "__main__":
    cls()
    print(f"{GREEN}Ready{R}")
    select_options()
    end()
