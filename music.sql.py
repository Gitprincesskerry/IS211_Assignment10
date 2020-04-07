# !/usr/bin/env python
# -*- coding: utf-8 -*-
# This is Kerry Rainford's Week 10 Assignment, Part 1

import sqlite3 as kerrydb

con = kerrydb.connect('music.db')
con.text_factory = str

with con:

    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS artistfacts")
    cur.execute("CREATE TABLE artistfacts(id INTEGER PRIMARY KEY ASC, artist_full_name TEXT, nickname TEXT)")


    cur.execute("DROP TABLE IF EXISTS albumfacts")
    cur.execute("CREATE TABLE albumfacts(id INTEGER PRIMARY KEY, artist_full_name TEXT, album_name TEXT)")

    cur.execute("DROP TABLE IF EXISTS songs")
    cur.execute("CREATE TABLE songs(id INTEGER PRIMARY KEY, song_name TEXT, album_name TEXT, track_number INTEGER, song_length TIME, artist_number INTEGER)")
