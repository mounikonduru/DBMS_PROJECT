import psycopg2
import pandas as pd
import warnings
import os
os.system('CLS')
warnings.filterwarnings('ignore')
def initialize():
    connection = psycopg2.connect(
        user = "postgres", #username that you use
        password = "Mouni@99", #password that you use, you don't need to include your password when submiting your code
        host = "localhost", 
        port = "5432", 
        database = "testing"
    )
    connection.autocommit = True
    return connection
    
# If you need to add new tables to your database you can use the following function to create the target table 
# assuming that conn is a valid, open connection to a Postgres database
def runQuery(conn):
    select_Query = " SELECT employee_id, department_id AS dpt_Name FROM employee_information ;"
    editions_df = pd.DataFrame(columns = ['employee_id', 'dpt_name'])
    with conn.cursor() as cursor:
        cursor.execute(select_Query)
        records = cursor.fetchall()
        for row in records:
            output_df = {'employee_id': row[0], 'dpt_name' : row[1]}
#             print("employee_id = ", row[0], )
#             print("dpt_name = ", row[1] )
            editions_df = editions_df.append(output_df, ignore_index=True)
    
        print(editions_df)

def main():
    conn = initialize()
    runQuery(conn)

if __name__ == "__main__":
    main()
