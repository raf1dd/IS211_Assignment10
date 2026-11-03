"""
Script: load_pets.py
Loads initial data into the pets.db SQLite database.
"""

import sqlite3

def load_data():
    conn = sqlite3.connect('pets.db')
    cursor = conn.cursor()

    # Create tables
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS person (
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        age INTEGER
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS pet (
        id INTEGER PRIMARY KEY,
        name TEXT,
        breed TEXT,
        age INTEGER,
        dead INTEGER
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS person_pet (
        person_id INTEGER,
        pet_id INTEGER
    );
    ''')

    # Insert Data
    persons = [
        (1, 'James', 'Smith', 41),
        (2, 'Diana', 'Greene', 23),
        (3, 'Sara', 'White', 27),
        (4, 'William', 'Gibson', 23)
    ]

    pets = [
        (1, 'Rusty', 'Dalmatian', 4, 1),
        (2, 'Bella', 'Alaskan Malamute', 3, 0),
        (3, 'Max', 'Cocker Spaniel', 1, 0),
        (4, 'Rocky', 'Beagle', 7, 0),
        (5, 'Rufus', 'Cocker Spaniel', 1, 0),
        (6, 'Spot', 'Bloodhound', 2, 1)
    ]

    person_pets = [
        (1, 1),
        (1, 2),
        (2, 3),
        (2, 4),
        (3, 5),
        (4, 6)
    ]

    cursor.executemany("INSERT OR REPLACE INTO person VALUES (?, ?, ?, ?)", persons)
    cursor.executemany("INSERT OR REPLACE INTO pet VALUES (?, ?, ?, ?, ?)", pets)
    cursor.executemany("INSERT OR REPLACE INTO person_pet VALUES (?, ?)", person_pets)

    conn.commit()
    conn.close()
    print("Database pets.db successfully loaded with data.")

if __name__ == '__main__':
    load_data()
