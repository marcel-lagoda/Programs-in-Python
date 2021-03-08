from database import Database
from user import User

Database.initialise(
    database="learning", host="localhost", password="postgres", user="postgres"
)

user = User("AangL@gmail.com", "Aang", "Luftbändiger", None)
# user.insert_into_db()
user_from_db = User.select_from_db_by_email("AangL@gmail.com")
print(user_from_db)
