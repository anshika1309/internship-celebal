DROP PROCEDURE IF EXISTS SP_Hierarchy;
GO
CREATE PROCEDURE SP_Hierarchy
AS
BEGIN
    SET NOCOUNT ON;
    TRUNCATE TABLE Employee_Hierarchy;

    WITH HierarchyCTE AS (
        -- Base Case
        SELECT 
            EmployeeID,
            ReportingTo,
            EmailID,
            1 AS Level,
            dbo.FIRST_NAME(EmailID) AS FirstName,
            dbo.LAST_NAME(EmailID) AS LastName
        FROM Employee_Master
        WHERE ReportingTo IS NULL

        UNION ALL

        -- Recursive Case with dynamic ID extraction
        SELECT 
            em.EmployeeID,
            em.ReportingTo,
            em.EmailID,
            h.Level + 1,
            dbo.FIRST_NAME(em.EmailID),
            dbo.LAST_NAME(em.EmailID)
        FROM Employee_Master em
        INNER JOIN HierarchyCTE h
            ON RIGHT(em.ReportingTo, CHARINDEX(' ', REVERSE(em.ReportingTo) + ' ') - 1) = h.EmployeeID
    )

    INSERT INTO Employee_Hierarchy (EmployeeID, ReportingTo, EmailID, Level, FirstName, LastName)
    SELECT * FROM HierarchyCTE;
END;
GO
