DROP TABLE IF EXISTS Employee_Master;
GO

CREATE TABLE Employee_Master (
    EmployeeID VARCHAR(10),
    ReportingTo VARCHAR(50),
    EmailID VARCHAR(100)
);
