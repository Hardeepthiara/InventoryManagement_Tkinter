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
#pid","Category","Supplier","Name","Price","Quantity","Status"
    sql_create_product_table = """CREATE TABLE IF NOT EXISTS product_792(
                                pid integer PRIMARY KEY AUTOINCREMENT,
                                Category text,
                                Supplier text,
                                Name text,
                                Price text,
                                Quantity text,
                                Status text
                                );"""
    
    conn = create_connection(database)
    # create tables
    if conn is not None:
        # create Student table
        create_table(conn, sql_create_product_table)
       
    else:
        print("Error! cannot create the database connection.")




if __name__ == '__main__':
    main()