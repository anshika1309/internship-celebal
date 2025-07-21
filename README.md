# 👩‍💻 Internship Project - Celebal Technologies

Welcome to the repository for my internship project at **Celebal Technologies**!  
This project focuses on automating the generation of **Employee Hierarchies** using **Microsoft SQL Server** and **Python**.


⚙️ Technologies Used
🐍 Python (with pyodbc)

🗃️ SQL Server (Microsoft SQL Server Management Studio v18.12.1)



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
