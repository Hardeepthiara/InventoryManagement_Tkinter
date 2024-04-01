from sqlite3 import Error
import sqlite3
def create_connection(Inventory_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(Inventory_file)
        return conn
    except Error as e:
        print(e)
    
    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except Error as e:
        print(e)



def main():
    database = r'Inventory_file.db'

    sql_create_student_table = """CREATE TABLE IF NOT EXISTS Employee_506(
                                empid integer PRIMARY KEY AUTOINCREMENT,
                                name text,
                                gender text,
                                contact text,
                                dob text,
                                doj text,
                                email text,
                                password text,
                                utype text,
                                address text,
                                salary text
                                );"""
    
    conn = create_connection(database)
    # create tables
    if conn is not None:
        # create Student table
        create_table(conn, sql_create_student_table)
        #insert a row
        #student_1 = ('Hardeep', 'Kaur', 'Brampton')
        #student_2 = ('Rekha', 'Rani', 'Himlton')
        #student_3 = ('Tom', 'Marry', 'GTown')
        #student_4 = ('Sukhleen', 'Kaur', 'Mississauga')
        #StudentID = Student_info(conn, student_1)
        #StudentID = Student_info(conn, student_2)
        #StudentID = Student_info(conn, student_3)
        #StudentID = Student_info(conn, student_4)

        #print("All Students Details: ")
        #select_StudentInfor(conn)

        #print("Updated Student Details:")
        #update_StuInfo(conn, ('Thiara','Surry',1))
        #select_StudentInfor(conn)

        #print("Deleted Student Detail where student id is 2:")
        #delete_StudentInfo(conn, 2)
        #select_StudentInfor(conn)

    else:
        print("Error! cannot create the database connection.")







if __name__ == '__main__':
    main()