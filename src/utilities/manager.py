import sqlite3
from ..model.Strategy import Strategy

# Execute a SQL command to create a table
def init_db():
    with sqlite3.connect('novesieve_dev.db') as conn:
            c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS strategies
                (strategyId INTEGER PRIMARY KEY, name TEXT, description TEXT)''')
            conn.commit()


def update_strategy(name, desc, id):
    return
    with sqlite3.connect('novesieve_dev.db') as conn:
        c = conn.cursor()
        c.execute("UPDATE strategies SET name = ?, description = ? WHERE strategyId = ?", (name, desc, id))
        conn.commit()

def insert_new_strategy():
    default_data = ("default_strategy", "This is desc")
    with sqlite3.connect('novesieve_dev.db') as conn:
        c = conn.cursor()
        c.execute("INSERT INTO strategies (name, description) VALUES (?, ?)", default_data)
        conn.commit()
    
def delete_strategy(strategy_id):
    with sqlite3.connect('novesieve_dev.db') as conn:
        c = conn.cursor()
        c.execute(f"DELETE FROM strategies WHERE strategyId = {strategy_id}")
        conn.commit()

def get_strategies(id=None):
    with sqlite3.connect('novesieve_dev.db') as conn:
        c = conn.cursor()
        if id:
            c.execute(f"Select * from strategies WHERE strategyId = {id}")
            data = c.fetchone()
            return data
        c.execute(f"SELECT * FROM strategies")
        data = c.fetchall()
    
    strategies = []

    for row in data:
        strategy = Strategy(row[0], row[1], row[2])
        strategies.append(strategy)
    
    return strategies

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
