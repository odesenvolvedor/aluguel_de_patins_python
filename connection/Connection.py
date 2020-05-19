import sqlite3

class Connection:
    
    def connect(self):
        try:
            self._db_connection = sqlite3.connect('aluguel_de_patins.db')

            print("Conexão estabelecida com sucesso!")

            return self._db_connection.cursor()

        except sqlite3.Error as error:

            print(error)

    def close(self):
        self._db_connection.close()