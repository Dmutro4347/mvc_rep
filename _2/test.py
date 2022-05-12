import psycopg2 as pg


with open('d:\_Arduino\_sql\course.txt', 'r') as course:
    course_sql = course.read()
    print(course_sql)

with open('d:\_Arduino\_sql\group_.txt', 'r') as group:
    group_sql = group.read()

with open('d:\_Arduino\_sql\human.txt', 'r') as human:
    human_sql = human.read()

