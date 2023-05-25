import sqlite3

def create_recipe_table():
    conn = sqlite3.connect('recipes.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS recipes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            label TEXT,
            ingredients TEXT,
            url TEXT
        )
    ''')

    conn.commit()
    conn.close()

create_recipe_table()
