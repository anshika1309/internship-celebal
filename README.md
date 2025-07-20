# 👩‍💻 Internship Project - Celebal Technologies

Welcome to the repository for my internship project at **Celebal Technologies**!  
This project focuses on automating the generation of **Employee Hierarchies** using **Microsoft SQL Server** and **Python**.


## 📁 Project Structure
sql/
├── employee_master.sql # Create Employee_Master table
├── insertDataEmployee_Master.sql # Insert sample employee data
├── employee_Hierarchy.sql # Create Employee_Hierarchy table
├── createFunction.sql # User-defined functions for name extraction
├── storedProcedure.sql # Stored procedure to generate hierarchy
├── execution.sql # Script to run the procedure and display output
main.py # Python script to automate execution


## ⚙️ Technologies Used

- **SQL Server (Microsoft sql server management studio with version (v 18.12.1)**
- **Python (pyodbc)**
- **Git / GitHub**
- **VS Code / SSMS**

- ## 🏗️ Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/anshika1309/internship-celebal.git
   cd internship-celebal

2. Run Python Script
Ensure you have Python and pyodbc installed:

pip install pyodbc
python main.py

3.Make sure your local SQL Server is running, and the EmployeeDB database exists.
For creating  EmployeeDB database 
IF DB_ID('EmployeeDB') IS NULL
    CREATE DATABASE EmployeeDB;

Output Example:-
After running the stored procedure, the employee_Hierarchy table is populated with levels and extracted names:

employeeId	reportingTo	    emailId	               level	   firstName	lastName
H1             NULL	      john.doe@example.com   	  1	     john	    doe
H3	         John Smith H1	alice.jones@example.com	  2	     alice	    jones
...	          ...	            ...	              ...	       ...	      ...

