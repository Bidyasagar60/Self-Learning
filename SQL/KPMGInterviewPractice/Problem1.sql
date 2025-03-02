USE KPMG

/*

CREATE TABLE TRANSACTIONS
(
transaction_id	 INT,
customer_id		 INT,
transaction_date  DATE,	
revenue     DECIMAL(6,2)
)

INSERT INTO TRANSACTIONS VALUES
(1,3223,'2019-08-22',250.00),
(2,4563,'2019-11-18',300.00),
(3,3223,'2020-02-14',200.00),
(4,6712,'2020-05-20',150.00),
(5,4563,'2020-08-11',250.00),
(6,6712,'2020-10-22',300.00),
(7,3223,'2021-03-14',500.00),
(8,6712,'2021-06-10',350.00),
(9,4563,'2021-09-02',400.00),
(10,6712,'2021-12-14',250.00)


Calculate Customer Lifetime Value (CLV) :
As a Data Analyst in KPMG, you're given a database of transactions that customers have made. Each transaction record contains the customer_id, date of transaction, and revenue generated from the transaction.

Your task is to calculate the Customer Lifetime Value (CLV) for each customer. CLV is the total revenue a company can realistically expect from a single customer account. It considers a customer's revenue value and compares that number to the company's predicted customer lifespan. For this task, you'll not consider churn rate.

Assume each customer has at least 1 transaction. If the customer has more than 1 transaction calculate the CLV as the cumulative sum of the revenue for each customer over time. List the top 10 customers with the highest CLV.
*/


-- Answer 
SELECT 
        TOP 10 
		Customer_id,
		SUM(revenue) AS CLV

FROM Transactions
GROUP BY Customer_id
ORDER BY CLV DESC


