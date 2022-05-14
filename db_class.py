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
        with open(file_name) as fl:
            lines = fl.readlines()
            # self.insert(table_name, fl_line)
            id = 0
            for line in lines:
                id += 1
                line = '(' + 'str(id),' + line + ')'
                self.insert(table_name, line)

