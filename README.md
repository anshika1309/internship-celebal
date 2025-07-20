# 👩‍💻 Internship Project - Celebal Technologies

Welcome to the repository for my internship project at **Celebal Technologies**!  
This project focuses on automating the generation of **Employee Hierarchies** using **Microsoft SQL Server** and **Python**.


## 📁 Project Structure
sql/
├── employee_master.sql               # Create Employee_Master table
├── insertDataEmployee_Master.sql    # Insert sample employee data
├── employee_Hierarchy.sql           # Create Employee_Hierarchy table
├── createFunction.sql               # User-defined functions for name extraction
├── storedProcedure.sql              # Stored procedure to generate hierarchy
├── execution.sql                    # Script to run the procedure and display output

script/
└── run.py                           # Python script to automate SQL execution




⚙️ Technologies Used
🐍 Python (with pyodbc)

🗃️ SQL Server (Microsoft SQL Server Management Studio v18.12.1)

🧠 Stored Procedures & User-defined Functions

💻 VS Code / SSMS

🧑‍💻 Git & GitHub


🏗️ Setup Instructions

1️⃣ Clone the Repository:
git clone https://github.com/anshika1309/internship-celebal.git
cd internship-celebal

2️⃣ Install Python Dependencies:
pip install pyodbc

3️⃣ Create the EmployeeDB Database (if not exists)
IF DB_ID('EmployeeDB') IS NULL
    CREATE DATABASE EmployeeDB;
    
4️⃣ Run the Python Script
python script/run.py

✅ This will create all the necessary tables, insert data, create functions and procedures, and finally populate the employee_Hierarchy table.

📊 Sample Output
After execution, the employee_Hierarchy table looks like:
| employeeId | reportingTo   | emailId                                                   | level | firstName | lastName |
| ---------- | ------------- | --------------------------------------------------------- | ----- | --------- | -------- |
| H1         | NULL          | [john.doe@example.com](mailto:john.doe@example.com)       | 1     | john      | doe      |
| H3         | John Smith H1 | [alice.jones@example.com](mailto:alice.jones@example.com) | 2     | alice     | jones    |
| ...        | ...           | ...                                                       | ...   | ...       | ...      |


