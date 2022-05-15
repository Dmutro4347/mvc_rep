import psycopg2 as pg


class DataBase:
    def __init__(self, database, password):
        self.con = pg.connect(
            database=database,
            user="postgres",
            password=password,
            host="127.0.0.1",
            port="5432"
        )
        self.cur = self.con.cursor()

    def insert(self, table_name, values, table_columns=''):
        q = f'''INSERT INTO {table_name} {table_columns}VALUES {values}'''
        self.cur.execute(q)
        self.con.commit()
        # print(q)

    def select(self, table_name):
        q = f'''SELECT * FROM {table_name}'''
        # print(q)
        self.cur.execute(q)
        self.con.commit()
        for row in self.cur:
            print(row)

    def update(self, table_name, column, value, id_):
        q = f"""UPDATE {table_name} SET {column} = '{value}' WHERE id = {id_}"""
        self.cur.execute(q)
        self.con.commit()

    def delete(self, table_name, id_):
        q = f'''DELETE FROM {table_name} WHERE id = {id_}'''
        self.cur.execute(q)
        self.con.commit()

    def insert_from_file(self, table_name, file_name):
        if file_name == 'group_.txt':
            with open('group_.txt') as group:
                group_lines = group.readlines()
                id_ = 0
                for group_sql in group_lines:
                    group_split = group_sql.split(', ')
                    id_ += 1
                    self.insert(table_name, f"({id_}, '{group_split[0]}', {group_split[1]}, {group_split[2]}, '{group_split[3]}', {group_split[4]}, {group_split[5]})")
        elif file_name == 'course.txt':
            with open('course.txt') as course:
                course_lines = course.readlines()
                id_ = 0
                for course_sql in course_lines:
                    id_ += 1
                    q = f'''({id_}, '{course_sql}')'''
                    self.insert(table_name, q)
# test