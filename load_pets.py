# !/usr/bin/env python
# -*- coding: utf-8 -*-
# This is Kerry Rainford's Week 10 Assignment, Part 2.0

import sqlite3 as kerrydb

person = (
    (1,'James','Smith',41),
    (2,'Diana','Greene',23),
    (3,'Sara','White',27),
    (4,'William','Gibson',23)
    )

pet = (
    (1,'Rusty','Dalmation',4,1),
    (2,'Bella','AlaskanMalamute',3,0),
    (3,'Max','CockerSpaniel',1,0),
    (4,'Rocky','Beagle',7,0),
    (5,'Rufus','CockerSpaniel',1,0),
    (6,'Spot','Bloodhound',2,1)
    )

person_pet = (
    (1,1),
    (1,2),
    (2,3),
    (2,4),
    (3,5),
    (4,6)
    )

con = kerrydb.connect('pets.db')

with con:

    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS person")
    cur.execute("CREATE TABLE person(id INTEGER PRIMARYKEY, first_name TEXT, last_name TEXT, age INTEGER)")
    cur.executemany("INSERT INTO person VALUES(?, ?, ?, ?)", person)


    cur.execute("DROP TABLE IF EXISTS pet")
    cur.execute("CREATE TABLE pet(id INTEGER PRIMARYKEY, name TEXT, breed TEXT, age INTEGER, dead INTEGER)")
    cur.executemany("INSERT INTO pet VALUES(?, ?, ?, ?, ?)", pet)


    cur.execute("DROP TABLE IF EXISTS person_pet")
    cur.execute("CREATE TABLE person_pet(person_id INTEGER, pet_id INTEGER)")
    cur.executemany("INSERT INTO person_pet VALUES(?, ?)", person_pet)

# Question 2 Answer: The person of the person_pet table is to establish a connection between the person table to the pet table
