import sqlite3
import hashlib

conn = sqlite3.connect("userdata.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS logindata (
    id INTEGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
)
""")


def new_user(username = str, password = str):
    username_to_enter, password_to_enter = username, hashlib.sha256(password.encode()).hexdigest()
    cur.execute("INSERT INTO logindata (username, password) VALUES (?, ?)", (username_to_enter, password_to_enter))

    cur.execute(f"""
        CREATE TABLE IF NOT EXISTS {username} (
            id INTEGER PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            dose INTEGER NOT NULL,
            time VARCHAR(255) NOT NULL
            )
            """)

# username1, password1 = "frankinside", hashlib.sha256("bolts".encode()).hexdigest()
# username2, password2 = "orpo", hashlib.sha256("poor".encode()).hexdigest()
# username3, password3 = "plaktuk", hashlib.sha256("kultklap".encode()).hexdigest()
# username4, password4 = "pikpluk", hashlib.sha256("toothpik".encode()).hexdigest()
# cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username1, password1))
# cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username2, password2))
# cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username3, password3))
# cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username4, password4))

new_user("frankinside", "bolts")
new_user("orpo", "poor")
new_user("plaktuk", "kultklap")
new_user("pikpluk", "toothpik")

conn.commit()

#can i make table names dynamically? iterating over numbers or something
#can i just encode the password again and check if its the same as the one in the database or is it more complicated than that?
#