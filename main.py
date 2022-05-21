import db_class
db = db_class.DataBase('studio', 'Int-32768')
db.insert_from_file('human.txt', 'human')

