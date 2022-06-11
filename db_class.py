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

    def last_id(self, table):
        q = f'''SELECT max(id) FROM human'''
        # print(q)
        self.cur.execute(q)
        self.con.commit()
        return self.cur.fetchone()[0]

    def insert(self, table_name, values, table_columns=''):
        if table_columns:
            table_columns = '(' + table_columns + ')'
        id_ = self.last_id(table_name)
        q = f'''INSERT INTO {table_name} {table_columns}VALUES ({id_+ 1}, {values})'''
        print(q)
        self.cur.execute(q)
        self.con.commit()

    def insert_from_file(self, file_name, table_name):

        with open(file_name) as fl:
            id_ = 0
            if file_name == 'group_.txt':
                for group_line in fl:
                    group_line = group_line.replace('\n', '')
                    group_line = group_line.replace('\t', '')
                    group_split = group_line.split(', ')
                    self.insert(table_name, f"'{group_split[0]}', {group_split[1]}, {group_split[2]}, '{group_split[3]}', {group_split[4]}, {group_split[5]}")
            elif file_name == 'course.txt':
                for course_line in fl:
                    course_line = course_line.replace('\n', '')
                    course_line = course_line.replace('\t', '')
                    id_ += 1
                    self.insert(table_name, f"({id_}, '{course_line}')")

            elif file_name == 'human.txt':
                for human_line in fl:
                    human_line = human_line.replace('\n', '')
                    human_line = human_line.replace('\t', '')
                    human_line = human_line.split(', ')
                    id_ += 1
                    try:
                        if human_line[2] == 'None':
                            self.insert(table_name, f"'{human_line[0]}', '{human_line[1]}', '{human_line[2]}', '{human_line[3]}'")

                        elif human_line[2][2] == '.':
                            self.insert(table_name, f"'{human_line[0]}', '{human_line[1]}', 'None', '{human_line[2]}'")
                        else:
                            self.insert(table_name, f"'{human_line[0]}', '{human_line[1]}', '{human_line[2]}', '{human_line[3]}'")
                    except Exception as _ex:
                        self.insert(table_name, f"'{human_line[0]}', '{human_line[1]}', 'None', null")


# test
