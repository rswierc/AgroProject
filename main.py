import sqlite3
from sys import argv # nie musze pisac sys.argv tylko samo argv(import sys)


#tworzymy połączenie, tworzymy kursor i wywołujemy metodę, zamykamy połączenie
class DataBase:
    def __init__(self, nazwa_bazy): #tworzenie polaczenia i kursora
        self.connection = sqlite3.connect(nazwa_bazy)
        self.cursor = self.connection.cursor()

    def create_table(self, dane):
        self.cursor.execute(dane)
    
    def delete_table(self):
        pass
    
    def __del__(self): #zamykanie polaczenia, wywolywane autowamtycznie kiedy tworzymy obiekt klasy w innej funkcji
        self.connection.close()


    
if len(argv[1]) > 1 and argv[1] == 'create':
    db = DataBase('MyDataBase.db')
    db.create_table("CREATE TABLE movie(title, year, score)")
    print('Create table')


