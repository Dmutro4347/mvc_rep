import db_class
import view
file_name = 'course.txt'

db = db_class.DataBase('studio', 'Int-32768')

a = db.last_id('human')
print(a)

