from db import connect_db

def add_user(name, email):
    conn = connect_db()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
        conn.commit()
        print("✔ User added successfully")
    except:
        print("✖ Email already exists")
    conn.close()


def get_users():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    data = cur.fetchall()
    conn.close()
    return data


def get_user_name(user_id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT name FROM users WHERE id = %s", (user_id,))
    result = cur.fetchone()
    conn.close()
    return result[0] if result else "Unknown"


def add_connection(u1, u2):
    conn = connect_db()
    cur = conn.cursor()

    # Check if users exist
    cur.execute("SELECT id FROM users WHERE id=%s", (u1,))
    user1 = cur.fetchone()

    cur.execute("SELECT id FROM users WHERE id=%s", (u2,))
    user2 = cur.fetchone()

    if not user1 or not user2:
        print("✖ One or both users do not exist!")
        conn.close()
        return

    try:
        cur.execute("INSERT INTO connections (user_id, connection_id) VALUES (%s, %s)", (u1, u2))
        cur.execute("INSERT INTO connections (user_id, connection_id) VALUES (%s, %s)", (u2, u1))
        conn.commit()
        print("✔ Connection added")
    except:
        print("✖ Connection already exists or error occurred")

    conn.close()


def get_connections():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT user_id, connection_id FROM connections")
    data = cur.fetchall()
    conn.close()
    return data