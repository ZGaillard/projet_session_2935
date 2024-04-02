import pymssql

conn_params = {
    'server'    : 'localhost',
    'user'      : 'SA',
    'password'  : 'Password123',
    'database'  : 'CASTINGAPP',
    'autocommit': True
}


class DBManager:
    def __init__(self):
        self.conn = pymssql.connect(**conn_params)
        self.cursor = self.conn.cursor()

    def read(self, table_name, attributes):
        sql_command = f"SELECT {attributes} FROM {table_name};"
        self.cursor.execute(sql_command)
        return self.cursor.fetchall()

    def read_where(self, table_name, attributes, condition):
        sql_command = f"SELECT {attributes} FROM {table_name} WHERE {condition};"
        self.cursor.execute(sql_command)
        return self.cursor.fetchall()

    def insert(self, data_tuple, table_name):
        sql_command = f"INSERT INTO {table_name} VALUES {data_tuple};"
        self.cursor.execute(sql_command)

    def update(self, table_name, attribute, value, condition):
        sql_command = f"UPDATE {table_name} SET {attribute}={value} WHERE {condition};"
        self.cursor.execute(sql_command)

    def delete(self, table_name, condition):
        sql_command = f"DELETE FROM {table_name} WHERE {condition};"
        self.cursor.execute(sql_command)

    def execute(self, sql_command):
        self.cursor.execute(sql_command)

    def run_function(self, function_name, *args):
        self.cursor.execute(f"EXEC {function_name} {args};")

    def __del__(self):
        self.cursor.close()
        self.conn.close()
