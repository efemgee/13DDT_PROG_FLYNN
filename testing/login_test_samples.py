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
    
    
#checks the username and passcode against the database
#def check_login_details:
    #take the values input into the entryboxes once the submit button has been pressed, then encode them. see if these encoded versions match the encoded versions already in the database. if they do, run login_to_user().

#puts the program into a state of being logged into one profile
#def login_to_user():
    #if the passcode and username used to attempt a login have matched the database, then this function will be used to open the home page in a state where the profile that was successfully logged into is the current user.

    
#Retrieves prescription table of current user
def retrieve_prescriptions(current_user = str):
    current_prescriptions = cur.execute(f"""SELECT * FROM {current_user} WHERE id >= 0""")
    print(current_prescriptions)
    rows = cur.fetchall()
    
    for row in rows:
        print(row)
        

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

current_user = "frankinside"

retrieve_prescriptions(current_user)

conn.commit()