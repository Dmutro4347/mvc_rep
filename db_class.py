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
        if table_columns:
            table_columns = '(' + table_columns + ')'
        q = f'''INSERT INTO {table_name} {table_columns}VALUES {values}'''
        # self.cur.execute(q)
        # self.con.commit()
        print(q)

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

    def insert_from_file(self, file_name, table_name):
            with open(file_name) as fl:
                id_ = 0
                if file_name == 'group_.txt':
                    for fl_line in fl:
                        fl_split = fl_line.split(', ')
                        id_ += 1
                        self.insert(table_name, f"({id_}, '{fl_split[0]}', {fl_split[1]}, {fl_split[2]}, '{fl_split[3]}', {fl_split[4]}, {fl_split[5]})")
                elif file_name == 'course.txt':
                    for fl_line in fl:
                        id_ += 1
                        self.insert(table_name, f"({id_}, '{fl_line}')")

                elif file_name == 'human.txt':
                    for human_line in fl:
                        human_line = human_line.split(', ')
                        id_ += 1
                        try:

                            if human_line[2] == 'None':
                                self.insert(table_name, f'{id_}, {human_line[0]}, {human_line[1]}, {human_line[2]}, {human_line[3]}')
                            elif human_line[2][2] == '.':
                                self.insert(table_name, f"{id_}, {human_line[0]}, {human_line[1]}, 'None', {human_line[3]}")
                            else:
                                pass

                        except Exception as _ex:
                            pass
# test
