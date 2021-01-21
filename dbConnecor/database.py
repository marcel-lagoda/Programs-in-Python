from psycopg2 import pool

cnx_pool = pool.SimpleConnectionPool(
    1, 1, user="user", database="database", password="password", host="host"
)


class Connection:
    def __init__(self):
        self.connection = None

    def __enter__(self):
        self.connection = cnx_pool.getconn()
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        cnx_pool.putconn(self.connection)
