-- Write your query below
SELECT seller_name FROM seller WHERE seller_id NOT IN
(SELECT seller.seller_id FROM seller JOIN orders ON seller.seller_id = orders.seller_id WHERE extract(year from sale_date) = 2020)
ORDER BY seller_name;