from connection.Connection import Connection

class Model(Connection):

    def __init__(self, table):
        self._cursor = self.connect()
        self._select = ''
        self._where = ''
        self._table = table

    @property
    def select(self):
        return self._select

    @select.setter
    def select(self, fields):
        self._select = fields

    @property
    def where(self):
        return self._where

    @where.setter
    def where(self, condictions):
        self._where = condictions

    def get(self):
        sql = f"SELECT {self._select} from {self._table}"        
        if (self._where):
            sql += f" WHERE {self._where}"

        #print(sql)
        self._cursor.execute(sql)
        return self._cursor.fetchall()

    def post(self, sql):
        self._cursor.execute(sql)
        self._db_connection.commit()
        
    def createTable(self, sql):
        self._cursor.execute(sql)