-- Write your query below
UPDATE employees SET salary = 0 WHERE NOT(employee_id % 2 = 1 AND name NOT LIKE 'M%');
SELECT employee_id, salary AS bonus FROM employees ORDER BY employee_id;