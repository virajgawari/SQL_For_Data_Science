-- Display the names of employees who do not have a manager.

SELECT ENAME
FROM EMP
WHERE MGR IS NULL;

-- Display the employee name and annual salary.

SELECT ENAME, SAL * 12 AS ANNUAL_SALARY
FROM EMP;

-- Display employees who earn commission.

SELECT *
FROM EMP
WHERE COMM IS NOT NULL;

-- Display the department number and total salary paid in each department.

SELECT DEPTNO, SUM(SAL) AS TOTAL_SALARY
FROM EMP
GROUP BY DEPTNO;

--  Display the job and average salary for each job role.

SELECT JOB, AVG(SAL) AS AVG_SALARY
FROM EMP
GROUP BY JOB;
