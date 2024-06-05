import sqlite3
from ..model.Strategy import Strategy
from ..model.Screener import Screener
from ..model.Ratio import Ratio

# Execute a SQL command to create a table
def init_db():
    with sqlite3.connect('novesieve_dev.db') as conn:
            c = conn.cursor()
            c.execute('''
                      CREATE TABLE IF NOT EXISTS strategies(
                          strategyId INTEGER PRIMARY KEY,
                          name TEXT,
                          description TEXT,
                          screenerId INTEGER,
                          trading TEXT,
                          stopLoss TEXT
                          
                          )
                ''')
            c.execute('''
                      CREATE TABLE IF NOT EXISTS screener(
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
                          value REAL,
                          MUST_MATCH INTEGER
                    )
            ''')
            conn.commit()

def update_strategy(name, desc, id, screenerId, trading, stopLoss):
    # return
    with sqlite3.connect('novesieve_dev.db') as conn:
        c = conn.cursor()
        c.execute("UPDATE strategies SET name = ?, description = ?, screenerId = ?, trading = ?, stopLoss = ? WHERE strategyId = ?", 
                  (name, desc, id, screenerId, trading, stopLoss))
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
        strategy = Strategy(row[0], row[1], row[2], row[3], row[4], row[5])
        strategies.append(strategy)
    
    return strategies

def get_screener_dictionary():
    with sqlite3.connect('novesieve_dev.db') as conn:
        c = conn.cursor()
        c.execute("SELECT screenerId, name from screener")
        data = c.fetchall()
    dictionary = {} 

    for row in data:
        dictionary[row[0]] = row[1]
    return dictionary
        

def insert_screener():
    default_data = ("default_strategy", "This is desc")
    with sqlite3.connect('novesieve_dev.db') as conn:
        c = conn.cursor()
        c.execute("INSERT INTO screener (name, description) VALUES (?, ?)", default_data)
        conn.commit()

# def insert_new_screener():
#     default_data = ("default_strategy", "This is desc")
#     with sqlite3.connect('novesieve_dev.db') as conn:
#         c = conn.cursor()
#         c.execute("INSERT INTO strategies (name, description) VALUES (?, ?)", default_data)
#         conn.commit()
    
def delete_screener(screener_id):
    with sqlite3.connect('novesieve_dev.db') as conn:
        c = conn.cursor()
        c.execute(f"DELETE FROM screener WHERE screenerId = {screener_id}")
        conn.commit()

def get_screener(id=None):
    with sqlite3.connect('novesieve_dev.db') as conn:
        c = conn.cursor()
        if id:
            c.execute(f"SELECT * from screener WHERE screenerId = {id}")
            data = c.fetchone()
            return data
        c.execute(f"SELECT * FROM screener")
        data = c.fetchall()
    
    screeners = []

    for row in data:
        strategy = Screener(row[0], row[1], row[2])
        screeners.append(strategy)
        
    return screeners

def update_screener(name, desc, id):
    # return
    with sqlite3.connect('novesieve_dev.db') as conn:
        c = conn.cursor()
        c.execute("UPDATE screener SET name = ?, description = ? WHERE screenerId = ?", (name, desc, id))
        conn.commit()

def insert_ratio(strategy_id, type, ratio="<select>",ratio2="<select>", operator="=", value=0, must_match=0):
    data = (strategy_id, ratio, ratio2, type, operator, value, must_match)
    with sqlite3.connect('novesieve_dev.db') as conn:
        c = conn.cursor()
        c.execute("""
                  INSERT INTO 
                  ratio_attributes
                  (strategyId, ratio_name, ratio_name2, type, operator, value, must_match)
                  VALUES
                  (?, ?, ?, ? ,?, ?, ?)
                  """
                  , data)
        conn.commit()

def get_ratio(strategy_id):
    with sqlite3.connect('novesieve_dev.db') as conn:
        c = conn.cursor()
        if id:
            c.execute(f"SELECT * from ratio_attributes WHERE strategyId = {strategy_id}")
            data = c.fetchall()
    
    ratios = []

    for row in data:
        ratio = Ratio(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
        ratios.append(ratio)
    
    return ratios

def delete_ratio(ratio_id):
    with sqlite3.connect('novesieve_dev.db') as conn:
        c = conn.cursor()
        c.execute(f"DELETE FROM ratio_attributes WHERE ratioId = {ratio_id}")
        conn.commit()

def update_ratio(ratio:Ratio):
    with sqlite3.connect('novesieve_dev.db') as conn:
        c = conn.cursor()
        c.execute("""
                  UPDATE
                  ratio_attributes
                  SET
                  ratio_name = ?,
                  ratio_name2 = ?,
                  operator = ?,
                  value = ?,
                  must_match = ?
                  WHERE ratioId = ?
                  """, (ratio.ratio, ratio.ratio2, ratio.operator, ratio.value, ratio.must_match, ratio.ratio_id))
        conn.commit()

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