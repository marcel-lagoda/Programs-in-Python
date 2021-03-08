from database import Cursor


class User:
    def __init__(self, email, f_name, l_name, idx):
        self.email = email
        self.f_name = f_name
        self.l_name = l_name
        self.idx = idx

    def __repr__(self):
        return f"Personal data for [{self.email}]: {self.f_name} {self.l_name}, id: {self.idx}"

    def insert_into_db(self):
        with Cursor() as cursor:
            cursor.execute(
                "INSERT INTO users (email, first_name, last_name) VALUES(%s, %s, %s)",
                (self.email, self.f_name, self.l_name),
            )

    @classmethod
    def select_from_db_by_email(cls, email):
        with Cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
            selected_data = cursor.fetchone()
            return cls(
                idx=selected_data[0],
                email=selected_data[1],
                f_name=selected_data[2],
                l_name=selected_data[3],
            )
