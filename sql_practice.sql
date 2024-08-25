SELECT SUM(ENGINEER.Count) as A FROM ENGINEER INNER JOIN DATA 
ON ENGINEER.ID = DATA.ID WHERE DATA.Type = 'FrontEnd';


select CONCAT(s.Name, ',' ,j.Date) as Offers
from Students s join Departments d
on (s.DepartmentId=d.DepartmentId)
left join Jobs j
on (s.Id=j.Id)
where j.Date is not NULL
order by d.DepartmentName
;


select
sum(distinct Salary) as Salary
from (
select s.Id,
s.Name,
s.DepartmentId,
j.Salary
from Students s, Jobs j
where s.Id = j.Id
and (select DepartmentName from Departments where Departments.DepartmentId=s.DepartmentId)='CSE'
) x
group by DepartmentId


--2nd highest
Select max(column)
from table1
where column < (Select max(column) from table)



-- highest by department
select max(column),department
from table1
group by department



--alternate table records
SELECT *
FROM Customers  
where customer_id % 2  == 0
order by country


-- Duplicate Values
select columnname,count(*)
from table1
group by columnname
having count(*) > 1




--Pattern matching 1
---Q1 display emp name whos name starts with 'm'
Select empname from table1 where empname like 'm%'
---Q2 display emp name whos name ends with 'n'
Select empname from table1 where empname like '%m'
---Q3 display emp name has 'n' in it
Select empname from table1 where empname like '%m%'
---Q4 display emp name does not has 'n' in it
Select empname from table1 where empname not like '%m%'



--Pattern matching 2
--Diplay name of all employees whoe name contains exactly 4 letters
SELCT ename from table where ename like '____'
--Display name of employees whose name contains the (i)second letter as 'L'(ii)fourthe letter as 'M'
(i)SELCT ename from table where ename like '_L%';
(ii)SELCT ename from table where ename like '___M%';
--Display employee name & hire dates for the employees joined in the month of December
SELECT hiredate,ename from table WHERE hiredate like 'DEC';
--Display name of employees whose name contains exactly 2 'L's
SELECT ename from table where ename like '%LL%'
--Display name of employees whose name starts with 'J' & ends with 'S'
SELECT ename from table where ename like 'J%S'


--Display nth row in SQL
option1
SELECT * from table WHERE rownum <= 4
minus SELECT * from table WHERE rownum <= 3
option2
SELECT * from (select rownum r, enam, sal from emp)WHERE r = 4;
option 3
SELECT * from (select rownum r, emp.* from emp) WHERE r in (2,3,7);


--UNION to get matching data from 2 tables
SELECT city from table1
UNION
SELECT city from table2

SELECT city from table1
UNION ALL
SELECT city from table2


--INNERJOIN
SELECT ename,sal,d.deptno,dname,loc from emp e,dept d WHERE e.deptno = d.deptno
-- Display employees who are working in location Chicago from emp dept.table
SELECT ename,sal,d.deptno,dname,loc from emp e,dept d
WHERE e.deptno = d.deptno AND loc = 'Chicago'
-- Display department name & total salaries from each department
SELECT dname,sum(sal) from emp e department d
WHERE e.deptno = d.deptno
group by deptno


--SELF JOIN
SELECT e1.ename "employees" e2.ename "manager"
from emp e1 emp e2
WHERE e2.empno = e1.mgr
--Display employee details who are getting more salary than their manager salary
SELECT e1.ename "employees", e2.ename "manager", e2.sal
from emp e1 emp e2
WHERE e2.empno = e1.mgr  and e1.sal > e2.sal
--Display the employee details who joined before their manager
SELECT e1.ename "employees", e2.ename "manager", e2.sal
from emp e1 emp e2
WHERE e2.empno = e1.mgr  and e1.hiredate < e2.hiredate



--LEFT JOIN
SELECT rownum,ename,emp.deptno,dname,loc,job
FROM emp LEFT JOIN dept
ON emp.deptno=dept.deptno AND dname = 'SALES'


--RIGHT JOIN
SELECT ename,job,sale,loc,dname, dept.departmentno
FROM emp
RIGHT JOIN dept
ON dept.deptno = emp.deptno

--FULL JOIN
SELECT ename, sal, job, d.deptno, e.deptname, dname
FROM emp e
FULL JOIN dept d
ON d.deptno = e.deptno



--CROSS JOIN
SELECT ename, d.deptno,sal,dname,loc
from emp e
CROSS JOIN dept d
WHERE d.deptno = 50;


--Display first & Last rows from table
SELECT * from (select rownum r, ename, sal from emp)
WHERE r=1 or r = (select count(*) from emp)
--Diplay last two rows of the columns
option1
SELECT * FROM emp
minus
SELECT * FROM emp
WHERE rownum <=(select count(*)-2 from emp)
option2
SELECT * FROM (select rownum r, emp.* from emp)
WHERE r > (SELECT count(*)-2 from emp) or r in (1,2)
--displany alternate records
SELECT * FROM (select rownum r, emp.* from emp)
WHERE mod(r,2)=1 (for odd)/mod(r,2)=0 (for even)


--nth Highest Salary
SELECT * from (SELECT DISTINCT sal from emp order by sal desc)
WHERE rownum <= 3
minus
SELECT * from (SELECT DISTINCT sal from emp order by sal desc)
WHERE rownum <= 2



--INTERSECT SQL (SET operators) dont use semicolon
SELECT column FROM table1
INTERSECT
SELECT column FROM table2



--MINUS in SQL
SELECT city from table1
MINUS
SELECT city from table2


--Normal form of sql data


##################################################################################################################################################################################

Q1. Write a query to fetch the EmpFname from the EmployeeInfo table in the upper case and use 
the ALIAS name as EmpName.

SELECT upper(EmpFname) as EmpName from EmployeeInfo ;


Q2. Write a query to fetch the number of employees working in the department ‘HR’.

SELECT count(*) from EmployeeInfo  WHERE department = 'HR';


Q3. Write a query to get the current date.

SELECT getdate();


Q4. Write a query to retrieve the first four characters of  EmpLname from the EmployeeInfo table.

SELECT EmpLname  from EmployeeInfo  where EmpLname   like '____%'
OR
SELECT substring(EmpLname , 1,4) from EmployeeInfo



Q5. Write a query to fetch only the place name(string before brackets) from the Address column of EmployeeInfo table.

SELECT substring(address,1, CHARINDEX('(', Address) ) from EmployeeInfop;



Q6. Write a query to create a new table which consists of data and structure copied from the other table.


SELECT * INTO newtable FROM EmployeeInfo WHERE 1=0
OR
CREATE TABLE NewTable AS SELECT * FROM EmployeeInfo;


Q7. Write q query to find all the employees whose salary is between 50000 to 100000.

SELECT salary from EmployeePosition where salary >= 5000 AND salary <= 100000;
OR
SELECT * FROM EmployeePosition WHERE Salary BETWEEN '50000' AND '100000';


Q8. Write a query to find the names of employees that begin with ‘S’

SELECT empname from employee where empname like 'S%';


Q9. Write a query to fetch top N records.

SELECT * FROM table limit 10;


Q10. Write a query to retrieve the EmpFname and EmpLname in a single column as “FullName”. The first name and the last name must be separated with space.

SELECT CONCAT(EmpFname ,' ',EmpLname) as FULLNAME  FROM EmployeeInfop;


Q11. Write a query find number of employees whose DOB is between 02/05/1970 to 31/12/1975 and are grouped according to gender

SELECT COUNT(*),gender from employeestable
WHERE DOB BETWEEN '02/05/1970 ' AND '31/12/1975'
GROUP BY gender ;


Q12. Write a query to fetch all the records from the EmployeeInfo table ordered by EmpLname in descending order and Department in the ascending order.

SELECT * from EmployeeInfo ORDER BY EmpLname  DESC, Department ASC;



Q13. Write a query to fetch details of employees whose EmpLname ends with an alphabet ‘A’ and contains five alphabets.

SELECT EmpLname FROM EmployeeInfo WHERE EmpLname like '____A'


Q14. Write a query to fetch details of all employees excluding the employees with first names, “Sanjay” and “Sonia” from the EmployeeInfo table.


SELECT * FROM EmployeeInfo WHERE EmpFname NOT IN (“Sanjay”,“Sonia”  ) ;



Q15. Write a query to fetch details of employees with the address as “DELHI(DEL)”.

SELECT * from table WHERE address = 'DELHI(DEL)%'


Q16. Write a query to fetch all employees who also hold the managerial position.

SELECT e.empname,p.position from EmployeeInfo e LEFT JOIN EmployeePosition p
ON e.empid = p.empid
AND p.Empposition IN ('Manager');


Q17. Write a query to fetch the department-wise count of employees sorted by department’s count in ascending order.

SELECT department,COUNT(empnid) as deptcount from EmpTable
GROUP BY department
ORDER BY deptcount ASC;


Q18. Write a query to calculate the even and odd records from a table.

SELECT * FROM (SELECT rownum r, table.* from table) WHERE MOD(r,2)=0;
SELECT * FROM (SELECT rownum r, table.* from table) WHERE MOD(r,2)=1;


Q19. Write a SQL query to retrieve employee details from EmployeeInfo table who have a date of joining in the EmployeePosition table.


SELECT * FROM EmployeeInfo e JOIN EmployeePosition p
ON e.empid = p.empid
WHERE p.DOJ NOT NULL ;


Q20. Write a query to retrieve two minimum and maximum salaries from the EmployeePosition table.

SLECT DISTINCT salary FROM employeepostiontable E1
WHERE 2 >= (SELECT COUNT(DISTINCT salary) FROM employeepostiontable  E2
WHERE E1.Salary >= E1.Salary ) ODER BY E1.Salary DESC;



Q21. Write a query to find the Nth highest salary from the table without using TOP/limit keyword.

SELECT salary FROM Table e1
WHERE N-1 = (SELECT COUNT(DISTINCT (E2.Salary))
FROM table e2
WHERE e2.Salary > e1.Salary);


Q22. Write a query to retrieve duplicate records from a table.

SELECT empname,empdept,COUNT(*) c FROM EmployeeTable
GROUP BY empname,empdept
WHERE c > 1;


Q23. Write a query to retrieve the list of employees working in the same department.

SELECT DISTINCT e.empid,e.empname,e.department FROM empinfotable e, employeetable e1
WHERE e.department = e1.department AND e.empid != e1.empid


Q24. Write a query to retrieve the last 3 records from the EmployeeInfo table.

SELECT * FROM (SELECT rownum r, table.* from table)
where r IN (1,3)

Q25. Write a query to find the third-highest salary from the EmpPosition table.

SELECT DISTINCT  max(salary) from Table
WHERE salary < (SELECT DISTINCT  max(salary) from Table
WHERE salary < (SELECT DISTINCT  max(salary) from Table) )


Q26. Write a query to display the first and the last record from the EmployeeInfo table.


SELECT * FROM Table WHERE EmpId= (SELECT MIN(EmpID) FROM Table) AND EmpID=(SLECT MAX(EmpID) FROM Table)


Q27. Write a query to add email validation to your database

SELECT Email FROM EmployeeInfo WHERE NOT REGEXP_LIKE(Email, ‘[A-Z0-9._%+-]+@[A-Z0-9.-]+.[A-Z]{2,4}’, ‘i’);


Q28. Write a query to retrieve Departments who have less than 2 employees working in it.

SELECT department, COUNT(empid) from table GROUP BY department having COUNT(empid) < 2;


Q29. Write a query to retrieve EmpPostion along with total salaries paid for each of them.

SELECT Empposition, SUM(Salary) from Table GROUP BY Empposition;


Q30. Write a query to fetch 50% records from the EmployeeInfo table.

SELECT * FROM EmployeeInfo WHERE empId <= (SELECT COUNT(empid)/2 from EmployeeInfo )


##################################################################################################################################################################################


Q1. Write a query to extract username(characters before @ symbol) from the Email_ID column.

SELECT SUBSTR(Email_ID, 1, INSTR(Email_ID, '@') - 1) FROM STUDENT;

Q2. Write a query to extract domain name like .com, .in, .au etc. from the Email_ID column.

SELECT SUBSTR(Email_ID, INSTR(Email_ID, '.') ) FROM STUDENT;


Q3. Write a query to extract email service provider names like google, yahoo, outlook, etc. from the Email_ID column.

SELECT SUBSTR(Email_ID, INSTR(Email_ID, '@') + 1, INSTR(Email_ID, '.') -
INSTR(Email_ID, '@') - 1) FROM STUDENT;


Q4. What is(are) the output of the following query?
SELECT CEIL(-12.43), FLOOR(-11.92) FROM DUAL;


Q5. Write a query to extract all the consonants present in your name.

SELECT TRANSLATE('Narendra', 'xaeiou', 'x') FROM DUAL;

Q6. Write a query to extract all the vowels present in your name.

SELECT TRANSLATE('Narendra', 'a' || TRANSLATE('Narendra', 'xaeiou', 'x'), 'a') FROM DUAL;


Q7. Write a query to extract the employees details who joined in the year 1981.

SELECT * FROM Table WHERE TO_CHAR(hire_date, YY) == 81;


Q8. Write a query to find the hiked salary for each employee after adding the commission.

SELECT NVL2(comm, comm+sal, sal) as hiked sal from table;


Q9. Write a query to find out the employees drawing salary more than their managers.

SELECT E.EMPNO, E.ENAME, E.SAL, M.EMPNO, M.ENAME, M.SAL
FROM EMP E, EMP M
WHERE E.MGR = M.EMPNO AND E.SAL > M.SAL;


Q10. Write a query to find out the subordinates (reportees) who joined the organization before their managers.

SELECT E.EMPNO, E.ENAME,E.HIREDATE, M.EMPNO, M.ENAME, M.HIREDATE
FROM EMP E, EMP M
WHERE E.MGR = M.EMPNO AND E.hiredate < M.hiredate


Q11. Write a query to find out the employees who dont have any subordinates (reportees) i.e. the employees who are not the managers.

SELECT * FROM EMP WHERE EMPNO NOT IN (SELECT DISTINCT NVL(mgr,0)FROM EMP)


Q12. Write a query to find out 2nd senior-most employee i.e. who joined the organization second as per hire date.

SELECT * FROM EMP e WHERE 2 = (SELECT COUNT(DISTINCT m.hire_date) FROM EMP m
WHERE e.hire_date >= m.hire_date);



Q13. Write a query to find out the 5th maximum salary.

SELECT * FROM EMP e WHERE 5 = (SELECT COUNT(DISTINCT salary) from EMP m
WHERE e.salary <= m.salary );


Q14. Write a query to find out the deviation from average salary for the employees who are getting more than the average salary.

SELECT ENAME, SAL, ROUND((SELECT AVG(SAL) FROM EMP),2) AS AVG, ROUND(SAL - (SELECT AVG(SAL) FROM EMP),2) AS DIFF FROM EMP WHERE SAL > (SELECT AVG(SAL) FROM EMP);

Q15. Write a query to find out the employees who are getting the maximum salary in their departments.

SELECT * EMP WHERE salary IN (SELECT MAX(salary) from EMP WHERE GROUP BY Department)


Q16. Write a query to find out department-wise minimum salary, maximum salary, total salary, and average salary.

SELECT D.DEPTNO, MIN(SAL), MAX(SAL), SUM(SAL), AVG(SAL) FROM EMP E, DEPT D WHERE E.DEPTNO = D.DEPTNO GROUP BY D.DEPTNO;


-- Online SQL Editor to Run SQL Online.
-- Use the editor to create new tables, insert data and all other SQL operations.
  CREATE DATABASE IF NOT EXIST my_db
  CREATE TABLE my_table
  (
  )
  CREATE TABLE table_copy as (SELECT * FROM main_table where 1=2)
  CREATE TABLE table_copy SELECT * FROM main_table
 
  SELECT MAX(salary) FROM employee WHERE salary < (SELECT MAX(salary) from emplyee WHERE salary < (SELECT * FROM employee))

