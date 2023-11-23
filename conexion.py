import sqlite3
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

class conexBD:
    #Se instancia desde la clase Personal.py
    #con y cur
    def __init__ (self):
        self.con=sqlite3.connect(os.path.join(ROOT_DIR, "./DATOS"))
        self.cur=self.con.cursor()
        
    def crearCapacitacion(self):
        query='''create table if not exists capacitacion (
            id integer not null primary key autoincrement,
            nombre varchar(50),
            apellido varchar(50),
            email varchar(50),
            antig varchar(10),
            curso varchar(30),
            modalidad varchar(20))'''
        self.cur.execute(query)
        self.close()

    #aca cierro la conexion y el cursor
    def close(self):
        self.con.commit()
        self.con.close()