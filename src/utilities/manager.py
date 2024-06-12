import sqlite3
from backend_api import analysis_options_reverse, novasieve
from datetime import datetime
from ..model.Strategy import Strategy
from ..model.Screener import Screener
from ..model.Ratio import Ratio
from ..model.Pattern import Pattern

# Execute a SQL command to create a table
def init_db():
    with sqlite3.connect('novesieve_dev.db') as conn:
            conn.execute("PRAGMA foreign_keys = 1")
            c = conn.cursor()
            c.execute('''
                      CREATE TABLE IF NOT EXISTS screener(
                          screenerId INTEGER PRIMARY KEY,
                          name TEXT,
                          description TEXT
                          )
                ''')
            
            c.execute('''
                      CREATE TABLE IF NOT EXISTS strategies(
                          strategyId INTEGER PRIMARY KEY,
                          name TEXT,
                          description TEXT,
                          screenerId INTEGER,
                          trading TEXT,
                          stopLoss TEXT,
                          FOREIGN KEY (screenerId) REFERENCES screener(screenerId) ON DELETE CASCADE
                          
                          
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
                          MUST_MATCH INTEGER,
                          FOREIGN KEY (screenerId) REFERENCES screener(screenerId) ON DELETE CASCADE
                          
                          )
            ''')
            c.execute('''
                      CREATE TABLE IF NOT EXISTS pattern_rules(
                          patternId INTEGER PRIMARY KEY,
                          screenerId INTEGER,
                          name TEXT,
                          MUST_MATCH INTEGER,
                          FOREIGN KEY (screenerId) REFERENCES screener(screenerId) ON DELETE CASCADE
                          
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
    
def get_strategy_dictionary():
    with sqlite3.connect('novesieve_dev.db') as conn:
        c = conn.cursor()
        c.execute("SELECT strategyId, name from strategies")
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
        conn.execute("PRAGMA foreign_keys = 1")
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



def update_pattern(pattern_id, name, must_match):
    data = (name,  must_match, pattern_id)
    with sqlite3.connect('novesieve_dev.db') as conn:
        c = conn.cursor()
        c.execute("""
                  UPDATE
                  pattern_rules
                  SET
                  name= ?,
                  must_match = ?
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
        pattern = Pattern(row[0], row[1], row[2], row[3])
        patterns.append(pattern)
    
    return patterns

def insert_pattern(screener_id, must_match, name="Basic Pattern Rule"):
    data = (screener_id, name, must_match)
    with sqlite3.connect('novesieve_dev.db') as conn:
        c = conn.cursor()
        c.execute(f"""
                    INSERT INTO
                    pattern_rules
                    (screenerId, name, MUST_MATCH)
                    VALUES
                    (?, ?, ?)
                    """, data)
        conn.commit()
        
def delete_pattern(pattern_id):
    with sqlite3.connect('novesieve_dev.db') as conn:
        c = conn.cursor()
        c.execute(f"DELETE FROM pattern_rules WHERE patternId = {pattern_id}")
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
        
def get_backtest_payload(strategy_id):
    with sqlite3.connect('novesieve_dev.db') as conn:
        c = conn.cursor()
        if id:
            c.execute(f"SELECT * FROM strategies WHERE strategyId = {strategy_id}")
            data = Strategy(c.fetchone())
    variables, rules = get_screening_payload(data.screenerId)
    
    return variables, rules
    
        
def get_backtest_result(strategy_id, symbols, start_time, end_time, variables, rules, trading_style, stoploss):
    variables, rules = get_backtest_payload(strategy_id=strategy_id)
    
    backtest_result = novasieve.screener.backtest(
        symbols=["CLEO.JK", "MEDC.JK", "BREN.JK", "TPIA.JK", "NCKL.JK", "MBMA.JK", "BMRI.JK", "BBRI.JK", "BBCA.JK", "TLKM.JK"], 
        start_time_period = start_time,
        end_time_period = end_time,
        variables=variables,
        rules=rules,
        trading_style = trading_style,
        stoploss=stoploss,
    )
    
    return backtest_result
    

def get_screening_payload(id):
    vars, rules = [], []
    technicals = get_technical(id)
    funds = get_fundamental(id)
    patterns = get_pattern(id)
    
    n_count = 0
    for pattern in patterns:
        pattern: Pattern = pattern

        pattern_cat = novasieve.screener.check_analysis_method_category("technical", pattern.name)
        if pattern_cat is None:
            continue

        var_ = {
            "var_id": f"ta-{n_count}",
            "type": "technical",
            "analysis_type": pattern_cat,
            "name": pattern.name,
            "params": None
        }
        rule_ = {
            "type": "binary", 
            "var_id": f"ta-{n_count}",
            "var_output": None,
            "optional": not pattern.must_match,
            "must_not_occur": False,
        }
        vars.append(var_)
        rules.append(rule_)
        n_count += 1
    
    for technical in technicals:
        tech:Ratio = technical
        tech.ratio = analysis_options_reverse["technical"].get(tech.ratio)
        tech.ratio2 = analysis_options_reverse["technical"].get(tech.ratio2)

        tech1_cat = novasieve.screener.check_analysis_method_category("technical", tech.ratio)
        tech2_cat = novasieve.screener.check_analysis_method_category("technical", tech.ratio2)
        if tech1_cat is None:
            continue

        var1_ = {
            "var_id": f"ta-{n_count}",
            "type": "technical",
            "analysis_type": tech1_cat,
            "name": tech.ratio,
            "params": {
                "price": "Close"
            }
        }
        vars.append(var1_)

        if tech2_cat is not None:
            var2_ = {
                "var_id": f"ta-{n_count+1}",
                "type": "technical",
                "analysis_type": tech2_cat,
                "name": tech.ratio2,
                "params": {
                    "price": "Close"
                }
            }
            vars.append(var2_)

        rule_ = {
            "type": "continuous", 
            "var_id": f"ta-{n_count}",
            "var_output": None,
            "operator": tech.operator,
            "var2_multiplier": tech.value,
            "var2_id": None if tech2_cat is None else f"ta-{n_count+1}",
            "var2_output": None,
            "optional": not tech.must_match,
        }
        rules.append(rule_)
        n_count += 1 + (tech2_cat is not None)
        
    
    for fund in funds:
        fund: Ratio = fund
        fund.ratio = analysis_options_reverse["fundamental"].get(fund.ratio)
        fund.ratio2 = analysis_options_reverse["fundamental"].get(fund.ratio2)
        
        
        fund1_cat = novasieve.screener.check_analysis_method_category("fundamental", fund.ratio)
        fund2_cat = novasieve.screener.check_analysis_method_category("fundamental", fund.ratio2)
        if fund1_cat is None:
            continue

        var1_ = {
            "var_id": f"fa-{n_count}",
            "type": "fundamental",
            "analysis_type": fund1_cat,
            "name": fund.ratio,
            "params": {
                "price": "Close"
            }
        }
        vars.append(var1_)

        if fund2_cat is not None:
            var2_ = {
                "var_id": f"fa-{n_count+1}",
                "type": "fundamental",
                "analysis_type": fund2_cat,
                "name": fund.ratio2,
                "params": {
                    "price": "Close"
                }
            }
            vars.append(var2_)

        rule_ = {
            "type": "continuous", 
            "var_id": f"fa-{n_count}",
            "var_output": None,
            "operator": fund.operator,
            "var2_multiplier": fund.value,
            "var2_id": None if fund2_cat is None else f"fa-{n_count+1}",
            "var2_output": None,
            "optional": not fund.must_match,
        }
        rules.append(rule_)
        n_count += 1 + (fund2_cat is not None)
    
    return vars, rules

def get_screening_result(screenerId, selected_stocks, date):
    variables, rules = get_screening_payload(screenerId)
    
    print("Something")
    screen_result = novasieve.screener.screen(
        symbols=selected_stocks, 
        time_period=str(date)   ,
        variables=variables,
        rules=rules
    )
    print(screen_result)
    return screen_result
        
        
    
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