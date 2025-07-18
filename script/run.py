import pyodbc

class SQLFileRunner:
    def __init__(self, server, database):
        self.server = server
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = pyodbc.connect(
                f'DRIVER={{ODBC Driver 17 for SQL Server}};'
                f'SERVER={self.server};'
                f'DATABASE={self.database};'
                
                f'Trusted_Connection=yes;' 
            )
            self.cursor = self.connection.cursor()
            print("✅ Connected to SQL Server.")
        except Exception as e:
            print("❌ Connection failed:", e)

    def run_sql_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                sql_script = file.read()
            
            for statement in sql_script.strip().split('GO'):
                if statement.strip():
                    self.cursor.execute(statement)
                    self.connection.commit()
            
            print(f"✅ Executed: {file_path}")
        except Exception as e:
            print(f"❌ Error in {file_path}:", e)

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("🔒 Connection closed.")

def main():
    server = 'LAPTOP-IQ2C90JF\\SQLEXPRESS'
    database = 'college'

    sql_files = [
        r"C:\Users\Mansi\OneDrive\Documents\internship\internship-celebal\sql\employee_master.sql",
        r"C:\Users\Mansi\OneDrive\Documents\internship\internship-celebal\sql\insertDataEmployee_Master.sql",
        r"C:\Users\Mansi\OneDrive\Documents\internship\internship-celebal\sql\employee_Hierarchy.sql",
        r"C:\Users\Mansi\OneDrive\Documents\internship\internship-celebal\sql\createFunction.sql",
        r"C:\Users\Mansi\OneDrive\Documents\internship\internship-celebal\sql\storedProcedure.sql",
        r"C:\Users\Mansi\OneDrive\Documents\internship\internship-celebal\sql\execution.sql"
    ]

    runner = SQLFileRunner(server, database)
    runner.connect()

    for file_path in sql_files:
        runner.run_sql_file(file_path)

    runner.close()

if __name__ == "__main__":
    main()
