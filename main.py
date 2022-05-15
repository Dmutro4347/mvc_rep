import psycopg2 as pg
con = pg.connect(
    database="studio",
    user="postgres",
    password="Int-32768",
    host="127.0.0.1",
    port="5432"
)
cur = con.cursor()
#
#
# with open('course.txt') as course:
#     course_lines = course.readlines()
#     i = 0
#     for course_sql in course_lines:
#         i += 1
#         a = f'''INSERT INTO course(id, name) VALUES
#             ({i}, '{course_sql}')'''
#         cur.execute(a)
#         con.commit()

with open('group_.txt') as group:
    group_lines = group.readlines()
    id_ = 0
    for group_sql in group_lines:
        c = group_sql.split(', ')
        id_ += 1
        q = f'''INSERT INTO group_ VALUES({id_}, '{c[0]}', {c[1]}, {c[2]}, '{c[3]}',{c[4]}, {c[5]})'''
        cur.execute(q)
        con.commit()
#         # print('a', a)
#         # print('c', c)
#
# with open('c:/sql/human.txt') as human:
#     human_lines = human.readlines()
#     for human_sql in human_lines:
#         c = human_sql.split(', ')
        
