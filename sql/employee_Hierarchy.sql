DROP TABLE IF EXISTS Employee_Hierarchy;
GO
CREATE TABLE Employee_Hierarchy (
    EmployeeID VARCHAR(10),
    ReportingTo VARCHAR(50),
    EmailID VARCHAR(100),
    Level INT,
    FirstName VARCHAR(50),
    LastName VARCHAR(50)
);
