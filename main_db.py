import db_class
import view
file_name = 'course.txt'

db = db_class.DataBase('studio', 'Int-32768')
menu = view.View()
# db.insert_from_file('group_', 'group_.txt')
answer = menu.main_menu()

if answer == '1':
    # DB
    answer = menu.db_menu(file_name)

    if answer == '1':
        # select
        table_name = menu.select_menu()
        db.select(table_name)
    elif answer == '2':
        # insert
        answer = menu.new_menu()
        if answer == '1':
            # human
            value = menu.new_human()
            db.insert('human', f"'{value[0]}', '{value[1]}', '{value[2]}', '{value[3]}'")
        elif answer == '2':
            # group
            value = menu.new_group()
        else:
            # course
            pass

    elif answer == '3':
        # update

        values = menu.update_menu()
        db.update(values[0], values[1], values[2], values[3])
    elif answer == '4':
        # delete

        values = menu.delete_menu()
        db.delete(values[0], values[1])

    elif answer == '5':
        # new student
        answer = menu.new_student()
        student = answer[0].split(', ')
        parent = answer[1].split(', ')
        id_ = answer[2]
        print(student, parent,  id_)

    else:
        # insert from file

        values = menu.insert_from_file_menu()
        db.insert_from_file(values, values + '.txt')
elif answer == '2':
    pass
else:
    pass
