from psycopg2 import pool

cnx_pool = pool.SimpleConnectionPool(
    1, 1, user="user", database="database", password="password", host="host"
)


class Cursor:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = cnx_pool.getconn()
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val is not None:
            self.connection.rollback()
        else:
            self.cursor.close()
            self.connection.commit()
        cnx_pool.putconn(self.connection)
