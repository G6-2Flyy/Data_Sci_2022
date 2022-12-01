-- 1. List the following details of each employee: employee number, last name, first name, sex, and salary
SELECT 
	Employees.emp_no, 
	Employees.last_name, 
	Employees.first_name, 
	Employees.sex, 
	Salaries.salary
FROM Employees
INNER JOIN Salaries ON Employees.emp_no=Salaries.emp_no;

-- 2. List first name, last name, and hire date for employees who were hired in 1986.
SELECT 
	first_name, 
	last_name, 
	hire_date 
FROM 
	Employees
WHERE
	hire_date BETWEEN '1986-01-01' AND '1986-12-31'
ORDER BY
	hire_date desc

--3. List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name.

SELECT
	departments.dept_no,
	departments.dept_name,
	employees.emp_no,
	employees.last_name,
	employees.first_name
FROM
	departments
	join dept_manager on departments.dept_no = dept_manager.dept_no
	join employees on employees.emp_no = dept_manager.emp_no
ORDER BY
	dept_no,
	last_name;
	
--4. List the department of each employee with the following information: employee number, last name, first name, and department name.
SELECT
	departments.dept_name,
	employees.emp_no,
	employees.first_name,
	employees.last_name
FROM
	departments
	join dept_manager on departments.dept_no = dept_manager.dept_no
	join employees on employees.emp_no = dept_manager.emp_no
ORDER BY
	dept_name,
	last_name;

--5. List first name, last name, and sex for employees whose first name is "Hercules" and last names begin with "B.
SELECT
	first_name,
	last_name,
	sex
FROM
	employees
WHERE
	first_name LIKE 'Hercules'
	AND last_name LIKE 'B%'
ORDER BY
	first_name;
--6. List all employees in the Sales department, including their employee number, last name, first name, and department name.
SELECT  e.emp_no,
        e.last_name,
        e.first_name,
        d.dept_name
FROM employees AS e
    INNER JOIN dept_emp AS de
        ON (e.emp_no = de.emp_no)
    INNER JOIN departments AS d
        ON (de.dept_no = d.dept_no)
WHERE d.dept_name = 'Sales'
ORDER BY e.emp_no;
--7. List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.
SELECT  e.emp_no,
        e.last_name,
        e.first_name,
        d.dept_name
FROM employees AS e
    INNER JOIN dept_emp AS de
        ON (e.emp_no = de.emp_no)
    INNER JOIN departments AS d
        ON (de.dept_no = d.dept_no)
WHERE d.dept_name = 'Sales'
	OR d.dept_name = 'Development'
ORDER BY
	emp_no;
--8. List the frequency count of employee last names (i.e., how many employees share each last name) in descending order.
SELECT
	last_name,
	count(*) as emp_counts
FROM
	employees 
GROUP BY
	last_name
order by
	emp_counts desc
limit 10;

