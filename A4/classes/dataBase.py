import sqlite3

class DataBase():

    def __init__(self):

        self.dbConnection = sqlite3.connect('db.sqlite')
        self._initDatabase()
    
    def _initDatabase(self):

        sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS students (
                                        studentID text PRIMARY KEY,
                                        firstName text NOT NULL,
                                        lastName text NOT NULL,
                                        email text NOT NULL
                                    ); """
 
        sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS scholarships (
                                id integer PRIMARY KEY,
                                description text NOT NULL,
                                amount real
                                );"""
        if self.dbConnection is not None:
            # create projects table
            c = self.dbConnection.cursor()
            c.execute(sql_create_projects_table)
            c.execute(sql_create_tasks_table)
            c.close()
        else:
            print("Error Connecting to the Database.")
            exit(1)
    

    