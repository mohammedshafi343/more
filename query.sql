-- database.sql
SELECT employees.name, departments.department_name, salaries.salary
FROM employees
JOIN salaries ON employees.employee_id = salaries.employee_id
JOIN departments ON employees.department_id = departments.department_id
WHERE salaries.salary > 50000
ORDER BY salaries.salary DESC;
