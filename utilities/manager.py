import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('novasieve_dev.db')
c = conn.cursor()

# Execute a SQL command to create a table
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')

# Commit the transaction
conn.commit()
# Close the connection
conn.close()

# # Read Data
# c.execute("SELECT * FROM users")
# rows = c.fetchall()
# for row in rows:
#     print(row)

# # Update Data
# c.execute("UPDATE users SET email = 'new_email@example.com' WHERE id = 1")
# conn.commit()

# # Delete Data
# c.execute("DELETE FROM users WHERE id = 1")
# conn.commit()
