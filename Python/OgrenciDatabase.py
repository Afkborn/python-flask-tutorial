
from os import getcwd
import sqlite3 as sql # sqlite3 is a module

from Python.Model.Ogrenci import Ogrenci
CREATETABLE_OGRENCILER = """CREATE TABLE IF NOT EXISTS ogrenciler (id	INTEGER PRIMARY KEY,name TEXT NOT NULL,surname TEXT NOT NULL,age INTEGER NOT NULL,tc_kimlik_no INTEGER NOT NULL)"""

class Database():
    dbName = "okul.db"
    dbLoc = fr"{getcwd()}\Databases\{dbName}"
    
    def __init__(self) -> None:
        self.createDB()
    
            
    def createDB(self):
        self.db = sql.connect(self.dbLoc)
        self.im = self.db.cursor()
        self.im.execute(CREATETABLE_OGRENCILER)
        self.db.commit()
        self.db.close()


    def addOgrenci(self,ogrenci:Ogrenci):
        self.db = sql.connect(self.dbLoc)
        self.im = self.db.cursor()
        KEY = f"name,surname,age,tc_kimlik_no"
        VALUES = f"""
        '{ogrenci.getName()}',
        '{ogrenci.getSurname()}',
        '{ogrenci.getAge()}',
        '{ogrenci.getTcKimlikNo()}'
        """
        self.im.execute(f"INSERT INTO ogrenciler({KEY}) VALUES({VALUES})")
        ogrenci.setID(self.im.lastrowid)
        self.db.commit()
        self.db.close()
        
    def addOgrenciIfNotExists(self,ogrenci:Ogrenci):
        self.db = sql.connect(self.dbLoc)
        self.im = self.db.cursor()
        self.im.execute(f"SELECT * FROM ogrenciler WHERE tc_kimlik_no = {ogrenci.getTcKimlikNo()}")
        result = self.im.fetchone()
        if result != None:
            return False
        self.addOgrenci(ogrenci)
        self.db.close()
        
    def getOgrenci_ID(self,id:int) -> Ogrenci:
        self.db = sql.connect(self.dbLoc)
        self.im = self.db.cursor()
        self.im.execute(f"SELECT * FROM ogrenciler WHERE id = {id}")
        result = self.im.fetchone()
        if result == None:
            return None
        id, name, surname, age, tc_kimlik_no = result
        ogrenciObj = Ogrenci(id,name,surname,age,tc_kimlik_no)
        self.db.close()
        return ogrenciObj

    def getOgrenci_TcKimlikNo(self,tc_kimlik_no:int) -> Ogrenci:
        self.db = sql.connect(self.dbLoc)
        self.im = self.db.cursor()
        self.im.execute(f"SELECT * FROM ogrenciler WHERE tc_kimlik_no = {tc_kimlik_no}")
        result = self.im.fetchone()
        id, name, surname, age, tc_kimlik_no = result
        ogrenciObj = Ogrenci(id,name,surname,age,tc_kimlik_no)
        self.db.close()
        return ogrenciObj
    
    
    def getOgrenciler(self) -> list[Ogrenci]:
        self.db = sql.connect(self.dbLoc)
        self.im = self.db.cursor()
        self.im.execute("SELECT * FROM ogrenciler")
        result = self.im.fetchall()
        ogrenciler = []
        for row in result:
            id, name, surname, age, tc_kimlik_no = row
            ogrenciObj = Ogrenci(id,name,surname,age,tc_kimlik_no)
            ogrenciler.append(ogrenciObj)
        self.db.close()
        return ogrenciler
    

    