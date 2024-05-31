import sqlite3
from ..model.Strategy import Strategy
from ..model.Screener import Screener
from ..model.Ratio import Ratio

# Database Initialization
def init_db():
    with sqlite3.connect('novesieve_dev.db') as conn:
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS strategies(
                strategyId INTEGER PRIMARY KEY,
                name TEXT,
                description TEXT
            )
        ''')
        c.execute('''
            CREATE TABLE IF NOT EXISTS screeners(
                screenerId INTEGER PRIMARY KEY,
                name TEXT,
                description TEXT
            )
        ''')
        c.execute('''
            CREATE TABLE IF NOT EXISTS ratio_attributes(
                ratioId INTEGER PRIMARY KEY,
                strategyId INTEGER,
                ratio_name TEXT,
                ratio_name2 TEXT,
                type TEXT,
                operator TEXT,
                value INTEGER,
                must_match INTEGER
            )
        ''')
        conn.commit()

# Strategy CRUD operations
def insert_strategy(name, description):
    try:
        with sqlite3.connect('novesieve_dev.db') as conn:
            c = conn.cursor()
            c.execute("INSERT INTO strategies (name, description) VALUES (?, ?)", (name, description))
            conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

def get_strategy(id=None):
    try:
        with sqlite3.connect('novesieve_dev.db') as conn:
            c = conn.cursor()
            if id:
                c.execute("SELECT * FROM strategies WHERE strategyId = ?", (id,))
                row = c.fetchone()
                return Strategy(*row) if row else None
            c.execute("SELECT * FROM strategies")
            rows = c.fetchall()
            return [Strategy(*row) for row in rows]
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return []

def update_strategy(id, name, description):
    try:
        with sqlite3.connect('novesieve_dev.db') as conn:
            c = conn.cursor()
            c.execute("UPDATE strategies SET name = ?, description = ? WHERE strategyId = ?", (name, description, id))
            conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

def delete_strategy(id):
    try:
        with sqlite3.connect('novesieve_dev.db') as conn:
            c = conn.cursor()
            c.execute("DELETE FROM strategies WHERE strategyId = ?", (id,))
            conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

# Screener CRUD operations
def insert_screener(name, description):
    try:
        with sqlite3.connect('novesieve_dev.db') as conn:
            c = conn.cursor()
            c.execute("INSERT INTO screeners (name, description) VALUES (?, ?)", (name, description))
            conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

def get_screener(id=None):
    try:
        with sqlite3.connect('novesieve_dev.db') as conn:
            c = conn.cursor()
            if id:
                c.execute("SELECT * FROM screeners WHERE screenerId = ?", (id,))
                row = c.fetchone()
                return Screener(*row) if row else None
            c.execute("SELECT * FROM screeners")
            rows = c.fetchall()
            return [Screener(*row) for row in rows]
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return []

def update_screener(id, name, description):
    try:
        with sqlite3.connect('novesieve_dev.db') as conn:
            c = conn.cursor()
            c.execute("UPDATE screeners SET name = ?, description = ? WHERE screenerId = ?", (name, description, id))
            conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

def delete_screener(id):
    try:
        with sqlite3.connect('novesieve_dev.db') as conn:
            c = conn.cursor()
            c.execute("DELETE FROM screeners WHERE screenerId = ?", (id,))
            conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

# Ratio CRUD operations
def insert_ratio(strategy_id, ratio_name, ratio_name2, type, operator, value, must_match):
    try:
        with sqlite3.connect('novesieve_dev.db') as conn:
            c = conn.cursor()
            c.execute("""
                INSERT INTO ratio_attributes
                (strategyId, ratio_name, ratio_name2, type, operator, value, must_match)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (strategy_id, ratio_name, ratio_name2, type, operator, value, must_match))
            conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

def get_ratio(strategy_id):
    try:
        with sqlite3.connect('novesieve_dev.db') as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM ratio_attributes WHERE strategyId = ?", (strategy_id,))
            rows = c.fetchall()
            return [Ratio(*row) for row in rows]
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return []

def update_ratio(ratio):
    try:
        with sqlite3.connect('novesieve_dev.db') as conn:
            c = conn.cursor()
            c.execute("""
                UPDATE ratio_attributes SET
                ratio_name = ?, ratio_name2 = ?, type = ?, operator = ?, value = ?, must_match = ?
                WHERE ratioId = ?
            """, (ratio.ratio_name, ratio.ratio_name2, ratio.type, ratio.operator, ratio.value, ratio.must_match, ratio.ratio_id))
            conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

def delete_ratio(ratio_id):
    try:
        with sqlite3.connect('novesieve_dev.db') as conn:
            c = conn.cursor()
            c.execute("DELETE FROM ratio_attributes WHERE ratioId = ?", (ratio_id,))
            conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

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
