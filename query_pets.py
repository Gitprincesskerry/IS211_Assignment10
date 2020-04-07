# !/usr/bin/env python
# -*- coding: utf-8 -*-
# This is Kerry Rainford's Week 10 Assignment, Part2.1

import sqlite3 as kerrydb

con = kerrydb.connect('pets.db')
con.text_factory = str

with con:

    cur = con.cursor()

userinput = 0
while userinput != -1:
    userinput = int(raw_input("Please enter the person ID for the record you're attempting to locate."))
    if userinput == -1:
        exit()
    try:
        cur.execute('''SELECT first_name, last_name, age FROM person WHERE id=?''', (userinput,))
        user = cur.fetchone()
        print("Owner Name: %s %s, Owner Age %d." %(user[0],user[1], int(user[2])))

        cur.execute('''SELECT pet_id FROM person_pet WHERE person_id=?''', (userinput,))
        pets = cur.fetchall()

        for x in pets:
            cur.execute('''SELECT name, breed, age FROM pet WHERE id=?''', (x))
            pet = cur.fetchone()
            print("Dog name: %s, Breed: %s, Dog Age: %d."%(pet[0], pet[1], int(pet[2])))
    except:
        print("Person ID doesn't exist. Please enter the person ID for the record you're attempting to locate.")
