import sqlite3

database = sqlite3.connect('database.db')
cursor = database.cursor()
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS products (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     title CHAR(50),
#     price FLOAT,
#     description CHAR(100),
#     category CHAR(50),
#     image CHAR(100),
#     rate FLOAT,
#     count INTEGER
# );
# """)

# =============================================================================

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS products_1 (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     title CHAR(50),
#     price FLOAT,
#     description CHAR(100),
#     category CHAR(50),
#     image CHAR(100),
#     rate FLOAT,
#     count INTEGER
# );
# """)

# =======================================================================
#
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS categories (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     title CHAR(50),
#     price FLOAT,
#     description CHAR(100),
#     category CHAR(50),
#     image TEXT,
#     rate FLOAT,
#     count INTEGER
# );
# """)



# =========================================================================
