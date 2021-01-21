from database import Connection


class User:
    def __init__(self, email, f_name, l_name, idx):
        self.email = email
        self.f_name = f_name
        self.l_name = l_name
        self.idx = idx

    def __repr__(self):
        return f"{self.email}"

    def insert_into_db(self):
        with Connection() as cnx:
            with cnx.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO users (email, first_name, last_name) VALUES(%s, %s, %s)",
                    (self.email, self.f_name, self.l_name),
                )

    @classmethod
    def select_from_db_by_email(cls, email):
        with Connection() as cnx:
            with cnx.cursor() as cursor:
                cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
                selected_data = cursor.fetchone()
                return cls(
                    selected_data[0],
                    selected_data[1],
                    selected_data[2],
                    selected_data[3],
                )
