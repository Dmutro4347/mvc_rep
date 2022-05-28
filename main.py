import db_class
import view
file_name = 'course.txt'

db = db_class.DataBase('studio', 'Int-32768')

db.insert_from_file('human.txt', 'human')