"""
Script: query_pets.py
Queries the pets.db database interactively by person ID.
"""

import sqlite3

def query_database():
    conn = sqlite3.connect('pets.db')
    cursor = conn.cursor()

    while True:
        try:
            user_input = input("Enter an ID number (-1 to exit): ")
            person_id = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid integer ID.")
            continue

        if person_id == -1:
            print("Exiting program. Goodbye!")
            break

        # Query person info
        cursor.execute("SELECT first_name, last_name, age FROM person WHERE id = ?", (person_id,))
        person = cursor.fetchone()

        if not person:
            print(f"Error: No person found with ID {person_id}.")
            continue

        first_name, last_name, age = person
        print(f"{first_name} {last_name}, {age} years old")

        # Query pets owned by the person
        cursor.execute('''
            SELECT p.name, p.breed, p.age, p.dead 
            FROM pet p
            JOIN person_pet pp ON p.id = pp.pet_id
            WHERE pp.person_id = ?
        ''', (person_id,))
        
        pets = cursor.fetchall()

        if not pets:
            print(f"{first_name} {last_name} currently owns no pets.")
        else:
            for pet in pets:
                pet_name, breed, pet_age, dead = pet
                status = "passed away"
                if dead == 0:
                    status = "is alive"
                print(f"{first_name} {last_name} owned {pet_name}, a {breed}, that was {pet_age} years old ({status})")

    conn.close()

if __name__ == '__main__':
    query_database()
