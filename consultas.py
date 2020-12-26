#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 10:36:36 2020
@author: noxonsoftwares
"""
import sqlite3


def sql_querry(self, querry, param=()):
    with sqlite3.connect(self.db) as conn:
        cursor = conn.cursor()
        result = cursor.execute(querry, param)
        conn.commit()
        return result
