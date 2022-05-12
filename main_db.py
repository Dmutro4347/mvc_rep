import db_class
import view

file_name = 'course.txt'

db = db_class.DataBase('studio', 'Int-32768')
menu = view.View()
# db.insert_from_file('group_', 'group_.txt')
answer = menu.main_menu()
if answer == 1:
    answer = menu.db_menu(file_name)
    if answer == 1:
        values = menu.insert_menu()
        db.insert(values[0], values[1], values[2])
    elif answer == 2:
        value = menu.select_menu()
        db.select(value)
    elif answer == 3:
        values = menu.update_menu()
        db.update(values[0], values[1], values[2], values[3])
    elif answer == 4:
        values = menu.delete_menu()
        db.delete(values[0], values[1])
    else:
        values = menu.insert_from_file_menu()
        db.insert_from_file(values[0], values[1])
elif answer == 2:
    

else:
    pass
