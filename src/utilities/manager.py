import sqlite3
from ..model.Strategy import Strategy
from ..model.Screener import Screener
from ..model.Ratio import Ratio
from ..model.Pattern import Pattern

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
                          screenerId INTEGER,
                          ratio_name TEXT,
                          ratio_name2 TEXT,
                          type TEXT,
                          category TEXT,
                          operator TEXT,
                          value REAL,
                          MUST_MATCH INTEGER
                    )
            ''')
            c.execute('''
                      CREATE TABLE IF NOT EXISTS pattern_rules(
                          patternId INTEGER PRIMARY KEY,
                          screenerId INTEGER,
                          name TEXT
                    )
            ''')
            conn.commit()

def update_strategy(name, desc, id, screenerId, trading, stopLoss):
    with sqlite3.connect('novesieve_dev.db') as conn:
        c = conn.cursor()
        c.execute("UPDATE strategies SET name = ?, description = ?, screenerId = ?, trading = ?, stopLoss = ? WHERE strategyId = ?", 
                  (name, desc, screenerId, trading, stopLoss, id))
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
    

def update_screener(name, desc, id):
    with sqlite3.connect('novesieve_dev.db') as conn:
        c = conn.cursor()
        c.execute("UPDATE screener SET name = ?, description = ? WHERE screenerId = ?", (name, desc, id))
        conn.commit()

def insert_screener():
    default_data = ("default_screener", "This is desc")
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

def update_pattern(pattern_id, name):
    data = (name, pattern_id)
    with sqlite3.connect('novesieve_dev.db') as conn:
        c = conn.cursor()
        c.execute("""
                  UPDATE
                  pattern_rules
                  SET
                  name= ?
                  WHERE patternId = ?
                  """, data)
        conn.commit()

def get_pattern(screener_id):
    with sqlite3.connect('novesieve_dev.db') as conn:
        c = conn.cursor()
        if id:
            c.execute(f"""
                      SELECT * FROM pattern_rules WHERE screenerId = {screener_id}
                      """)
            data = c.fetchall()
    
    patterns = []

    for row in data:
        pattern = Pattern(row[0], row[1], row[2])
        patterns.append(pattern)
    
    return patterns

def insert_pattern(screener_id, name="Basic Pattern Rule"):
    data = (screener_id, name)
    with sqlite3.connect('novesieve_dev.db') as conn:
        c = conn.cursor()
        if id:
            c.execute(f"""
                      INSERT INTO
                      pattern_rules
                      (screenerId, name)
                      VALUES
                      (?, ?)
                      """, data)
            conn.commit()

def insert_ratio(screener_id, type, category, ratio="<select>",ratio2="<select>", operator="=", value=0, must_match=0):
    data = (screener_id, ratio, ratio2, type, category, operator, value, must_match)
    with sqlite3.connect('novesieve_dev.db') as conn:
        c = conn.cursor()
        c.execute("""
                  INSERT INTO 
                  ratio_attributes
                  (screenerId, ratio_name, ratio_name2, type, category, operator, value, must_match)
                  VALUES
                  (?, ?, ?, ? ,?, ?, ?, ?)
                  """
                  , data)
        conn.commit()

def get_fundamental(screener_id):
    with sqlite3.connect('novesieve_dev.db') as conn:
        c = conn.cursor()
        if id:
            c.execute(f"SELECT * FROM ratio_attributes WHERE screenerId = {screener_id} AND category = 'fundamental'")
            data = c.fetchall()
    
    ratios = []

    for row in data:
        ratio = Ratio(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
        ratios.append(ratio)
    
    return ratios

def get_technical(screener_id):
    with sqlite3.connect('novesieve_dev.db') as conn:
        c = conn.cursor()
        if id:
            c.execute(f"SELECT * FROM ratio_attributes WHERE screenerId = {screener_id} AND category = 'technical'")
            data = c.fetchall()
    
    ratios = []

    for row in data:
        ratio = Ratio(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
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

def get_screening_result(id):
    rules = []
    technicals = get_technical(id)
    funds = get_fundamental(id)
    patterns = get_pattern(id)
    
    for pattern in patterns:
        pattern:Pattern = pattern
        item = {}
        item["type"] = "binary"
        item["id"] = pattern.name
        rules.append(item)
    
    for technical in technicals:
        tech:Ratio = technical
        item = {}
        item["type"] = "Technical"
        item["first-id"] = tech.ratio
        item["operator"] = tech.operator
        if (tech.category == 'versus'):
            item["second-id"] = tech.ratio2
            item["second-multiplier"] = tech.value
        rules.append(item)
    
    for fund in funds:
        fund:Ratio = fund
        item = {}
        item["type"] = "Technical"
        item["first-id"] = fund.ratio
        item["operator"] = fund.operator
        if (tech.category == 'versus'):
            item["second-id"] = fund.ratio2
            item["second-multiplier"] = fund.value
        rules.append(item)
    
    print(rules)
    
    return
        
        
        
    
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