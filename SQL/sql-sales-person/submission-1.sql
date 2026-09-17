-- Write your query below
SELECT name FROM sales_person WHERE sales_id NOT IN
(SELECT sales_person.sales_id FROM sales_person JOIN orders on orders.sales_id = sales_person.sales_id JOIN company on company.com_id = orders.com_id WHERE company.name = 'CRIMSON');