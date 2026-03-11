DROP TABLE IF EXISTS supermarket_sales;

CREATE TABLE supermarket_sales(
	gender VARCHAR(10),
	invoice_id TEXT,
	branch VARCHAR(10),
	city TEXT,
	customer VARCHAR(10),
	product_line TEXT,
	unit_price NUMERIC(10, 2),
	quantity INT,
	tax_5percent NUMERIC(10, 2)
);

\copy supermarket_sales FROM 'C:\\Program Files\\PostgreSQL\\18\\data\\supermarketSales\\supermarket_sales_new.csv' DELIMITER ',' CSV HEADER;
--Consider ',' as data separator
--Read file as CSV file and skip first line
--Note: Unlike normal SQL, meta‑commands are parsed by psql client itself; they don’t support line breaks the way SQL statements do.

SELECT COUNT(*) FROM supermarket_sales;
SELECT * FROM supermarket_sales LIMIT 5;

-- QUERY 1: RANK BRANCHES BY TOTAL SALES
\copy (SELECT branch, SUM(unit_price*quantity) AS total_sales, SUM(tax_5percent) AS total_taxes FROM supermarket_sales GROUP BY branch ORDER BY total_sales DESC) TO 'C:/Users/Wong Shi Yuen/OneDrive/Documents/supermarketSales/branch_sales.csv' WITH CSV HEADER;

-- QUERY 2: IDENTIFY PRODUCT LINE WITH HIGHEST SALES PER BRANCH
\copy (SELECT branch, product_line, total_sales, total_taxes FROM (SELECT branch, product_line, SUM(unit_price*quantity) AS total_sales, SUM(tax_5percent) AS total_taxes, RANK() OVER (PARTITION BY branch ORDER BY SUM(unit_price*quantity) DESC) FROM supermarket_sales GROUP BY branch, product_line)) TO 'C:/Users/Wong Shi Yuen/OneDrive/Documents/supermarketSales/branch_bestsellers.csv' WITH CSV HEADER;

--'\copy' is used to convert results in CSV format.
--NOTE: '\copy' is PSQL command code; must be written on a single line.